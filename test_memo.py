import time
import memoization
import pytest
from itertools import combinations_with_replacement

x = 1000

@pytest.mark.function
def test_resolver():
    # to check uniqueness of resolver

    list1 = list(range(0, 11))
    resolver_result = []
    com = combinations_with_replacement(list1, 3)
    for y, m, d in list(com):
        result = memoization.resolver(y, m, d)
        if result not in resolver_result:
            resolver_result.append(result)
        elif result in resolver_result:
            print(y, m, d, memoization.resolver(y, m, d))
        else:
            print(memoization.resolver(y, m, d))


@pytest.mark.function
def test_memoize():
    result1 = memoization.memoize(memoization.add_to_time, 0, 1, 00, x)
    # time.sleep()
    result2 = memoization.memoize(memoization.add_to_time, 0, 1, 00, x)
    assert result1 == result2

@pytest.mark.time
def test_run_time():
    t1= int(round(time.time() * 1000))
    result1 = memoization.memoize(memoization.add_to_time, 0, 1, 00, x)
    t2 = int(round(time.time() * 1000))
    print("the function was executed in {} ms by running the function".format(t2-t1))

    t1 = int(round(time.time() * 1000))
    result1 = memoization.memoize(memoization.add_to_time, 0, 1, 00, x)
    t2 = int(round(time.time() * 1000))
    print("the function was executed in {} ms by returning  from memory ".format(t2 - t1))

@pytest.mark.time
def test_cached_time():
    result1 = memoization.memoize(memoization.add_to_time, 0, 1, 00, x)
    t1 = int(round(time.time() * 1000))

    while (memoization.memoize(memoization.add_to_time, 0, 1, 00, x)) == result1:
        t2 = int(round(time.time() * 1000))

    print('..value was stored for {} ms in memory'.format(t2 - t1))


@pytest.mark.time
def test_updated_value():
    result1 = memoization.memoize(memoization.add_to_time, 0, 1, 00, x)
    t1 = int(round(time.time() * 1000))

    while True:
        if (memoization.memoize(memoization.add_to_time, 0, 1, 00, x)) > result1:
            t2 = int(round(time.time() * 1000))
            break
    print('..value updated as previous was stored for {} ms in memory'.format(t2 - t1))



@pytest.mark.time
def test_time_clock():
    assert memoization.time_now() == int(round(time.time() * 1000))

