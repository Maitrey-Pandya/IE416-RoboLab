import numpy as np
def main():

  # Generate random matrix
  arr6x6=np.random.random((6,6))
  print("The randomly generated 6x6 matrix is : \n",arr6x6)
  print()

  # Modify the given matrix according to given rules
  arr6x6[arr6x6>0.5]=1
  arr6x6[arr6x6<=0.5]=0
  print("After modification : ")
  print(arr6x6)
  print()

  # Slice the given matrix
  arr3x3=arr6x6[2:5,2:5] # For index (2,2) we have assumed 0 - based indexing as in python
  print("The sliced 3x3 array is : \n",arr3x3)
  print()
  
  # Find mean of the sliced matrix
  mean_arr=np.mean(arr3x3)
  print("The mean of this sliced array is : ",mean_arr)

main()