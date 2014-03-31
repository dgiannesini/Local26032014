# Add after commit 01042014c1

# Assignment 2 for ITC 415

# Car class to create 3 car object: Toyota Kruger, Nissan Patrol, and Ford Territory

class Car():

   def __init__(self, name):
      self.name=name
      self.sale_price = float(input("What is the Selling price of the " + name + " :"))
      self.unit_sold = int(input("How many " + name + " have been sold: "))
      self.partial_income = 0.0
      self.partial_income = self.sale_price * self.unit_sold

def Global_Income(Cars):

   global_Income = 0.0
   for key in Cars:
      global_Income += Cars[key].partial_income

   return global_Income

def Display_Partial_Income(Cars, listOfCars):
   for key in listOfCars:
      print("The income for the ",key," is $",format(Cars[key].partial_income,',.2f'),".",sep='')

def Global_Bonus(income):
   bonus = 0.0

   if income <= 500000:
      return income * 0.001
   elif income <= 1000000:
      return 500 + (income-500000) * 0.002
   elif income <= 5000000:
      return 1500 + (income-1500000) * 0.003
   elif income <= 10000000:
      return 13500 + (income-5000000) * 0.004
   else:
      return 33500 + (income-10000000) * 0.005
   
def Partial_Bonus(Cars, global_bonus, global_income, listOfCars):
   for key in listOfCars:
      print ("Bonus for ",key," is $",format((Cars[key].partial_income / global_income) * global_bonus,',.2f'),sep='')

   
def main ():
   print("ok")
# Declare a 'Cars' dictionary for car. This dictionnary stores car maker for keys and
# Car objects as values.
   global_income = 0.0
   global_bonus = 0.0
   cars_dictionnary={}
   list_of_cars=("Toyota Kruger","Nissan Patrol","Ford Territory")

# This loop creates a car object for each item in listOfCars.
# It assigns the object name and prompt user for sale price and number of units sold
# Partial income is calculated at creation time as well
   for item in list_of_cars:
      cars_dictionnary[item]=Car(item)
   
# call function to display partial incomes
   Display_Partial_Income(cars_dictionnary, list_of_cars)
   
# call function to calculate global and partial sales

   global_income = Global_Income(cars_dictionnary)
   print("The global income for the ABC shop is $",format(global_income,',.2f'),sep='')

# call function to calculate global bonus
   global_bonus = Global_Bonus(global_income)
   print("The Global bonus for ABC shop is $",format(global_bonus,',.2f'),sep='')

# call function to calculate partial bonus
   Partial_Bonus(cars_dictionnary, global_bonus, global_income, list_of_cars)


main()
