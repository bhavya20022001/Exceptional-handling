#specific exception handling with custom messages
a=5
b=0
try:
    print("resources are opened!")    
    print(a/b) # NOTE! if this line is causing error so next line won't be executed within the try block
    x=int(input("enter a number :"))
    print(x)
except ValueError as e:
    print("ValueError occured!")
except ZeroDivisionError as e:
    print("You can't divide a number by Zero!")

except Exception as e:
    print("oh no!",e.__class__,"occured")

# always runs whether exception occurs or not! use this to close your file    
finally:
    print("resources are closed")