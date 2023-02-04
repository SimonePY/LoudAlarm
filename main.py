import datetime

import playsound

print("Welcome to your personal SimpleAlarm!")

alarm_zone = str(input("Set (AM/PM): ")).upper()
alarm_hour = int(input("Set the hour: "))
alarm_minute = int(input("Set the minutes: "))
alarm_seconds = int(input("Set the seconds: "))

alarm_time = datetime.datetime.now().replace(hour=alarm_hour, minute=alarm_minute, second=alarm_seconds, microsecond=0)
if alarm_zone == "PM" and alarm_hour != 12:
    alarm_time += datetime.timedelta(hours=12)

print(f"Alarm set for {alarm_time.strftime('%H:%M:%S %p')}.")

while True:
    now = datetime.datetime.now()
    if now >= alarm_time:
        print("Time to wake up!")
        playsound.playsound("sound.mp3", False)
        input("Press Enter to stop the alarm.")
        break
