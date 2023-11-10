import os
import datetime
import telebot

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mrr.settings")

import django

django.setup()

from telebot import types
from main.models import PersonalAccount
from Services.meter_reading_service import save_value, update_code_validity

token = "6472590444:AAH911J01CgccTCDJ0Wbhb56desyqaqVH2Y"
bot = telebot.TeleBot(token)

markup2 = types.ReplyKeyboardMarkup(
    row_width=1, resize_keyboard=True, one_time_keyboard=True
)
meter_reading_button = types.KeyboardButton("Meter Reading")
markup2.add(meter_reading_button)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello", reply_markup=markup2)
    bot.register_next_step_handler(message, start_meter_reading)


@bot.message_handler(commands=["write"])
def start_meter_reading(message):
    bot.send_message(message.chat.id, "Enter your personal account number:")


@bot.message_handler(regexp="^\d+$")
def check_pesonal_account(message):
    try:
        global account_number
        account_number = message.text
        personal_account = PersonalAccount.objects.get(account_number=account_number)
        if str(personal_account.code_validity) < str(datetime.datetime.now()):
            update_code_validity(account_number)
        bot.send_message(
            message.chat.id,
            "A confirmation code has been sent to your email, please enter the current value and code separated by a space",
        )
        print(personal_account.verification_code)
    except PersonalAccount.DoesNotExist:
        bot.send_message(
            message.chat.id,
            "You entered an incorrect account number, please try again:",
        )


@bot.message_handler(regexp="^\d+ \w+$")
def check_and_save_record(message):
    try:
        current_value = ""
        verification_code = ""
        for i in range(len(message.text)):
            if message.text[i] != " ":
                current_value += message.text[i]
            else:
                verification_code += message.text[i + 1 :]
                break
        if (
            PersonalAccount.objects.get(
                account_number=account_number, verification_code=verification_code
            ).verification_code
            == verification_code
        ):
            save_value(cv=current_value, an=account_number)
            bot.send_message(message.chat.id, "Hurray!")
    except PersonalAccount.DoesNotExist:
        bot.send_message(message.chat.id, "Invalid verification code, try again:")


bot.infinity_polling()
