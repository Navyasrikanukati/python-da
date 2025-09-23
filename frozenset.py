#FROZENSET
  # same like set, but immutable.
  # initialize set:-
#f_set1=frozenset((1,2,3,4,5,6,7,8))
#print(f_set1)

# f_set2=frozenset(['a','A',34,76,0,True,False])
# print(f_set2)
# print(type(f_set2))

# f_set3 =frozenset({12,"hsgtwtjwuw" ,False,'0'})
# print(f_set3)
# print(type(f_set3))

##membership operators:-
# f_set4=frozenset([1,2,3,4,5])
# print(4 in f_set4)
# print(1 in f_set4)
# print(10 not in f_set4 )
# print(11 in f_set4)

# #set

# s1=frozenset([1,2,3,4])
# s2=frozenset([3,4,5,6])

# #union
# print(s1|s2)

# #intersection
# print(s1&s2)

# #difference
# print(s1-s2)
# print(s2-s1)

# #symmetric difference
# print(s1^s2)

# OTHER OPERATION:-
# s3=frozenset([1,2,3]) #subset
# s4=frozenset([1,2,3,4,5,6])# superset
# print(s3.issubset(s4))
# print(s4.issuperset(s3))

# print(s4.issubset(s4))
# print(s4.issuperset(s4))

# print(s3.issuperset(s4)) 

# dic1 ={
# 1:100,
# 's':'navya',
# None: 'nothing',
# True: 'yes',
# 2.3:'two points five',
# #[1,2,3]:'list',
# (1,3,4):'tup',
# frozenset([1,2,3,4]):10,
# }
# print(dic1)


#UNION
s1=frozenset([1,2,3,4])
s2=frozenset([3,4,5,6])
# print(s1 | s2)
# print(s1.union(s2))
# #intersection 
# print(s1&s2)
# print(s1.intersection(s2))
# #differece 
# print(s1-s2)
# print(s1.difference(s2))
# print(s2-s1)
# print(s2.difference(s1))
#symme
#print(s1^s2)
f1=frozenset([1,2,3,4,5])
# print(max(f1))
# print(min(f1))
# def avg(fset):
#     return sum(fset)/len(fset)
# print(avg(f1))

# import math 
# print(math.prod(f1))
# print(len(f1))
# print(sorted(f1,reverse=True))
# import statistics
# print(statistics.mean(f1))
# print(statistics.median(f1))
# print(statistics.mode(f1))
# print(statistics.stdev(f1))
# print(statistics.variance(f1))
# import numpy as np 
# print(np.median(f1))
# print(np.mean(f1))
# print(np.std(f1))
# print(np.var(f1))
# print(np.prod(f1))
# print(np.sum(f1))
# print(np.max(f1))
# print(np.min(f1))
# print(np.sort(f1)[::-1])
# print(np.sort(f1))
# print(np.size(f1))