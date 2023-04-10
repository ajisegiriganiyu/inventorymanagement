# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:18:17 2022

@author: hp
"""

#This is where all the class have been called and run
# Admin and customer have access to this. 

from products import Products as prd
from admin import Admin
from user import User





print(" =======================================")
print("// Welcome to Medy Grocery Store Checkout //")
print(" =======================================")

while (1):
    print("Choose Any One of The Following :- ")
    print("1)Admin")
    print("2)User")
    print("3)Exit")
    print("Enter Your Choice Here :- ")
    n = int(input())
    if (n == 1):
        ad=Admin()
        ad.admin_fun()
    elif (n == 2):
        us=User()
        us.user_fun()
    elif (n == 3):
        break
    else:
        print("Invalid Choice...!!!")
