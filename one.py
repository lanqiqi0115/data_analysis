list1 = [1,2,3,4]
list2 = list('hello')
list3 = [i for i in range(10)]


list3.append(5)
list3.insert(0,44)
list3.extend(list2)
print(list1+list3)
print(list1*3)