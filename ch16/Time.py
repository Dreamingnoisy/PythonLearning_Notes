class Time:
    """Represents the time of a day.
    attributes: hour, minute, second"""

def print_time(t):
    '''takes a Time object and prints the time'''
    print("%.2d:%.2d:%.2d"%(t.hour, t.minute, t.second))

def time2int(t):
    seconds = (t.hour*60 + t.minute) *60 + t.second
    return seconds

def int2time(seconds):
    t =Time()
    t.hour,t.minute,t.second= seconds // 3600, (seconds % 3600) // 60 ,(seconds % 3600) % 60
    return t

def is_after(t1,t2):
    '''takes two Time objects and 
       return True if t1 follows t2 chronologically
    '''

    time1 = time2int(t1)
    time2 = time2int(t2)

    return time1 > time2

def increment(t,seconds):
    '''takes a Time object and a number of seconds, 
       add the given number to the object.
    ''' 
    #modifier

    t_seconds = time2int(t)
    seconds = t_seconds + seconds
    t.hour,t.minute,t.second= seconds // 3600, (seconds % 3600) // 60 ,(seconds % 3600) % 60 



def p_increment(t,seconds):
    '''takes a Time object and a number of seconds, 
       add the given number to the object and returns
       a new Time object without modifying the input object
    ''' 
    #pure function

    t_seconds = time2int(t)
    seconds = t_seconds + seconds

    return int2time(seconds)

def main():
    t1 = Time()
    t1.hour, t1.minute, t1.second  = 11 , 59 , 30

    t2 = Time()
    t2.hour, t2.minute, t2.second  = 2 , 30 ,  0


    print_time(p_increment(t2,3661))

    increment(t2,3661)
    
    print_time(t2)

    
if __name__ == "__main__":
    main()
