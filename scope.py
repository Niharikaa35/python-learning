
# Global scope and Global Variable
fname="niharika"
print("before  the function",fname)

def globalScopeEx():
    print("inside the function",fname)

globalScopeEx()

print("after  the function",fname)

# Local  scope and Local Variable
def localScope():
    lname="G.niharika"
    print("My name is", lname)
localScope()


fname="Global"
def MyFun():
    fname="Local"
    print(fname)
MyFun()
print(fname)



fname="hero"
def MyFun():
    fname="zero"
MyFun()
print(fname)


fname="hero"
def MyFun():
    global fname
    fname="zero"
MyFun()
print(fname)


# nested function
def outerfunction():
        # Enclosing scope
        print("this is outer function")
        def innerfunction():
         print("this is inner function")

         
outerfunction()


# nested function calling the child function
def outerfunction():
        print("this is outer function")
        def innerfunction():
         print("this is inner function")

        innerfunction()    
outerfunction()


# Enclosing function
def outerfunction():
        print("this is outer function")
        # Enclosing variable
        myname="niharika"
        def innerfunction():
         myname="niha"
         print("this is inner function" ,myname)

        innerfunction()    
outerfunction()


def outerfunction():
        myname="hero"
        print("this is outer function")
        # Enclosing variable
        myname="zero"
        def innerfunction():
         nonlocal myname
         myname="niha"
         print("this is inner function" ,myname)

        innerfunction()    
outerfunction()


fname="hero"
def outerfunction():
       
        print("this is outer function")
        # Enclosing variable
        global fname
        myname="zero"
        def innerfunction():
         nonlocal myname
         myname="niha"
         print("this is inner function" ,myname)

        innerfunction()    
outerfunction()

a="niharika"
print(len(a))

myname="global"
def outer():
    myname="enclosing"
    def inner():
        myname="local"
        print(myname)
    inner()
outer()

def outer():
    def inner():
        a="niharika"
        print(len(a))
        inner()
    outer()  

gvar="global"
def outer():
    evar="enclosing"
    def inner():
        lvar="local" 
        print(gvar)
        print(evar)
        print(lvar)
        inner()
    outer()



def myfun():
    return "hero"
    print("hii")

print(myfun())