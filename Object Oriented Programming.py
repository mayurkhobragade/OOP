#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming

# In[7]:


class Atm:
    
    #constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input(""" 
        Hi How Can I help you?
        1. Press 1 to create Pin
        2. Press 2 to change Pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
         """)
        
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
    def create_pin(self):
        user_pin = input("Enter your Pin")
        self.pin = user_pin
        
        user_balance = int(input('enter balance'))
        self.balance = user_balance
        
        print("Pin created Successfully")
        self.menu()
        
    def change_pin(self):
        old_pin = input('enter old pin')
        if old_pin == self.pin:
            #change pin
            new_pin = input('enter new pin')
            self.pin = new_pin
            print('pin change successfully')
            self.menu()
        else:
            print("no change")
            self.menu()
        
    def check_balance(self):
        user_pin = input('enter the pin')
        if user_pin == self.pin:
            print('Your balance is', self.balance)
        else:
            print('Sorry, incorrect credentials')
        self.menu()
            
    def withdraw(self):
        user_pin = input('enter the pin')
        if user_pin == self.pin:
            amount = int(input('enter the amount'))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdrawl Successfull. Balance is", self.balance)
            else:
                print('enter the right amount')       
        else:
            print('Password is incorrect')
        self.menu()
        
        


# In[ ]:


obj = Atm()


# In[ ]:




