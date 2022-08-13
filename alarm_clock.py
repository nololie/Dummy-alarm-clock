import playsound
import datetime

alarm_hour = int(input("Enter hour: "))
alarm_min = int(input("Enter minutes: "))
am_pm = input("am/pm")

if am_pm == "pm":
    alarm_hour += 12

while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_min == datetime.datetime.now().minute:
        print("It's time.....")
        playsound.playsound(
            "ty_dolla_ign_by_yourself_feat._bryson_tiller_jhene_aiko.mp3")
        break
