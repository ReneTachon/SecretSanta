# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:41:58 2022

@author: rene.tachon
"""


import random
# List of people in the secret santa
GiftersList = ["Ren","Laur","Bev","louis","Gab","John","Max","Chris","Dad"]
# List of partners as a dictionary. We don't want to buy for our partners in the sectret santa
Partners = {"Ren":"Laur", "Bev":"louis", "John":"Gab", "Max":"Chris", "Dad":"x"}
RecipientsList = GiftersList.copy()

# Creates the reverse of the partners key value pairs in the dict and adds back into the dict
Partners_inv_map = {v: k for k, v in Partners.items()}
Partners.update(Partners_inv_map)

#Instantiate the "buys for" list
buyForDict = dict()

#Loop through the list and if the first entry in the shuffled list is not themselves or partner
# then assign them to the first entry and remove that enty from RecipientsList
for x in GiftersList:
    random.shuffle(RecipientsList)
    if (x != RecipientsList[0]) & (Partners[x] !=RecipientsList[0]) :
        buyForDict.update({x:RecipientsList[0]}) 
        RecipientsList.remove(RecipientsList[0])

#Print out who buys for who
for z in buyForDict:
    print(z, " buys for ", buyForDict[z])
           
           


        
    
    
    
    
    
    