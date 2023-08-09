#!/usr/bin/env python
# coding: utf-8

# In[6]:


Normal = 140
Recliner = 10
Nprice = 270
Rprice = 430
Combo = 200


while True:
    Name = input("Enter Name: ")
    Amount = 0
    
    print("""prices:
Normal seat : 270/seat
Recliner seat : 430/seat""")
    
    print("""
Press 1 for Normal
Press 2 for Recliner""")
    
    Choice = int(input("Enter your choice between 1 or 2: "))
    Seats = int(input("Enter number of seats: "))
    
    if Choice == 1:
        Normal -= Seats
        if Normal <= 0:
            print("Housefull")
            break
        else:
            Amount += (Seats*Nprice)
            #print(amount)
            print(Normal)
            
        
    
    elif Choice == 2:
        Recliner -= Seats
        if Recliner <= 0:
            print("Housefull")
            break
        else:
            Amount += (Seats*Rprice)
            #print(amount)
            print(Recliner)
            
        
        
    Item= input("You need combo?(yes\no):")
    if Item == "yes":
        Amount+=Combo


    print("-"*40)
    print("Enter Name:", Name)
    print("Paybal Amount:", Amount)
    print("")
    print("-"*40)



    Repeat = input("Next person?")
    if Repeat == "no":
        break
        
       


# In[ ]:




