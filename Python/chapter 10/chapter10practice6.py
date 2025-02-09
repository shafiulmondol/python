"""can you change the self peramiter inside a class to somthing else try 
changing self to slf or shafiul and see the effects """
#it will be no change
from random import randint
class train:
    def __init__(shafiul,trainno) :
         shafiul.trainno=trainno

    def book(shafiul,fro,to):# its a mathod
        print("ticket is book in train no: ",shafiul.trainno,"from",fro,"to",to)

    def statas(shafiul):
         print("train no: ",shafiul.trainno,"from is running on time")

    def fear(shafiul,fro,to):
         print("ticket fear in train no: ",shafiul.trainno,"from",fro,"to",to,"is",randint(222,5555))
t=train(123324)
t.book=("rangpur","dhaka")
t.statas()
t.fear("rangpur","dhaka")