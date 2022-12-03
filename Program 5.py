##########################################################################
# Computer Science Program 5
# December 1,2022
# Franklin Jeffries
# Professors name
###########################################################################
from datetime import date
#class is titled House
class House:
    def __init__(self,year_built, price, value_now = 0,location=None):
        self.year_built = year_built
        self.price = price
        self.current_year = current_year
        self.location = location
    def value_now(self):
        value_now = self.price (1+0.08)*(self.current_year - self.year_built)
        return int(value_now)
    def cash_made(self):
        cash_made = self.value_now() - self.price
        return cash_made
    #This section is made up of the menu for the app that will be displayed. 
    def __str__(self):
        print('---------------------------')

        print('House Information:  ')
        print('\t Year Built:  ',self.year_built)
        print('\t Purchase price:  ',self.price)
        print('\t Current Value of House:  ',self.value_now())
        print('\t Location:  ',self.location)

        print('---------------------------')

        print('\n------------------------------------------------------')
        print('Total value youw will earn :',self.cash_made())
        print()
        print('------------------------------------------------------')

        pass
    def main(self):
        self.__str__()




print('Welcome to our house calculation app')

x = True
while x:
    house_model_year - int(input("Enter House model year: "))
    if house_model_year > 0 and house_model_year <date.today().year:
        x = False
    else:
        print("Enter Valid year")


y = True
while y:
    price = int(input('price of the house: '))
    if price > 0:
        y = False
    else:
        print("Enter Valid price")

z = True
while z:
    current_year = int(input("Enter the current year :"))
    if current_year == date.today().year:
        z = False
    else:
        print("Enter the correct current year")
house_location = input("Enter your house location: ")


obj = House(house_model_year,price,current_year,house_location)
obj.main()