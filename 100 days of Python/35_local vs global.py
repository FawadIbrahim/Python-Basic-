f=10
print(f"This is a global {f} Variable.")
def my_function():
    g=5
    print(f"This is local {g} Variable")
print(f"This is also a global {f} Variable.")    
my_function()    
print(f"This is also a global {f} Variable.")