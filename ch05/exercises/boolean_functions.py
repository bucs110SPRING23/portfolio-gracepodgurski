def foo(param1, param2):
    return param1 + param2
# foo(1) would be an error - needs both parameters


def bar(param1=4,param2=3): #default values aka named parameters 
    local_var = 5 #scope is limited to the function
    return param1 + param2 # Return ends the function 

# Default parameters not helpful when the two values need to be compared etc

def percentage_to_letter():
    
    return