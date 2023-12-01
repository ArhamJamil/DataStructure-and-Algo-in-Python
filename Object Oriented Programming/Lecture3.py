# Defining a class named Myclass
class Myclass:
    def __init__(self):
        # Public variable, accessible from outside the class
        self.PublicVariable = "arham"

        # Protected variable, conventionally considered internal to the class
        # Accessible from outside, but using it directly is discouraged
        self._ProtectedVariable = 18

        # Private variable, name-mangled to _Myclass__PrivateVariable
        '''
        In Python, variables with a double underscore (__) prefix undergo a process called name mangling. Name mangling is a mechanism used to make it harder to accidentally override private attributes in subclasses. When you define a variable like __PrivateVariable, Python internally renames it to _ClassName__PrivateVariable, where ClassName is the name of the class in which the variable is defined.

        For example, in your case, the private variable __PrivateVariable in the Myclass class would be transformed to _Myclass__PrivateVariable behind the scenes.

        So, when you try to access obj.__PrivateVariable directly, you are using the incorrect name after name mangling has occurred. This will result in an AttributeError because Python cannot find an attribute with the name __PrivateVariable.
        '''
        # Should be accessed using the provided method getPrivate()
        self.__PrivateVariable = "MUHAMMAD"

    # Method to get the value of the protected variable
    def getProtected(self):
        return self._ProtectedVariable

    # Method to get the value of the private variable
    def getPrivate(self):
        return self.__PrivateVariable

# Creating an instance of the class
obj = Myclass()

# Accessing the public variable directly
print(obj.PublicVariable)

# Accessing the protected variable directly (discouraged, but possible)
print(obj._ProtectedVariable)

# Attempting to access the private variable directly will result in an AttributeError
# print(obj.__PrivateVariable)  # Uncommenting this line will raise an AttributeError

# Accessing the private variable using the provided method getPrivate()
print(obj.getPrivate())
