#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		res=[]
		d=dict()
		for val in nums:
		    if val not in d:
		        d[val]=1
		    else:
		        d[val]+=1
		for val in d.keys():
		    if d[val]==1:
		        res.append(val)
        return sorted(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()
