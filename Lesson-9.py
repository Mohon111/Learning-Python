#function advance
#1.
def test_function(num1, num2):
    print(num1, "-", num2)
test_function(5, 3)

#2.
def test_function(num1, num2 = 100):
    print(num1, "-", num2)
test_function(10)

#3.
def wishcard(name = "Mohon Basu", wish = "Happy Birthday To You "):
    print(wish + name)
wishcard("Jewel")


#4.
var = 10
def local():
    #var = var + 1
    # global  var
    # var = var + 1
    loc = var
    loc = loc + 1
    print(loc)
local()
def local1():
    print(var)
local1()