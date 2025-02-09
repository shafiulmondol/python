# write a programe to display user entared name folowed by good afternoon using input function
a=input("enter your name:\n")
import pyttsx3
shafiul = pyttsx3.init()
shafiul.say(f"hellow- {a} sir Good afternoon. What can I do for you?")# for writting a string and a veriable at a time we can use f and {}
shafiul.runAndWait()
