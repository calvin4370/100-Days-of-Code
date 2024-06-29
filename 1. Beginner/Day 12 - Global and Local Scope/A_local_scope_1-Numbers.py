# Variables declared in the global scene are global variables
original = 1

# Reads the value of a parameter and returns it
def readvalue(variable):
    return variable

# NOTE Functions can take in global variables as parameters and access their value
print(readvalue(original))
#>>> 1

# Reads the value of a parameter, increases its value in the local scene, and returns the increased version
def valueup(variable):
    variable += 1
    return variable

# 
print(valueup(original))
#>>> 2

# NOTE how the function did not manage to change the value of the variable in the global scope
print(original)
#>>> 1