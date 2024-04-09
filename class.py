#Create a python class named person,with the following attributes.
class person:
    def __init__(self, name, age, gender):
        #initialize attributes.
        self.name = name
        self.age = age
        self.gender = gender
        #Implement a method called introduce
    def introduce (self):
        print(f"Hello, my name is {self.name}.I am {self.age} years old and I am {self.gender}.")
        #create an instance of the person class
person1 = person("Daniel", 22, "male")

# Call the introduce method to display the person's information
person1.introduce()








