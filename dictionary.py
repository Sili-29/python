# kind of list but items are stored in key value pair

marks= {'hindi':80 , 'eng':90, 'math':99}
print(type(marks))
print(marks)

print(marks['hindi'])

car={'brand':'baleno', 'year': 2023, 'name':'nitish', 'loc':'bangalore', 'km': 2500.50}
print(car)
print(car['km'])

#how to add the items or append the items
marks['history']=85
print(marks)    

# there are 2 ways of getting the values of keys
print(marks.get('history'))
print(marks['hindi'])


# how to delete the items from a dictionary
del car['loc']
print(car)

# getting number of key-value available in dictionary
print(len(car))
print(len(marks))