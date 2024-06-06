nums=[1,2,3]
k=3

count=0
sum=0 
for i in range(len(nums)):
    sum+=nums[i]
    count+=1
    if sum==k:
        print(count)