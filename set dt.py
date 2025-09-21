# SET :-
# #set is a collection 
# set is collecction unique elements
# set is mutable
# set is unordered
# doest allow duplicaties
# it is partially heterogeneous
# it doesnot support indexing


# how to intialize  /cerating set:-
# set1={1,2}
# print(set1)
# print(type(set1))

# set2= set([1,2,3,4,5])
# print(set2)
# print(type(set2))

# set3=set((4,5,6,7))
# print(set3)
# print(type(set3))

# set4=set({20,30,40,40,50})
# print(set4)
# print(type(set4))

# set5=set("apple")
# print(set5)
# print(type(set5))

# #membership operator:-
# in
# not in
#set100={"A",12,34.5,67,1.0,False,('a','c',100,True)}
# print(120 in set100)
# print(120 not in set100)
# print('A'.lower()in set100)
# print(1 in set100)
# #print(0.0000 in set100)
# #print (1 in set100)
#  ##  ADDING ELEMENTS TO THE SET:-
set420={12,23,34,45,56,'A','a',65}
# # set420.add(67)
# # print(set420)
# # print(type(set420))
# # set420.add("BABOON".title())
# # print(set420)
# # set420.add(False)
# #print(set420)
# set420.add((1,2,3))
# print(set420)
# REMOVING:-
#set420.remove(False)
#set420.remove(34)
# #set420.remove(9*5)
# set420.remove((True+True)*6)
# print(set420)

# set420.remove(chr(97))
# print(set420)
# set420.remove(ord('A'))
# print(set420)
#######################3333333
# set22={'A','B',6,7.5,(1,2,3),"Hello"}
# print(set22)
# # print(type(set22))
# #clear()

# set22.clear()
# print(set22)
# print(type(set22))
#update
# set22.update('navya')
#print(set22)
# set22.update([12,45,67])
# print(set22)
#set22.update((True,False,0,1,(2,1,0,)))
# #pop
# set22.pop()
# print(set22)


################
#set operations

# set1={1,2,3}
# set2={3,4,5}
# ##union
# set3=set1 |set2
# print(set3)
# #differeceset
# set4=set1-set2
# print(set4)
# set5=set2-set1
# print(set5)
# #intersection
# set6=set1&set2
# print(set6)
# #symmetric difference
# set7=set1^set2
# print(set7)

######################
# #isdisjoint
# set1={11,22,33,44}
# set2={99,33,10,200}
# # print(set1.isdisjoint(set2))
# # #difference_update
# # set1.difference_update(set2)
# # print(set1)
# #intersection_update
# set1.intersection_update(set2)
#print(set1)
#is subset
# s1={1,2,3,4,5}
# s2={4,5}
# s3={3,4,5}
# s4={9,1,2,3}
# s5={3,4,5,6,7}
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s3.issubset(s1))
# print(s5.issubset(s2))
# print(s5.issubset(s1))
############symmetric_difference_update
s11={1,2,3,4}
s12={4,5,6,7,8}
s11.symmetric_difference_update(s12)
print(s11)