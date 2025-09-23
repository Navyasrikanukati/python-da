# The range data type in Python represents an immutable sequence of numbers, typically used for looping a specific number of times in for loops. 

# It generates numbers in a specified range without storing them in memory, which makes it highly efficient.
#RANGE

#mmutable sequence of number 
#  generates numbers on fly
# doesnt store numbers  in memory
# memorry efficient

#initialize range:-
# only single argument-->stop
#python takes defaukt start -->0
# python takes deflut step-->1 
# r1=range(5)
# print(r1)
# l1=list(r1)
# print(l1)

#if two number as an argument ,
#fist num -->start
#last num --.>stop
#python takes step nas a default -->1

# r2=range(5,15)
# print(r2)
# t1=tuple(r2)
# print(t1)
#if three arguments 
#first num -->start
#second num-->Stop
# #third num-->Step
# r3=range(2,20,5)
# print(r3)
# s1=set(r3)
# print(s1)


#ACCESSING ELEMENTS FROM RANGE:-
# r4=range(23,6,-1)
# print(r4)
# print(r4[0])
# print(r4[1])
# print(r4[2])
# print(r4[3])
# print(r4[4])

r5=range (-34,5,2)
#print(len(r5))
s1=set(r5)
print(s1)
print(max(r5))
print(min(r5))
print(sum(r5)/len(r5))


print(r5.count(2))
print(r5.index(2))