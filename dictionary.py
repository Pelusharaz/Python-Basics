'''creating a dictionary
with integer keys'''
Dict={1:'welcome',2:' to sharaz',3:'codes'}
print("\nwiththe use of integer keys:")
print(Dict)

#with mixed keys
Dict={'programmer':'sharaz','integers':[1,2,3]}
print("\nwith mixed keys:")
print(Dict)

#empy dictionary
Dict={}
print("empty dictionary:")
print(Dict)

#with dict()method
Dict=dict({1:'you',2:'sleep',3:'i code'})
print(Dict)

Dict=dict([(1,'programmer'),(2,'sharaz')])
print("\nDictionary with each item as pair")
print(Dict)

#creating nested Dictionary
Dict={1:'sharaz',2:'codes',
      3:{'p':'are','Q':'the best'}}
print(Dict)

#Adding elements to a Dictionary
Dict={}
print("empty dictionary")
print(Dict)

#adding elements one at a time
Dict[0]='you'
Dict[1]='sleep'
Dict[2]=3
print("\nafter adding 3 elements")
print(Dict)

'''Adding a set of values to a single
key'''
Dict['value_set']='we', 'code'
print("\nafter adding a set of values")
print(Dict)

#updating an exixting key's value
Dict[0]='they'
print("\nupdated:")
print(Dict)

#addding nested values
Dict[4]={'Nested':{'1':'geeks','2':'for','3':'life'}}
print("\nafter adding nested value")
print(Dict)

#Acessing elements from a dictionary
Dict={1:'welcome',2:' to sharaz',3:'codes'}
print("\naccesing elements using key:")
print(Dict[3])
#using get method
Dict={1:'welcome',2:' to sharaz',3:'codes'}
print("\nAccessing elements using get:")
print(Dict.get(1))

#Accessing elements from a nested dictionary
Dict={'Dict1':{1:'sharaz',2:'codes'},
      3:{'p':'are','Q':'the best'}}
print(Dict['Dict1'])
print(Dict['Dict1'][2])
print(Dict[3]['Q'])

'''Deleting elements from a dictionary
del dict-deletes the entire  dictionary'''
#initial dictionary
Dict={'Dict1':{1:'sharaz',2:'codes'},
      3:{'p':'are','Q':'the best'}}
print("\nintial dictionary:")
print(Dict)

#deleting deleting keys
del Dict['Dict1'][2]
del Dict[3]['p']
print("\nafater deletion")
print(Dict)

#using pop
Dict={1:'sharaz',2:'codes',
      3:{'p':'are','Q':'the best'}}
print("\nintial dictionary:")
print(Dict)

pop_ele=Dict.pop(1)
print('\nafter deletion:'+str(Dict))
print('value associated with the popped key is'+str(pop_ele))

#using clear
Dict={1:'sharaz',2:'codes',
      3:{'p':'are','Q':'the best'}}
print("\nintial dictionary:")
print(Dict)
#deleting entire dictionary
Dict.clear()
print("\nDeleting entire dictionary")
print(Dict)
