import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number=input("Enter your number: ")
phone= phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
sim=carrier.name_for_number(phone,"en")
regester=geocoder.description_for_number(phone,"en")
print(number)
print(phone)
print(time)
print(sim)
print(regester)
