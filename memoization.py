# a basic program to show memoization using python3.7 with time out

import time

# to store the given output with its time out value
memory = {}


# to get the time in ms
def time_now():
    return int(round(time.time() * 1000))


# caching
def memoize(fun, year, month, day, timeout):
    # unique address to save the value i.e resolver
    key = resolver(year, month, day)

    if key in memory:
        if time_now() <= memory[key]['time']:
            # print('memory')
            return memory[key]['value']

    result = fun(year, month, day)
    memory.update({key: {'time': (time_now() + timeout), 'value': result}})
    return result


# converting the arguments to a hexa value as address for the output function
def resolver(year, month, day):
    return (hex(year) + hex(month) + hex(day))


# some function taking arguments and returning data..(to take total millisecond in sum of year,month,day)
def add_to_time(year, month, day):
    totaldays = (((year * 365) + (month * 31) + day) * 86400000) + time_now()
    time.sleep(0.001)  # time to run this function
    return totaldays


if __name__ == "__main__":
    """"" test case to call the function with some argument and calling again to get from memory.
     and checking again after the time out """""

    print(memoize(add_to_time, 0, 1, 00, 5000))
    print(memoize(add_to_time, 0, 1, 00, 5000))
    time.sleep(5)
    print(memoize(add_to_time, 0, 1, 00, 5000))
