def hello(greet,name):
    print(f"{greet} {name}")

hello("Hello","Adan")
hello("Ciao","Adan")

def big_function(*args,**kwargs):
    print(args)
    print(kwargs)
big_function(1,2,3,4,5,name="Adan",age=47)