# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:17:08 2022

@author: hp
"""
import pandas as pd
import json
import os.path
import random
import time
from admin import Admin 

class User(object):
    """
    This is the User/Customer class. This allows customer to operate and buy products. Get the bills for what he purchased.
    He has not priviledge to modify the database at anytime. it allow the user to buy any amount of product from any category as available.
    An error will occur if a customer tries to buy more than the available stock for any product.
    customer will get message out of stock (OOS) if the product exist but the quantity available is zero.
    customer can buy multiple products at the same time
    """
    def __init__(self):
        self.u=''
    #This is the function that gives the user the priviledge to buy products and get the details of teh transactions
    def user_fun(self):
        self.ad=Admin()
        print("======= Welcome to the User Inventory Management System ====")
        while (1):
            print("1)Display All Products With Details")
            print("2)Display Specific Product With Details")
            print("3)Display All Purchase Bills")
            print("4)Buy The Product")
            print("5)Exit")
            print("Enter Your Choice :- ")
            n = int(input())
            if (n == 1):
                
                self.ad.display_data()
            elif (n == 2):
                self.ad.display_specific_data()
            elif (n == 3):
                self.display_user_data()
            elif (n == 4):
                self.buy_product()
            elif (n == 5):
                break
            else:
                print("Invalid Choice...!!!")

    #This Function will help the user to track his purchase and all bills reports till today. 
    # This Function also provides information only to the User if he enters User ID
    def display_user_data(self):
    	
    	if (os.path.isfile("user_data.json") is False):
    		print("No User Reports are Present")
    		return
    	
    	self.fd = open("user_data.json", 'r')
    	txt = self.fd.read()
    	user_data = json.loads(txt)
    	self.fd.close()
    	print("Enter your User ID to Display All your Bills :- ")
    	i = input()
    	temp = pd.DataFrame()
    	
    	if i in user_data.keys():
    		for j in user_data[i].keys():
    			d = dict()
    			d['User ID'] = i
    			d['Purchase Number'] = j
    			for k in user_data[i][j].keys():
    				d[k] = user_data[i][j][k]
    			temp = temp.append(d, ignore_index=True)
    			d = dict()
    		temp = temp.reset_index(drop=True)
    		
    		from IPython.display import display
    		display(temp)
    	else:
    		print("You Have Entered Wrong User ID that is not Present in DataBase...!!!")
        
    
    # This function allow User/Customer to get his bill regarding purchases done by him just after the purchase 
    #with a unique 10 digit Transaction ID. 
    #If a user buys multiple products in one go it will give an aggregate bill.
    def generate_bill(self, user_id, prod_id, price, time_date,
    				purchase_no, name, category,
    				quantity_all, transaction_id):
    	print("================================\
    ================= Bill ================\
    =================================")
    	print("########################################")
    	print(" User ID :-", user_id)
    	print("############################################")
    	amount = 0
    	n = len(purchase_no)
    	
    	for i in range(n):
    		print("--------------------------------------")
    		amount = amount+float(price[i])*float(quantity_all[i])
    		print("Purchase number", purchase_no[i],
    			"\nPurchase Time :-", time_date[i],
    			"\nProduct ID :-", prod_id[i],
    			"\nName Of Product :-",
    			name[i], "\nCategory Of Product :-", category[i],
    			"\nPrice of Product per Item :-", price[i],
    			"\nPurchase Quantity :-", quantity_all[i])
    		print("-------------------------------------------------")
    	print("*********************************************************")
    	print("	 Total Payable Bill :-",
    		amount, "Transaction ID :-", transaction_id)
    	print("*************************************")


    # This is the main function of this class. it allow the user to buy any amount of product from any category as available.
    # An error will occur if a customer tries to buy more than the available stock for any product.
    #customer will get message out of stock (OOS) if the product exist but the quantity available is zero.
    # customer can buy multiple products at the same time
    def buy_product(self):
    	
    	if (os.path.isfile("user_data.json") is False):
    		user_data = {}
    	else:
    		self.fd = open("user_data.json", 'r')
    		txt = self.fd.read()
    		user_data = json.loads(txt)
    		self.fd.close()
    		
    	self.fd = open("data.json", 'r')
    	txt = self.fd.read()
    	data = json.loads(txt)
    	self.fd.close()
    	print("Enter Your User ID if You are Old Customer\
    	else press '0' To New User ID :- ")
    	p = int(input())
    	
    	if (p == 0):
    		if (len(user_data.keys()) == 0):
    			user_id = 1000
    		else:
    			user_id = int(list(user_data.keys())[-1])+1
    	else:
    		if str(p) in user_data.keys():
    			user_id = p
    		else:
    			user_id = -1
    			
    	if (user_id != -1):
    		user_id = str(user_id)
    		price = []
    		time_date = []
    		purchase_no = []
    		name = []
    		category = []
    		quantity_all = []
    		prod_id = []
    		transaction_id = ''.join(random.choice(
    			'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
    		print("Enter Number of Products You Want To Buy :- ")
    		n = int(input())
    		print("Enter Data As Follows :- ")
    		
    		if user_id not in user_data.keys():
    			user_data[user_id] = {}
    			g = 0
    		else:
    			g = int(list(user_data[user_id].keys())[-1])+1
    			
    		for i in range(n):
    			print("Enter Product ID of Product " +
    				str(i+1)+" that you want to buy")
    			id = input()
    			
    			if id in data.keys():
    				user_data[user_id][str(i+1+g)] = {}
    				user_data[user_id][str(i+1+g)]['time_date'] = str(time.ctime())
    				time_date.append(str(time.ctime()))
    				if(float(data[id]['quantity']) == 0):
    					print("Product You Want is Currently Out Of Stock...!!!")
    					continue
    					
    				purchase_no.append(i+1+g)
    				name.append(data[id]['name'])
    				user_data[user_id][str(i+1+g)]['name'] = data[id]['name']
    				prod_id.append(id)
    				user_data[user_id][str(i+1+g)]['product_id'] = id
    				category.append(data[id]['category'])
    				user_data[user_id][str(
    					i+1+g)]['category'] = data[id]['category']
    				print("For Product "+str(data[id]['name']) +
    					" Available Quantity is :- "+str(data[id]['quantity']))
    				print("Enter Quantity of Product " +
    					str(i+1)+" that you want to buy")
    				quantity = input()
    				
    				if (float(quantity) <= float(data[id]['quantity'])):
    					data[id]['quantity'] = str(
    						float(data[id]['quantity'])-float(quantity))
    					quantity_all.append(quantity)
    					user_data[user_id][str(i+1+g)]['quantity'] = str(quantity)
    					price.append(data[id]['price'])
    					user_data[user_id][str(i+1+g)]['price'] = data[id]['price']
    					user_data[user_id][str(
    						i+1+g)]['Transaction ID'] = str(transaction_id)
    				else:
    					print(
    						"The Quantity You Have Asked is Quite High\
    						Than That is Available in Stock")
    					print(
    						"Did you Want To buy According to The Quantity\
    						Available in Stock then Enter '0' Else '1'\
    						to skip This Product")
    					key = int(input())
    					
    					if (key == 0):
    						print("Enter Quantity of Product " +
    							str(i+1)+" that you want to buy")
    						quantity = input()
    						if (float(quantity) <= float(data[id]['quantity'])):
    							data[id]['quantity'] = str(
    								float(data[id]['quantity'])-float(quantity))
    							quantity_all.append(quantity)
    							user_data[user_id][str(
    								i+1)]['quantity'] = str(quantity)
    							price.append(data[id]['price'])
    							user_data[user_id][str(
    								i+1)]['price'] = data[id]['price']
    							user_data[user_id][str(
    								i+1+g)]['Transaction ID'] = str(transaction_id)
    						else:
    							print("Invalid Operation Got Repeated...!!!")
    					elif (key == 1):
    						continue
    					else:
    						print("Invalid Choice...!!!")
    			else:
    				print("Invalid Product ID...!!!")
    		if(len(purchase_no) != 0):
    			self.generate_bill(user_id, prod_id, price, time_date, purchase_no,
    						name, category, quantity_all, transaction_id)
    	else:
    		print("User ID Doesn't Exists...!!!")
    	self.js = json.dumps(data)
    	self.fd = open("data.json", 'w')
    	self.fd.write(self.js)
    	self.fd.close()
    	self.js = json.dumps(user_data)
    	self.fd = open("user_data.json", 'w')
    	self.fd.write(self.js)
    	self.fd.close()
