# import pywhatkit as pyw
# a="+88"
# pyw.sendwhatmsg(a+(input("Enter your no: ")),input("Enter message:\n"),input("Enter time in hour: "),input("Enter time in miute: "))

# import pywhatkit as pyw
# b=[input("Enter your numbers: ")]
# a = "+88" + b
# message = input("Enter message:\n")
# hour = int(input("Enter time in hour: "))
# minute = int(input("Enter time in minute: "))

# pyw.sendwhatmsg(a, message, hour, minute)
import pywhatkit as pyw

# Input multiple numbers separated by commas
numbers = input("Enter your numbers separated by commas: ").split(',')

message = input("Enter message:\n")
hour = int(input("Enter time in hour: "))
minute = int(input("Enter time in minute: "))

# Loop through each number and send the message
for number in numbers:
    a = "+88" + number.strip()  # Adding country code and stripping any extra spaces
    pyw.sendwhatmsg(a, message, hour, minute)

    # Increment minute to avoid overlapping messages
    minute += 1
