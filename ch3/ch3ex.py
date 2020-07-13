# exercise 3.1
def right_justify(Astring):
    multi_space=' '*(70-len(Astring))
    Astring_justified = multi_space + Astring
    print(Astring_justified)
right_justify('monty')

#exercise 3.2
#(1)
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
do_twice(print_spam)
#(2)
def do_twice_2(f,arg):
    f(arg)
    f(arg)
do_twice_2(right_justify,'spam')
#(3)
def printtwice(AniArgs):
    print(AniArgs)
    print(AniArgs)
#(4)    
do_twice_2(printtwice,'spam')
#(5)
def do_four(f,arg):
    do_twice_2(f,arg)
    do_twice_2(f,arg)
do_four(right_justify,'Ahhaha')
