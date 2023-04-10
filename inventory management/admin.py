# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import json
import os.path



class Admin(object):
    """
    This is the administrative class. Only the admin is allowed to insert, delete, update the database at anytime
    Users does not have priviledge to insert, delete or update the database.
    """
    def __init__(self):
        self.n=''
    
    #This is the function that gives the admin the priviledge to insert, delete, update the product details as required
    def admin_fun(self):    
        print("============= Welcome to the Medy Admin Inventory Management System =====")
     
        while (1):
            print("1)Display DataBase/All Products with there details")
            print("2)Display Specific Product with its details")
            print("3)Insert Data Into DataBase")
            print("4)Update Product in Database")
            print("5)Delete Product in DataBase")
            print("6)Display User Purchase Reports")
            print("7)Exit")
            print("Enter Your Choice :- ")
             
            n = int(input())
            if (n == 1):
                self.display_data()
            elif (n == 2):
                self.display_specific_data()
            elif (n == 3):
                self.add_new()
            elif (n == 4):
                self.update_prod_data()
            elif (n == 5):
                self.delete_prod()
            elif (n == 6):
                self.display_reports_admin()
            elif (n == 7):
                break
            else:
                print("Invalid Choice...!!!")
            
    #The two next functions show all product in inventory 
    # the Admin have the perrogatory to either wants all all list as it is in Database or
    # else he wants to have a look at all products by their categories.
    
    # This function allow Admin to display all the products in the inventory
    def display_data(self):
        
        #self.p=prd()
    	self.fd = open("data.json", 'r') # Open file in read mode
    	txt = self.fd.read() # reading data from file
    	data = json.loads(txt)
    	
    	# This will parse the JSON data,
    	# populates a Python dictionary with the data
    	self.fd.close()
    	print("Enter '0' To Display Data Category Wise or '1' \
    	To Show Data As its Sequence Of Insertion :- ")
    	n = int(input())
    	
    	# Display All Records
    	if (n == 1):
    		table = pd.DataFrame(
    			columns=['ID', 'name', 'price', 'category',
    					'quantity', 'date'])
    		
    		# Creating Pandas dataframe to show data in table
    		# format later
    		for i in data.keys():
    			'''Fetch all keys in dictionary'''
    			temp = pd.DataFrame(columns=['ID'])
    			temp['ID'] = [i]
    			
    			for j in data[i].keys():
    				temp[j] = [data[i][j]]
    			table = table.append(temp)
    		table = table.reset_index(drop=True)
    		
    		# This will reset index of dataframe
    		from IPython.display import display
    		display(table)
    	elif (n == 0):
    	
    		# Display Records by Category
    		table = pd.DataFrame(
    			columns=['ID', 'name', 'price', 'category',
    					'quantity', 'date'])
    		cat = []
    		
    		for i in data.keys():
    			temp = pd.DataFrame(columns=['ID'])
    			temp['ID'] = [i]
    			for j in data[i].keys():
    				temp[j] = [data[i][j]]
    				if (j == 'category'):
    					cat.append(data[i][j])
    			table = table.append(temp)
    			table = table.reset_index(drop=True)
    			cat = set(cat)
    			cat = list(cat)
    			
    		for k in cat:
    			temp = pd.DataFrame()
    			temp = table[table['category'] == k]
    			print("Data Of Products Of Category "+k+" is:- ")
    			from IPython.display import display
    			display(temp)
    	else:
    		print("Enter Valid Choice...!!!")
    		
    # This function allow Admin to display a specific product by category in the inventory
    def display_specific_data(self):
        self.fd = open("data.json", 'r')
        txt = self.fd.read()
        data = json.loads(txt)
        self.fd.close()
        print("Enter Product ID Whose Details You Want to Have a Look on :- ")
        i = input()
         
        # Following Code will Filter out Product ID from Records
        if i in data.keys():
            temp = pd.DataFrame(columns=['ID'])
            temp['ID'] = [i]
             
            for j in data[i].keys():
                temp[j] = [data[i][j]]
                 
            from IPython.display import display
            display(temp)
        else:
            print("You Have Entered Wrong Product ID \
            that is not Present in DataBase...!!!")


    def add_new(self):
        
        ##In this Function, Admin will have to enter the Product ID of the product to 
        #see the details he wants to check he will get all details regarding that particular product
        
    	self.fd = open("data.json", 'r')
    	txt = self.fd.read()
    	data = json.loads(txt)
    	self.fd.close()
    	print("Enter New Product ID :- ")
    	id = input()
    	
    	if id not in data.keys():
    		print("Enter Product Name :- ")
    		name = input()
    		
    		print("Enter Price of Product(price for product quantity as 1) :- ")
    		price = input()
    		
    		print("Enter Category of Product :- ")
    		category = input()
    		
    		print("Enter Quantity of Product :- ")
    		quantity = input()
    		
    		print("Enter The Date on Which Product is Added in Inventory :- ")
    		date = input()
    		
    		data[id] = {'name': name, 'price': price,
    					'category': category, 'quantity': quantity, 'date': date}
    		print("Please Press '0' to Add New Attributes\
    		/Properties of Product or Press '1' to Continue :- ")
    		z = int(input())
    		
    		if(z == 0):
    			print("Enter Number of New Attributes/Properties of Product :- ")
    			n = int(input())
    			
    			for i in range(n):
    				print("Enter Attribute Name That you Want To Add :- ")
    				nam = input()
    				print("Enter The "+str(nam)+" of Product :- ")
    				pro = input()
    				data[id][nam] = pro
    		print("Product ID "+str(id)+" Added Successfully...!!!")
    		
    	else:
    		print("The Product ID you Have Entered Is Already Present\
    		t in DataBase Please Check...!!!")
    	self.js = json.dumps(data)
    	self.fd = open("data.json", 'w')
    	self.fd.write(self.js)
    	self.fd.close()
	

    # The function that allows admin to remove a product completely (if out of stock oos)
    # or product that need to be removed completely if the product is being stoped for sales in the future
    def delete_prod(self):
        self.fd = open("data.json", 'r')
        txt = self.fd.read()
        data = json.loads(txt)
        self.fd.close()
        print("Enter The Product ID of The Product Which You Want To Delete :- ")
        temp = input()
         
        if temp in data.keys():
           
              # here we are removing that particular data
            data.pop(temp) 
            print("Product ID "+str(temp)+" Deleted Successfully...!!!")
        else:
            print("Invalid Product ID...!!!")
        self.js = json.dumps(data)
        self.fd = open("data.json", 'w')
        self.fd.write(self.js)
        self.fd.close()


    #This function make sure the admin is able to update all details of the products 
    # and he can also edit a specifi detail/attribute of  the concerned product
    def update_prod_data(self):
    	self.fd = open("data.json", 'r')
    	txt = self.fd.read()
    	data = json.loads(txt)
    	self.fd.close()
    	print("Enter The Product ID of The Product\
    	Which You Want To Update :- ")
    	temp = input()
    	
    	if temp in data.keys():
    		print("Want to update whole product data\
    		press '0' else '1' for specific data :- ")
    		q = int(input())
    		if (q == 0):
    		
    			print("Enter Product Name :- ")
    			name = input()
    			
    			print("Enter Price of Product(price for product quantity as 1) :- ")
    			price = input()
    			
    			print("Enter Category of Product :- ")
    			category = input()
    			
    			print("Enter Quantity of Product :- ")
    			quantity = input()
    			
    			print("Enter The Date on Which Product is Added in Inventory :- ")
    			date = input()
    			
    			data[temp] = {'name': name, 'price': price,
    						'category': category, 'quantity': quantity,
    						'date': date}
    			print(
    				"Please Press '0' to Add more Attributes\
    				/Properties of Product or Press '1' to Continue :- ")
    			z = int(input())
    			if(z == 0):
    				print("Enter Number of New Attributes/Properties of Product :- ")
    				n = int(input())
    				
    				for i in range(n):
    					print("Enter Attribute Name That you Want To Add :- ")
    					nam = input()
    					print("Enter The "+str(nam)+" of Product :- ")
    					pro = input()
    					data[temp][nam] = pro
    			print("Product ID "+str(temp)+" Updated Successfully...!!!")
    			
    		elif(q == 1):
    			print("Enter Which Attribute of Product You want to Update :- ")
    			p = input()
    			
    			if p in data[temp].keys():
    				print("Enter "+str(p)+" of Product :- ")
    				u = input()
    				data[temp][p] = u
    				print("Product ID "+str(temp)+"'s attribute " +
    					str(p)+" is Updated Successfully...!!!")
    			else:
    				print("Invalid Product Attribute...!!!")
    		else:
    			print("Invalid Choice...!!!")
    	else:
    		print("Invalid Product ID...!!!")
    	self.js = json.dumps(data)
    	self.fd = open("data.json", 'w')
    	self.fd.write(self.js)
    	self.fd.close()
	
    # Admin report on daily transaction is very important.
    #This function allow the admin to be able to look at the purchases.
    # The admin can either check all purchase reports or check purchase report of any specific customer
    def display_reports_admin(self):
    	if (os.path.isfile("user_data.json") is False):
    	
    		# Check for if file is present or not
    		# File will be generated only
    		# if any user will do some purchase
    		print("No User Reports are Present")
    		return
    	
    	self.fd = open("user_data.json", 'r')
    	txt = self.fd.read()
    	user_data = json.loads(txt)
    	self.fd.close()
    	print("Enter '0' to Check All Bills/Reports and \
    	'1' To Check Specific User Bills/Reports :- ")
    	n = int(input())
    	
    	if (n == 1):
    		print("Enter User ID Whose Details You Want to Have a Look on")
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
    	elif (n == 0):
    		table = pd.DataFrame()
    		
    		for i in user_data.keys():
    			temp = pd.DataFrame()
    			
    			for j in user_data[i].keys():
    				d = dict()
    				d['User ID'] = i
    				d['Purchase Number'] = j
    				
    				for k in user_data[i][j].keys():
    					d[k] = user_data[i][j][k]
    				temp = temp.append(d, ignore_index=True)
    				d = dict()
    			table = table.append(temp)
    		table = table.reset_index(drop=True)
    		from IPython.display import display
    		display(table)
    	else:
    		print("Please Enter Valid Choice...!!!")

    #This allow the admin to delete all the database in the system if need be.        
    def delete_all(self):
    	self.fd = open("data.json", 'r')
    	txt = self.fd.read()
    	data = json.loads(txt)
    	self.fd.close()
    	data = {} # Replacing Data with NULL Dictionary
    	js = json.dumps(data)
    	self.fd = open("data.json", 'w')
    	self.fd.write(js)
    	self.fd.close()


