class SchoolBus:

    def __init__(self, color):
        self._color = color
    
    def welcome_student(self, student_name):
        print(f"hello {student_name}, how are you today?")
    
bus = SchoolBus('blue')
SchoolBus.welcome_student(bus, 'Amy')

my_bus = SchoolBus('yellow')
my_bus.welcome_student('Molly')

#to make a method non-public
#you need to add a leading underscore
# def _display_data:
# def __display_data: this is name mangling