#Largest Increasing subsequence using dynamic programming
'''First of all initializing all the array value's lis(largest increaing subsequence)
 as 1 then moving forward and checking whether 
the right element is greater than the left one (if greater then 
			if arr[i]>arr[j]:
				lis[i]=max(lis[i],lis[j]+1))
Hence we find the largest increasing subsequence no				
'''

from collections import defaultdict
dc=defaultdict(list)
def LargestIncresingSubsequence(arr):
	n=len(arr)
	lis=[1]*n

	for i in range(n):
		for j in range(i):
			if arr[i]>arr[j]:
				lis[i]=max(lis[i],lis[j]+1)
	return lis
	
arr=[10,20,9,33,21,40,30]

'''for i in arr:
	dc[i]=1
#print(dc)	
lis=LargestIncresingSubsequence(arr)
print(lis)
for i,j in enumerate(arr):
	dc[j]=lis[i]

print(dc)'''
print(max(LargestIncresingSubsequence(arr)))


