def deco(func):
    print("primer print deco")
    func()
    print("seundo print deco")


@deco    
def suma(a, b):
    return a + b

suma(2, 2)
    
    