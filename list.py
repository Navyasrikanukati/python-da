# str1='fara'
# str2='neha'
# str3='navya' 
# str4='sri'
# str5='bunny'
# str6='amrutha'
# str7='panud'
# students1 =['neha','navya','bunny','pandu']
# students2 =list(('ravi',123,True,56.3,9+6j,['A',1.1,False]))
# students3= list({34,56.5,5-5j,'sam','Apple@23'})
# students4 = list(['A','B','C','D','E',1,2,3,0.0,0.1,0.2,True,False])
# print(f'type of student1 is {type(students1)}')
# print(f'type of student2 is {type(students2)}')
# print(f'type of student3 is {type(students3)}')
# print(f'type of student4 is {type(students4)}')

# l1=[10,20,30,40]
# print(l1)
# print(type(l1))
# #+ve
# print(l1[0])
# print(l1[1])
# print(l1[2])
# print(l1[3])
# #-ve
# print(l1[-1])
# print(l1[-2])
# print(l1[-3])



# list1=[12,24,36,48,60,72]
# print(list1[2:5:1])
# print(list1[2:5:])
# print(list1[-4:-1:-1])
# #slicing
# print(list1[0:2:1])
# print(list1[2::1])
# print(list1[::2])
# print(list1[::-1])
# print(list1[-1::-2])



# # BUILT IN METHODS:-
list2=['A',23,'Baby',45.5,True]
# #append:- adds element at the end of the list 
# list2.append(False)
# print(list2)
# list2.append('Buji')
# print(list2)


#list2.append(100,200)  its is  not correct bec append is only one element add not two are more


# extend:-adds  new elements at end of the existing elements
#takes  multiple arguments

# list2.extend([100,200,300])
# print(list2)

# list2.extend(('m','n',12,5.5, 'petorl'))
# print(list2)

# list2.extend({0,0.01,0.02,'male'})
# print(list2)

#INSERT:- 
#insert an iteam at specfied  index 
# list2.insert(0,'apple')
# print(list2)

# list2.insert(3,'navya')
# print(list2)

# #REMOVE
# list2.remove('Baby')
# print(list2)


# list2.remove(1)
# print(list2)
# list2.remove(1.1)
# print(list2)#error

#POP

list3=[100,200,300,400,500,600,700]

# list3.pop() 
# print(list3)
# list3.pop(3)
# print(list3)
# list3.pop(0)
# print(list3)
# list3.pop()
# print(list3)


# #clear()
# list3.clear()
# print(list3)


###index
list4=[11,22,33,44,55,66,77,88,99,88,77,66,55,44,33,22]
# print(list4.index(44))
# print(list4.index(77))

# ########COUNT()
# print(list4.count(22))
# print(list4.count(11))
# print(list4.count(77))
# print(list4.count(1000))

####len()


# list5=['A',1,2,3,4,5,6,True,False,[12,23,34],'mango','nimboo',56.6]
# print(len(list5))

list6=[133,24,2,635,9286,165,7,0,10000]
# list6.sort(reverse=True)
# list6.sort()
# print(list6)


# list6.reverse()
# print(list6)

# print(list6[::-1])
# l2=[1,2,3]
# l1=[1,2,3]
# l2=l2
# print(l1)
# print(l2)

# print(id(l1))
# print(id(l2))
# j1=[100,200,300]
# j2=j1.copy()
# print(j1)
# print(j2)
# print(id(j1))
# print(id(j2))
###ADDITIONAL:-
ll1=[1,2,3]
ll2=[9,8,7]
print(ll1+ll1+ll2)
#repetition
print(ll1*3)