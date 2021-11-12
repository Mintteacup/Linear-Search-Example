#The list of values to search through
arr = [0, 56, 5, 45, 3, 2, 3, 8]
#Length of the Array
length = len(arr)
#How many times the program will loop
loopTimes = 3

#Linear Search Function
def linearSearch(arr, length, x):
  #Looks through the list
  for i in range(0, length):
    if (arr[i] == x):
      return i
  return -1

while loopTimes > 0:
  x = int(input("Enter the Value to Search For: "))
  result = linearSearch(arr, length, x)

  if (result != -1):
    print("Element Found at Index: ", result)
  else:
    raise Exception("Element Not Found")
  
  loopTimes -= 1