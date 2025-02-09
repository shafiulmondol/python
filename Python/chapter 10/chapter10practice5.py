'''write a class Train which has methods to book a trikets, got 
status(no of seats) and get fare information of train running under bangladeshi 
ralway'''
from random import randint
class train:
    def __init__(self,trainno) :
         self.trainno=trainno

    def book(self,fro,to):# its a mathod
        print("ticket is book in train no: ",self.trainno,"from",fro,"to",to)

    def statas(self):
         print("train no: ",self.trainno,"from is running on time")

    def fear(self,fro,to):
         print("ticket fear in train no: ",self.trainno,"from",fro,"to",to,"is",randint(222,5555))
t=train(123324)
t.book=("rangpur","dhaka")
t.statas()
t.fear("rangpur","dhaka")