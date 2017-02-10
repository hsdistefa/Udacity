import math
import operator

# optimize the function f(x)=(x mod 6)^2 mod 7 - sin(x)
# for integers x in {1,..,100}
print(max( {i:(i % 6)**2 % 7 - math.sin(i) for i in range(1, 101)}.iteritems(),
            key=operator.itemgetter(1))[0])

# optimize the function f(x)= -x^4 + 1000x^3 - 20x^2 + 4x - 6
# for all rational numbers
# f'(x) = -4x^3 + 3000x^2 - 40x + 4
# use newton's method to compute max(x) where f'(x)=0
# or just graph and estimate ~750
