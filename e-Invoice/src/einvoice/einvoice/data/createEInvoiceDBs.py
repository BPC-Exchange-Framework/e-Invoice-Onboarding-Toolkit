#!/Users/kelly/Dev/virtualenvs/e-Invoice/bin python

# Author: Kelly Kinney
# Date: 2021-06-22 (June 22, 2021)
# File: createEInoviceDBs.py
# About: Create three small databases for invoice data
# Notes: chmod 755 create_dev_struct.sh in order to execute.
#
# LICENSE
# Copyright (C) 2021 Kelly Kinney
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# A copy of the GNU General Public License is included in the GitHub
# repository root which contained this file.  
# If not, see <http://www.gnu.org/licenses/>.

from faker  import Faker
from tinydb import TinyDB, Query
import csv
import random


dbAddresses = TinyDB('./tinydb_Addresses.json')
dbLineItems = TinyDB('./tinydb_LineItems.json')
# dbInvoices  = TinyDB('./invoices.json')

dbAddresses.truncate()  # drop all address data before we start.
dbLineItems.truncate() 
# dbInvoices.truncate()


User = Query()    # type: TinyDB.queries.Query

Items = []
with open('./things.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        Items.append(row)

PerItem = []
with open('./peritem.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        PerItem.append(row)



class Company():
    def __init__(self):
        self.uniqueID = ''
        self.Name = ''
        self.Addr_1 = ''
        self.Addr_2 = ''
        self. City =' ' 
        self.State = ''
        self. Zip = ''



fake = Faker()
Faker.seed(0)
for _ in range (100):
    # address = fake.address()
    # print(address)
    uniqueID = fake.bothify(text='????-######', letters='ACDEFGHIJKLMNOPQRSQSTeUVWXYZ')
   #  print(uniqueID)
    CompanyName = fake.company()
    # print (CompanyName)
    Attn = "Attn: " + fake.name()
    # print(Attn)
    Address = fake.street_address()
    # print(Address)
    City = fake.city()
    State = fake.state()
    Zip = fake.postcode()
    # print (City + " " + State + ", " + Zip)
    dbAddresses.insert({'uniqueID': uniqueID,\
        "Name": CompanyName,\
            "Addr_1":Attn,\
                "Address":Address,\
                     "City":City,\
                         "State":State,\
                             "Zip":Zip})

# dbSize = len(dbAddresses)
# print("Size of tinydb_addresses.json is: " + dbSize + " rows.")

for _ in range (200):
    LIID = fake.bothify(text='??????-###', letters='ACDEFGHIJKLMNOPQRSQSTeUVWXYZ')
    LIQty = random.randint(1,10)
    LIPerItem = random.choice(PerItem)
    LIPPI = (random.randint(100, 10000))/100
    LIName = random.choice(Items)
    LITotal = LIQty * LIPPI
    dbLineItems.insert({'Item ID':LIID,\
        'Quantity':LIQty,\
            'Per Item':LIPerItem,\
                'Price per Item':LIPPI,\
                    'Item':LIName,\
                        'Total':LITotal})
