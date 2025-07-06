# Same as list but it is immutable means we can not modify the items of Tuple

# Immutable and Ordered

days=('mon', 'tue', 'wed')

dayz=('thurs', 'fri', 'sat', 'sun', 'sun', 'sun')
print(type(days))

print(days[0])

# it will count how many sun are available in the tuple dayz
print(dayz.count('sun'))

#we can reassign the value
#dayz=(20,30)
#print(dayz)
# it will print 20 and 30 now

# how to check the item is present in which index
print(dayz.index('thurs'))
print(dayz.index('sun'))