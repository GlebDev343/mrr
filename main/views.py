from .models import MeterReading, InstalledMeter, PersonalAccount
from rest_framework.views import APIView


class MeterReadingsController(APIView):
    def post(current_value, time_of_taking, account_number):
        personal_account = PersonalAccount.objects.get(account_number=account_number)
        installed_meter = InstalledMeter.objects.get(personal_account=personal_account)
        meter_reading = MeterReading(
            current_value=current_value,
            time_of_taking=time_of_taking,
            installed_meter=installed_meter,
        )

        meter_reading.save()
        print("Record saved successfully")
