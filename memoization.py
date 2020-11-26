# a basic program to show memoizaton using python3.7 with time out


import time

memory = {}


# to get the time in ms
def time_now():
    return int(round(time.time() * 1000))


# caching
def memoize(fun, year, month, day, timeout):
    # unique address to save the value i.e resolver
    key = resolver(year,month,day)

    if key in memory:
        if time_now() <= memory[key]['time']:
            #print('memory')
            #time.sleep(3)
            return memory[key]['value']

    result = fun(year, month, day)
    memory.update({key: {'time': (time_now() + timeout), 'value': result}})
    return result


def resolver(year, month, day):
    return (hex(year) + hex(month) + hex(day))


# some function taking arguments and returning data..
def add_to_time(year, month, day):
    totaldays = (((year * 365) + (month * 31) + day) * 86400000) + time_now()
    #print('from function')
    #time.sleep(7)
    return totaldays


if __name__ == "__main__":


    print(memoize(add_to_time, 0, 1, 00, 5000))
    print(memoize(add_to_time, 0, 1, 00, 5000))
    time.sleep(5)
    print(memoize(add_to_time, 0, 1, 00, 5000))


