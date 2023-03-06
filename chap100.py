# aggregation
# concept in OOP that describes the relationship between 2 or more classes
# build complex objects that are composed of other objects

# class A and class B
# class B has all the functionalities of class A
# we store instances of the simpler objects in the more complex objects
# 'has a' relationship between the classes
# an object of class B has an object of class A

# example
# employee and vehicle
# an employee has a vehicle
# store the info of vehicle inside of employee
# employee class, vehicle class
# vehicle inside of employee class

class Vehicle:
    
    def __init__(self, color, license_plate, is_electric):
        self.color = color
        self.license_plate = license_plate
        self.is_electric = is_electric
    
    def show_license_plate(self):
        print(self.license_plate)
    
    def show_info(self):
        print('my vehicle:')
        print(f'color: {self.color}')
        print(f'license plate: {self.license_plate}')
        print(f'electric: {self.is_electric}')


class Employee:

    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle
    
    def show_vehicle_info(self):
        self.vehicle.show_info()


gina_vehicle = Vehicle('black', 'XYZ 123', is_electric=False) #to make is extra explicit than False
employee_1 = Employee('Gina', gina_vehicle)

print(employee_1)
print(employee_1.name)
print(employee_1.vehicle) # return the vehcile instance
employee_1.show_vehicle_info()

print(gina_vehicle.color)
print(gina_vehicle.license_plate)

print(employee_1.vehicle.color)
print(employee_1.vehicle.license_plate)

print(employee_1.show_vehicle_info())