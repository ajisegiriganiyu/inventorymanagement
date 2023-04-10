# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:36:55 2022

@author: hp
"""

import json
import os.path
import pandas as pd

class Products:
    
    def __init__(self):
        """
        This is a class to generate a JSON file for the whole categories of products being sold in our Grocery
        No need to manually add any products in this class.
        The admin has only access to add product by category as required.
        """

        # Creating Dictionary to store data
        self.available_products = {1001: {"name": "chocolate drinks", "price": 230,
        							"category": "Beverages",
        							"quantity": 10, "date": "10/03/2022"},
        					1002: {"name": "coffee", "price": 250,
        							"category": "Beverages",
        							"quantity": 100,
        							"date": "15/07/2022"},
        					1003: {"name": "tea", "price": 500,
        							"category": "Beverages",
        							"quantity": 200, "date": "12/04/2022"},
        					1004: {"name": "Soy Drinks", "price": 20,
        							"category": "Beverages",
        							"quantity": 50, "date": "27/06/2022"},
        					1005: {"name": "Pop and Soda", "price": 700,
        							"category": "Beverages",
        							"quantity": 100,
        							"date": "30/01/2022"},
        					1006: {"name": "Carrying Case", "price": 33,
        							"category": "Phone accessories",
        							"quantity": 56, "date": "22/02/2022"},
        					1007: {"name": "earpieces", "price": 765,
        							"category": "Phone accessories",
        							"quantity": 70,
        							"date": "11/03/2022"},
        					1008: {"name": "Screen guards", "price": 764,
        							"category": "Phone accessories",
        							"quantity": 90, "date": "16/02/2022"},
        					1009: {"name": "Toilet paper", "price": 87,
        							"category": "Toiletries",
        							"quantity": 50, "date": "17/07/2021"},
        					1010: {"name": "Body Soap", "price": 24,
        							"category": "Toiletries", "quantity": 60,
        							"date": "20/05/2022"},
                            1011: {"name": "Scrubs", "price": 24,
        							"category": "Toiletries", "quantity": 60,
        							"date": "20/05/2022"},
                            1012: {"name": "Body Crème", "price": 24,
        							"category": "Toiletries", "quantity": 160,
        							"date": "20/05/2022"},
                            1013: {"name": "Shampoo", "price": 24,
        							"category": "Toiletries", "quantity": 60,
        							"date": "20/05/2022"},
                            1014: {"name": "Pizza", "price": 24,
        							"category": "Pastry", "quantity": 120,
        							"date": "20/05/2022"},
                            1015: {"name": "Burgers", "price": 24,
        							"category": "Pastry", "quantity": 130,
        							"date": "20/05/2022"},
                            1016: {"name": "Donuts", "price": 24,
        							"category": "Pastry", "quantity": 140,
        							"date": "20/05/2022"},
                            1017: {"name": "Muffins", "price": 24,
        							"category": "Pastry", "quantity": 160,
        							"date": "20/05/2022"},
                            1018: {"name": "Cheesecakes", "price": 104,
        							"category": "Pastry", "quantity": 100,
        							"date": "20/05/2022"},
                            1019: {"name": "Perfumes", "price": 56,
        							"category": "Cosmetics", "quantity": 100,
        							"date": "20/05/2022"},
                            1020: {"name": "vanishes", "price": 30,
        							"category": "Cosmetics", "quantity": 100,
        							"date": "20/05/2022"},
                            1021: {"name": "Nail Polish", "price": 25,
        							"category": "Cosmetics", "quantity": 120,
        							"date": "20/05/2022"},
                            1022: {"name": "Deodorants", "price": 54,
        							"category": "Cosmetics", "quantity": 90,
        							"date": "20/05/2022"},
                            1023: {"name": "Facial Scrubs", "price": 34,
        							"category": "Cosmetics", "quantity": 200,
        							"date": "20/05/2022"},
        					}
        
        # Formatting Dictionary into JSON format
        self.js = json.dumps(self.available_products)
        ''' json.dumps() function converts a Python object into a json string '''
        self.js # so we got all data in json string format here
        
        # Create Jason File for DataBase and Write data Into File
        self.fd = open("data.json", 'w')
        
        self.fd.write(self.js) # writing string into file
        self.fd.close() # Close File After Inserting Data
        


