def do_four(f):
    f()
    f()
    f()
    f()
def print_type1():
    print('+','-','-','-','-','+','-','-','-','-','+')
def print_type2():
    string1 = ('|'+' '*9)*2+'|'
    print(string1)

def ex3_2():
    print_type1()
    do_four(print_type2)
    print_type1()
    do_four(print_type2)
    print_type1()
ex3_2()
