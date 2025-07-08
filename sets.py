# An Unordered and Unique elements
# in sets the duplicate values are not allowed
my_sets= {'mon', 'tue', 'mon'}
print(my_sets)

#adding new values in sets
my_sets.add('thurs')
print(my_sets)

#adding the existing value
my_sets.add('mon')
print(my_sets)
# the sets does not allow the duplicate value. we won't see any difference

#we will convert a list to sets. the list will have duplicate values
my_list=['sun', 'mon', 'tue', 'fri', 'sat' ,'mon', 'sun', 'tue','fri', 'sat' ]
print(my_list)
days_set=set(my_list)
print(days_set)