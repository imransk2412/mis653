# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:27:49 2024

@author: skimr
"""

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
 
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"Mileage: {self.mileage} miles")
 
    def drive(self, miles):
        self.mileage += miles
        print(f"Driving {miles} miles. New mileage: {self.mileage} miles")
my_car = Car("Toyota", "Corolla", 2020, 15000.5)
my_car.display_info()
my_car.drive(200)
my_car.display_info()
