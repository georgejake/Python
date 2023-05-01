import numpy as np

#1D Arrays & 2D Arrays/1D arrays are also called "list" one of the 4 collection data types in Python
"""
2D array a2 = np.array([ [1,2,3],[4,5,6],[6,7,8] ]) looks like
|   1   2   3   |
|   4   5   6   |
|   6   7   8   |
a2[1] ==> First row
ndim ==> returns number of dimensions of array e.g for a2 it will be 2
print size of each item(a2.itemsize) in array and type(a2.dtype)
a3.size ==> this prints number of elements ,for 2D the array is flattened and size is printed
a2.shape ==> prints (rows,columns) as a tuple
c1 = np.array([[5, 0], [1, 0], [10, 0]], dtype=complex) ==> for getting complex arrays
"""
a1 = np.array([1,2,3])
print(a1[2])
a2 = np.array([ [1,2,3],[4,5,6],[6,7,8] ])
print(a2[1])
print(a2.ndim)
print(a2.itemsize,a2.dtype)
a3= np.array([ [1,2,3],[4,5,6] ],dtype=float)
print(a3.itemsize,a3.dtype)
print(a3.size)
print(a2.shape,a3.shape)
c1 = np.array([[5, 0], [1, 0], [10, 0]], dtype=complex)
print(c1)

#Init array with zeros and ones
"""
Make sure we are using double brackets
"""
b1 = np.zeros((3,3))
print(b1)
b2 = np.ones((3,3))
print(b2)
#Range function ,this is used to create lists/1D Arrays
"""
#d[4] is not there
Using reshape along with arange ,we can create 2D arrays also
d = range(1,5) ==> Sequence starting from 1 till 4, index position is from 0 to 3
"""
d = range(1,5)
print(d[0],d[1],d[2],d[3])
d1 = np.arange(start=1,stop=10,step=1)
print(d1)
d2 = np.arange(0,10,1).reshape((5,2))
print(d2)
#Linespace
"""
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
num=number of samples to generate between start and stop, by default it is 50
"""
d3 = np.linspace(start=1, stop=5, num=10)
print(d3)
# Reshaping array
"""
Reshaping is not Transpose, the way it does can be understood by referring below link
https://mxnet.apache.org/versions/1.5.0/tutorials/basic/reshape_transpose.html
"""
d4 = np.array([[1, 2], [3, 2], [4, 2]])
print(d4.shape)
print(d4.reshape(2, 3))
#Ravel function
"""
Ravel function just converts a 2D array to 1D array ,it just flattens
"""
print(d4.ravel())
# Math functions
"""
axis=0 column wise
axis=1 row wise
Numpy array also support all kinds of matrix addition + subtraction, rs.dot(rs1) etc
"""
print("Math functions")
print(d4.min(), d4.max(), d4.sum(), d4.sum(axis=0), d4.sum(axis=1), np.sqrt(d4))
d5 = np.array([[1, 2], [3, 4], [5, 6]])
print(d4 + d5)