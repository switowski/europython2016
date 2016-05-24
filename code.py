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
people = {
    'john': {
        'first': 'John',
        'last': 'Doe'
    }
}

if 'john' in people and 'last' in people['john']:
    fullname = people['john']
else:
    fullname = ''


try:
    fullname = people['john']['last']
except KeyError:
    fullname = ''

fullname = people.get('john', {}).get('last', '')


######### Calling a function 1000 times vs running operation 1000 times in a function ##########
def square(number):
    return number**2
squares = [square(i) for i in range(1000000)]


def compute_squares():
    return [i**2 for i in range(1000000)]

################################# Def vs lambda ##############################
def name_d(person):
    return person.get('name')

name_l = lambda person: person.get('name')


MILLION_NUMBERS = range(1,1000001)

output = []
for element in MILLION_NUMBERS:
    if element % 2:
        output.append(element)

filter(lambda x: x % 2, MILLION_NUMBERS)
