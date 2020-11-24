# a basic program to show memoizaton using python3.7

import time
memory = {}

def timenow():
    return int(round(time.time() * 1000))

# some function taking arguments and returning data..
def addToTime(year,month,day):
    totalday = ((year*365) + (month*31) + (day))*86400000
    print('from function')
    return totalday


def memoize(year,month,day):
    key = year+month+day

    if (key in memory):
        if ((timenow() - memory[key]['time']) <= 5000):
            print('memory')
            return memory[key]['value']

    else:
        result = addToTime(year, month, day)
        memory.update({key:{'time': timenow(), 'value':result}})
        return result








print(memoize(1, 1, 30))
time.sleep(5)

print(memoize(1, 1, 30))