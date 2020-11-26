import time
import memoization
import pytest
from itertools import combinations_with_replacement

# to change the timeout value for all the test condition can also be changed individually
x = 1000

# to check uniqueness of resolver
@pytest.mark.function
def test_resolver():
    # to get all combinations of 3 parameter from 0 to 11
    list1 = list(range(0, 11))
    resolver_result = []
    com = combinations_with_replacement(list1, 3)
    for y, m, d in list(com):
        result = memoization.resolver(y, m, d)
        # check for same values
        if result not in resolver_result:
            resolver_result.append(result)
        elif result in resolver_result:
            print(y, m, d, memoization.resolver(y, m, d))
        else:
            print(y, m, d,memoization.resolver(y, m, d))

# to check if the values are same from function and memory
@pytest.mark.function
def test_memoize():
    result1 = memoization.memoize(memoization.add_to_time, 1, 1, 1, x)
    # time.sleep()
    result2 = memoization.memoize(memoization.add_to_time, 1, 1, 1, x)
    assert result1 == result2

# to check time required to return value from function and from memory.
@pytest.mark.time
def test_run_time():
    t1= int(round(time.time() * 1000))
    result1 = memoization.memoize(memoization.add_to_time, 1, 1, 00, x)
    t2 = int(round(time.time() * 1000))
    print("the function was executed in {} ms by running the function".format(t2-t1))

    t1 = int(round(time.time() * 1000))
    result1 = memoization.memoize(memoization.add_to_time, 1, 1, 00, x)
    t2 = int(round(time.time() * 1000))
    print("the function was executed in {} ms by returning  from memory ".format(t2 - t1))

# To calculate the total time  the value is saved in memory in ms
@pytest.mark.time
def test_cached_time():
    result1 = memoization.memoize(memoization.add_to_time, 0, 1, 10, x)
    t1 = int(round(time.time() * 1000))

    while (memoization.memoize(memoization.add_to_time, 0, 1, 10, x)) == result1:
        t2 = int(round(time.time() * 1000))
    print('..value was stored for {} ms in memory'.format(t2 - t1))

# To calculate the total time the value
@pytest.mark.time
def test_updated_value():
    result1 = memoization.memoize(memoization.add_to_time, 0, 1, 00, x)
    t1 = int(round(time.time() * 1000))

    while True:
        if (memoization.memoize(memoization.add_to_time, 0, 1, 00, x)) > result1:
            t2 = int(round(time.time() * 1000))
            break
    print('..value  should be updated if called  as it has to be stored for only {} ms in memory'.format(t2 - t1))


# To check for clock tamper
@pytest.mark.time
def test_time_clock():
    assert memoization.time_now() == int(round(time.time() * 1000))

