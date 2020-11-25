import time
import memoization


print(memoization.memoize(memoization.add_to_time, 0, 1, 00, 5000))
memoization.incrimenttime(5001)
print(memoization.memoize(memoization.add_to_time, 0, 1, 00, 5000))
