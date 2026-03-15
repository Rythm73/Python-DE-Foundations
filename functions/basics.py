"""function with no parameters and arguments"""
def greet_me():
    return "Hello,there....! Good Morning"
print(greet_me())

''' Multiple ways for a Personalization in this Function.'''
''' 1)String Way'''
def string_greet(name):
    return "Hello,"+name+"! How are you?"
print(string_greet("Dinaya"))

'''2)Format Way'''
def format_greet(name):
    return "Welcome to the team,{}!" .format(name)
print(format_greet("lachlyn"))

'''3)Multiple Parameters'''
def mparameter_greet(time_of_day,name):
    return f"Good{time_of_day},{name}!Have a great day."
print(mparameter_greet("morning","Nina"))

def user_greet():
    user_name=input("Name:")
    return f"it's good to see you,{user_name}"
print(user_greet())
