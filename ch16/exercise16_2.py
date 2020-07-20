from datetime import datetime ,date,timedelta

# get current date

def print_today():
    today = date.today()
    dstr = 'Today is {0}. Have a good time, sir!'.format(today.strftime("%Y-%m-%d, %A"))
    print(dstr)


def date_guardian(d):
    '''check if d belongs to datetime.date, if not try to convert it.
        Return a datetime.date object if it is successful.

    '''

    if type(d) is datetime.date:
        pass
    elif type(d) is str:
        try: 
            lt = d.split('-')
            dlt = []

            for ele in lt:
                dlt.append(ele.zfill(2))

            d = date.fromisoformat('-'.join(dlt) )
        except ValueError:
            print('Invalid date format!')
            return None
    else:
        print('Please provide a datetime.date object or a ISO format string!')
        return None
    return d


def age(d):
    '''takes a dateime.date object(instance) or a ISO 8601 string as one`s birthday,
       return the one`s age and the time period until birthday.'''
    #guardians
    d = date_guardian(d)
    d_today = date.today()
    
    delta = d_today - d
    age = delta.days // 365
    print(age)
    print('run here!')

def time2next_birthday(d):
    d_birth = date_guardian(d)
    d_now = datetime.now()

    d_birth = d_birth.replace(year=d_now.year)
    d_birth = datetime(d_birth.year, d_birth.month, d_birth.day,0,0,0)
    if d_birth < d_now:
        d_birth = d_birth.replace(year=d_birth.year + 1)

    delta = d_birth - d_now
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = (delta.seconds % 3600) % 60
    outstr = "Still {0} days, {1} hours, {2} minutes, {3} seconds until next birthday".format(delta.days,hours,minutes,seconds)
    print(outstr)

def ntimes_day(birth1,birth2,n):
    '''takes two datetime.date objects and an integer n, calculates the n times older day.'''
    birth1 , birth2 = date_guardian(birth1) , date_guardian(birth2)


    if birth1 > birth2:
        birth1,birth2 = birth2,birth1
    delta = birth2 - birth1

    date = birth2 + (n - 1) * delta
    return date



if __name__ == '__main__':
    print(ntimes_day('1998-1-1','1997-1-1',3))
