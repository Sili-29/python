# ordered sequence of different types of values

nums=[23,12,45,78,29,94]
print (nums)

# How to get the values from a list
a= nums[3]
print (a)

#slicing of list
#getting index from index 2
a= nums[2:]
print(a)

#a=nums[7]
print(a)

#getting item of index -5
#index number starts from 0 - left to right and when we count from right to left we will start count from -1 ,-2 .-3 and so on
a=nums[-5]
print(a)


# geting last 2 items
print(nums[-2:])


names= ['silu', 'nitu', 'priya', 'piu']
print (names)

print(names[-2:])

values= [9.5, 'sili', 34]
mil= [nums,names,values]

print (mil)


#adding items to a list 

nums.append(90)  #List is mutable means we can change the value
print (nums)  

#adding items in a particular position
nums.insert(2,100)
print (nums)


#deleting values from a list

nums.remove(78)
print(nums)


# in data structure we have learnt about the push and pop.. pop command will remove the last element we have added 

nums.pop(2)
print(nums)

nums.pop()
print(nums)



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

#how to modify values from a list?
names[2]='Nitish'
print(names)

#checking the length of the list
print(len(names))
print(len(nums))


#Sorting the iteam in a list
names.sort()
print(names)

#sorting iteam in reverse
names.sort(reverse=True)
# or 
# names.reverse()

print(names)


