# numpy array creation functions
import numpy as np
a =[1,3,2,4,5,6,7,8,9]
print(np.array(a))

# creating a 2D array
list1= [1,2,3,4]
list2 = [5,6,7,8]
list3 = [9,10,11,12]
sampleArray= np.array([list1,list2,list3]   )
print(sampleArray)
# shape of the array
print(sampleArray.shape)


# 3d arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#  indexing
arr = np.array([1, 2, 3, 4])

print(arr[0])

print(arr[1])

print(arr[2] + arr[3])

#  numopy array slicing 

print("slicing of  numpy array")
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[4:])

print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])

print(" copy of the array")

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42



print(arr)
print(x)

print(" view of  the array")
x = arr.view()
arr[0] = 42

print(arr)
print(x)


x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

#  numpy array Shape 

print(" reshaping arrays -> chaging shape of an array")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
print( "1d to 3d ")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

print("lattening the arrays Flattening array means converting a multidimensional array into a 1d arr We can use reshape(-1) to do this.")

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

# iterating arrays -->usefor  loop 
print(" numpy array joining ")

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
print(" splittingnumpy array ")


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

print(" Seaching Arrays ")

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

print("Filtering Arrays")

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)





















