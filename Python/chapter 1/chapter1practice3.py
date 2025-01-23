# Install an external module use it to perform an operation of your interest
import pyttsx3
shafiul = pyttsx3.init()
print("***Write your text for listing:--\n")
mondol=input()
shafiul.say(mondol)
shafiul.runAndWait()