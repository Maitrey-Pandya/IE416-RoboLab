import numpy as np
# Generate 1D random array
arr1d=np.random.random((1,16))
print("The 1D array with 16 elements is : \n",arr1d,end="\n")
print("The shape of the array is : ",np.shape(arr1d))
print()
# Re-shape the array to 4x4 matrix
arr4x4=np.reshape(arr1d,(4,4))
print("The reshaped 4x4 matrix is : \n",arr4x4,end="\n")
print("The shape of the matrix is : ",np.shape(arr4x4))
print()
# Generate random matrix with 3x3x3 dim
arr3x3x3=np.random.random((3,3,3))
print("The generated 3x3x3 matrix is : ",arr3x3x3,end="\n")
print("The shape of the matrix is : ",np.shape(arr3x3x3))
print()
# Re-shape the 3x3x3 matrix to 1D array
arr1d_new=np.reshape(arr3x3x3,(1,27))
print("The reshaped 1d array is : \n",arr1d_new,end="\n")
print("The shape of the array is : ",np.shape(arr1d_new))
print()

# Generating and re-shaping an array
array=np.array([1,2,3,4])
print("The initial array is  : \n",array)
print("Initial array has shape : ",np.shape(array))
print()
array=np.reshape(array,(2,2))
print("The final array is  : \n",array)
print("Final array has shape : ",np.shape(array))
print()