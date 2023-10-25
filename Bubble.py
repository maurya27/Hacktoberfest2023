def Bubble_Sort(arr, n):
	flag = True
	
	for i in range(1,n):
		flag = False
		for j in range(n-i):
			if (arr[j] > arr[j + 1]):
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				flag = True
		
		if (flag == False):
			break
		
n = 5
arr = [2, 0, 1, 4, 3]
Bubble_Sort(arr, n)
print("The Sorted Array by using Bubble Sort is : ", end='')
for i in range(n):
	print(arr[i], end= " ")
