# a basic program to show memoizaton using python3.7 with time out


import time

memory = {}


# to get the time in ms
def time_now():
    return int(round(time.time() * 1000))

# caching
def memoize(fun, year, month, day, timeout):
    # unique address to save the value i.e resolver
    key = int(str(year) + str(month) + str(day))

    if key in memory:
        if time_now() <= memory[key]['time']:
            print('memory')
            return memory[key]['value']

    result = fun(year, month, day)
    memory.update({key: {'time': (time_now() + timeout), 'value': result}})
    return result


# some function taking arguments and returning data..
def add_to_time(year, month, day):
    totaldays = (((year * 365) + (month * 31) + day) * 86400000) + time_now()
    print('from function')
    return totaldays


if __name__ == "__main__":
    print(memoize(add_to_time, 0, 1, 00, 5000))
    time.sleep(5)
    print(memoize(add_to_time, 0, 1, 00, 5000))
    time.sleep(0)

