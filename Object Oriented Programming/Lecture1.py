'''
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which encapsulate data and behavior. In Python, everything is an object, and Python supports OOP principles such as encapsulation, inheritance, and polymorphism.

'''

# CLASSES & OBJECTS:

    # 1. Creating Class:

class Dog:
    # Class attribute:
        
        # also known as a class property, is a property that is shared by all instances (objects) of a class. It belongs to the class itself rather than any specific instance of the class. Class attributes are defined within the class and are accessible to all instances of that class.

        # Shared among Instances: Class attributes are shared by all instances of the class. Changes to the class attribute affect all instances.

        # Defined Outside Methods: Class attributes are typically defined outside any methods within the class.

        # Accessing Class Attributes: You can access class attributes using the class name or through an instance of the class.

    species = "Canis familiaris"


# Creating instances/OBJECTS of the Dog class
dog1 = Dog()
dog2 = Dog()

# Accessing class attribute
print(dog1.species)  # Outputs: Canis familiaris
print(dog2.species)  # Outputs: Canis familiaris



Dog.species = "Canis lupus"  # Modifying the class attribute
print(dog1.species)  # Outputs: Canis lupus
print(dog2.species)  # Outputs: Canis lupus



dog1.species = "hello"

'''
When you modify the class attribute using Dog.species = "Canis lupus", it only affects instances that don't have their own instance attribute with the same name. Since dog1 has its own species instance attribute, it retains the value "hello," while dog2 reflects the modified class attribute with the value "Canis lupus."

'''
Dog.species = "Canis lupus"  # Modifying the class attribute
print(dog1.species)  # Outputs: hello
print(dog2.species)  # Outputs: Canis lupus

