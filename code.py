import math

def sin_slow(deg):
    factor = math.pi/180.0
    return math.sin(deg * factor)

def sin_fast(deg, factor=math.pi/180.0):
    return math.sin(deg * factor)


################## Ask for forgiveness vs permissions ########################
class Foo(object):
    hello = 'world'

class Bar(object):
    pass

# Version with attribute existing
def permissions():
    foo = Foo()
    if hasattr(foo, 'hello'):
        foo.hello

def forgiveness():
    foo = Foo()
    try:
        foo.hello
    except:
        pass

# Version with attribute not existing
def permissions():
    bar = Bar()
    if hasattr(bar, 'hello'):
        bar.hello

def forgiveness():
    bar = Bar()
    try:
        bar.hello
    except AttributeError:
        pass

################# Dictionary ask for permission/forgiveness ##################
people = {'john': 'John Doe',
          'tim': 'Tim Doe'}

if 'john' in people:
    fullname = people['john']
else:
    fullname = ''


try:
    fullname = people['john']
except KeyError:
    fullname = ''

######### Calling a function 1000 times vs running operation 1000 times in a function ##########
def square(number):
    return number**2
squares = [square(i) for i in range(1000000)]


def compute_squares():
    return [i**2 for i in range(1000000)]