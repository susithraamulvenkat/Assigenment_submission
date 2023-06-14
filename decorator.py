def decorator_func(*args):
    print("I am the decorator function")
    def inside_func(func):
        print("I am inside function")
        for i in args:
            if i=='Admin':
                func()
            else:
                print("Sorry,User cant able to access this ")
        
    return inside_func
@decorator_func('Admin','susithra')
def fun():
    print("Admin can access")
