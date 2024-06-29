enzyme_state = "unactivated"

def readstate(enzyme):
    return enzyme

print(readstate(enzyme_state))
#>>> unactivated

def activate(enzyme):
    enzyme = "activated"
    return enzyme

print(activate(enzyme_state))
#>>> activated

activate(enzyme_state)
print(enzyme_state)
#>>> unactivated