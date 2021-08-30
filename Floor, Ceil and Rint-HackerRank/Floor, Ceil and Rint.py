"""
    https://www.hackerrank.com/challenges/floor-ceil-and-rint/
        HACKERRANK
    Practice > Python > Numpy > Floor, Ceil and Rint

------------------Floor, Ceil and Rint---------------------

floor

The tool floor returns the floor of the input element-wise.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

ceil

The tool ceil returns the ceiling of the input element-wise.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]

rint

The rint tool rounds to the nearest integer of input element-wise.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

Sample Input

1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9


Sample Output

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

"""

import numpy
numpy.set_printoptions(legacy = '1.13')
a = numpy.array(list(map(float, input().split())))

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
