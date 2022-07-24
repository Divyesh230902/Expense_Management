from flask import *
class Save_expense:
    # logic to save expense
    def __init__(self, salary):
        self.salary = salary
        self.save = 0
    def dft_save_expense(self):
        if self.salary in range(100, 1000):
            self.save = self.salary * 0.06
            return self.save
        elif self.salary in range(1000, 10000):
            self.save = self.salary * 0.08
            return self.save
        elif self.salary in range(10000, 100000):
            self.save = self.salary * 0.1
            return self.save
        elif self.salary in range(100000, 1000000):
            self.save = self.salary * 0.12
            return self.save
        elif self.salary in range(1000000, 10000000):
            self.save = self.salary * 0.14
            return self.save
        elif self.salary in range(10000000, 100000000):
            self.save = self.salary * 0.16
            return self.save
        elif self.salary in range(100000000, 1000000000):
            self.save = self.salary * 0.18
            return self.save
        elif self.salary in range(1000000000, 10000000000):
            self.save = self.salary * 0.2
            return self.save
        else:
            self.save = self.salary * 0.25
            return self.save
    def cust_save_expense(self,percentage):
        self.save = self.salary * percentage
        return self.save

class manage_expense(Save_expense):
    # logic to manage expense
    def __init__(self, salary):
        super().__init__(salary, self.save)
        self.save
        self.salary = salary
        self.net = self.salary - self.save
    def make_budget(self):
        self.budget = self.net/28
        return self.budget, self.net
    def bucket(self):
        # check if budget is less than or equal to net
        if self.budget <= self.net:
            # user will input item and amount which will be added to dictionary named basket
            while True:
                choice = input("[1] Add item to basket\n[2] Checkout\n[3] Exit\nEnter: ")
                self.basket = {'item': [], 'amount': []}
                if choice == "1":
                    # as the amount is entered it should be reduced from net
                    self.item = input('Enter item: ')
                    self.amount = int(input('Enter amount: '))
                    self.basket['item'].append(self.item)
                    self.basket['amount'].append(self.amount)
                    self.net = self.net - self.amount
                elif choice == "2":
                    print("Your total is: ", self.net)
                    print("Your budget is: ", self.budget)
                    print("Your save is: ", self.save)
                    print("Your basket is: ", self.basket)
                    break
                elif choice == "3":
                    print("Thank you for using the program")
                    break
                else:
                    print("Invalid input")
                    continue

# print("Welcome to the expense management program")
# while True:
#     # user will enter salary
#     salary = int(input("Enter your salary: "))
#     # user will enter if they want to use default saving or custom saving
#     choice = input("[1] Default saving\n[2] Custom saving\nEnter: ")
#     if choice == "1":
#         # if user wants to use default saving then it will be calculated and saved in save variable
#         save = Save_expense(salary).dft_save_expense()
#         # user will be asked to make budget
#         budget = manage_expense(salary).make_budget()
#         # user will be asked to add item to basket
#         manage_expense(salary).bucket()
#     elif choice == "2":
#         # if user wants to use custom saving then it will be calculated and saved in save variable
#         # user will enter percentage of saving
#         percentage = float(input("Enter your percentage of saving: "))
#         save = Save_expense(salary).cust_save_expense(percentage/100)
#         # user will be asked to make budget
#         budget = manage_expense(salary).make_budget()
#         # user will be asked to add item to basket
#         manage_expense(salary).bucket()
#     else:
#         print("Invalid input")
#         continue
#     # user will be asked to continue or exit
#     choice = input("[1] Continue\n[2] Exit\nEnter: ")
#     if choice == "1":
#         continue
#     elif choice == "2":
#         print("Thank you for using the program")
#         break
#     else:
#         print("Invalid input")
#         continue
