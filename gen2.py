#python 3.7.1
"""
  So this is 2nd version, but not in C++
  I stopped develope C++ version
  Because #Really Hard lol
  (Maybe i will make it more simmilar)#
  But this is Python3 version,
  Made by GameHerobrine
  
"""
#version 1.3_rev 2(1.3_frev)
#next update: 1.4?

#version 1.3 rev:
  # Some Fixes
  # Fixed main bugs
  #One bug left
  
#version 1.3:
  # Full bug fix.
  #Maybe final version



import random
from random import randint

regeneration='1'
rquant='1'

def defend(value):
  
  try:
    if rquant<= '0' or regeneration<='0':
      print("Number of regen or quantity cant be less than 1")
      exit(0)
    else:
      val = int(value)
  except ValueError:
    print("You entered not interger")
    exit(0)
   
def regen():
  print("Not developed yet") #wtf lol no one use it

def fbug(): #final bug fix
  if min>max:
    print("Error.\nMin cant be more than max.")
    exit(99)
     
print("Enter min number\n>>>")
min= str(input(""))
defend(min)

print("Enter max number\n>>>")
max= str(input(""))
defend(max)

fbug()

print("Enter quantity of rand number\n>>>")
rquant= str(input(""))
defend(rquant)

#unuseful code
print("Enter Number of Number regeneration")
regeneration = str(input(">>>"))
defend(regeneration)

i=0

while i < int(rquant):
  rnum=random.randint(int(min),int(max))
  print("discord.gift/"+str(rnum))
  i= i+1

