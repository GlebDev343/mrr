import datetime
import random
import string
from main.views import MeterReadingsController
from main.models import PersonalAccount


def save_value(cv, an):
    time_now = datetime.datetime.now()
    MeterReadingsController.post(
        current_value=cv, time_of_taking=time_now, account_number=an
    )


def update_code_validity(an):
    personal_account = PersonalAccount.objects.get(account_number=an)
    time_now = datetime.datetime.now()
    digits = random.choices(string.digits, k=3)
    letters = random.choices(string.ascii_uppercase, k=3)
    sample = random.sample(digits + letters, 6)
    personal_account.verification_code = "".join(sample)
    personal_account.code_validity = time_now + datetime.timedelta(minutes=15)
    personal_account.save()
