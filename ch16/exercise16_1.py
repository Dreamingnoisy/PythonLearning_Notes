from Time import time2int, int2time,Time,print_time
def mul_time(t,fraction):
    seconds = time2int(t) * fraction
    return int2time(seconds)

def pace(finishing_time,distance):
    '''takes a finishing_time and a number that represents a distance,
    return a Time object representing the pace (time per mile)

    finishing_time :Time object
    distance : Positive number unit:mile
    '''
    pace = mul_time(finishing_time,1/distance)
    return pace




def main():
    t_test = Time()
    t_test.hour,t_test.minute,t_test.second = 10,30,47
    
    t_pace = Time()
    t_pace.hour,t_pace.minute,t_pace.second = 0,5,30

    print_time(pace(t_pace,0.3))

if __name__ == "__main__":
    main()
