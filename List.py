nums=[23,12,45,78,29,94]
print (nums)


a= nums[3]
print (a)

a= nums[2:]
print(a)

#a=nums[7]
print(a)

a=nums[-5]
print(a)

names= ['silu', 'nitu', 'priya', 'piu']
print (names)

values= [9.5, 'sili', 34]
mil= [nums,names,values]

print (mil)

nums.append(90)  #List is mutable means we can change the value
print (nums)  

nums.insert(2,100)
print (nums)

nums.remove(78)
print(nums)

nums.pop(2)
print(nums)

nums.pop()
print(nums)

# in data structure we have learnt about the push and pop.. pop command will remove the last element we have added 


#removing multiple values
del nums[2:]         
print (nums)


#adding multiple values
nums.extend([202,204,286,298])
print(nums)

# we will use some inbuilt functions

print(min(nums))

print(max(nums))

print(sum(nums))

