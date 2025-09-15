# # STRING DATA TYPE:-
# What is string :- 
# if anything id written inside quotes
# then it is called string data type 


# what type of data type is string :-
#   string is an immutable datatype
#    can not be modified = immutable
# string does support indexing 
# ===postive indexing :starts from left first indexis always 0
#===negative indexing :starts from right first in always -1
# string is an ordered datatype 
# string is reffered as str 
# " ", ' ',"''" ,""" """
# name='navya sri' 
# name="navya sri"
# name="""navya sri"""
# name='''navya sri'''
# name='navya "sri"'
# name='navya ""sri""'
# name="navya'sri'"
# name='navya ""sri""'
# examples
# name ="navya sri"
# surname='kanukati'
# password="guyikd@365"
# email="navyasrikanukati@gmail.com"
# print(type(name))# <class 'str'>
# print(type(surname))
# a=5
# b=2.5
# c=3-5j
# # print(f"a type is:{type(a)}")
# # print(f"b type is:{type(b)}")
# # print(f"c type is:{type(c)}")

# d='5'
# e='2.5'
# f='3-5j'
# print(f"d type is:{type(d)}")
# print(f"e type is:{type(e)}")
# print(f"f type is:{type(f)}")
# print("c type is:{type(c)}")   #c type is:{type(c)}
 ##    inedex ="+"
#girl="Navya_sri"
# print(girl[0])
# print(girl[1])
# print(girl[2])
# print(girl[3])
# print(girl[4])
# print(girl[5])
# print(girl[6])
# print(girl[7])
# print(girl[8])
# print(girl[9])
# print(girl[10])
# print(girl[11]) #IndexError: string index out of range
  # inedex ="-"
#print(girl[0])
# print(girl[-1])
# print(girl[-2])
# print(girl[-3])
# print(girl[-4])
# print(girl[-5])
# print(girl[-6])
# print(girl[-7])
# print(girl[-8])
# print(girl[-9])
# print(girl[-10])    #print(girl[-10]) IndexError: string index out of range
# print(girl[-11])
##        slicing
#creating pieces
# #strat:end:step
# password="kdhfurbf46#2"
# # print(password[4])
# #print kdhf
# #+ve
# print(password[4:6:1])
# #-v
# print(password[-2:-4:2])
#####################################################
#in built methods of string in python:-
# str99 ='APPLE'
# str88='banana'
# str77='mAngo'
# str66='PinEaPPlE'
# str55="Bunny@123"

# #case converstion methods:-
# #all case conversion methods work only alphabetic char
#       #1 Lower
# print(str99.lower())
# print(str88.lower())
# print(str77.lower())
# print(str66.lower())
# print(str55.lower())

#         #2 Upper
# print(str99.upper())
# print(str88.upper())
# print(str77.upper())
# print(str66.upper())
# print(str55.upper())
#       #3 capitalize() (in fist letter is capital and all other letter are small in one sent)
# str44="python is an easy 100%" 
# str33="java is veryhard 100%"
# print(str44.capitalize())
# print(str33.capitalize())
#       #4 title ()  (first leter of each word is capital and all other leters are small)
# print(str44.title())
# print(str33.title())
# str22='1rooma is gone 2custumre'
# print(str22.title())
#         # 5 swapcase (converts small leters to capital and capital leters to small)
# str11 ='aliana Dcruze is a BolIywood actResSs'  
# str00='APPLE grapes'
# str0='Ahemad is 123 year old'
# print(str11.swapcase())
# print(str00.swapcase())
# print(str0.swapcase())
#######################################################
# string and replece in built methods of string in pythoon 
str999='APPLE'
    # 1) FIND (returns the index of the first occurance of the substring)
# print(str999.find('P'))  #1
# print(str999.find('L'))  #3
# print(str999.find('h'))  # (if the substring is not found it will return -1)


#      #2)rfind(returns the index of the last occurance of the substring)
# print(str999.rfind('P'))  #2(last occurance of P is at index 2)
# print(str999.rfind('L'))  #3  
# print(str999.rfind('h'))  #-1 (if the substring is not found it will return -1)
    
    
#     #3) index (returns the index of the first occurance of the substring)

# # print(str999.index('A'))  #0
# print(str999.index('P'))  #1 
# print(str999.index('L')) #3
# # print(str999.index('M'))  #ValueError: substring not found (if the substring is not found it will return ValueError) 
# #       #4)rindex(returns the index of the last occurance of the substring)
# # print(str999.rindex('A'))  #0
# print(str999.rindex('P')) #2
# print(str999.rindex('L')) #3   
# # print(str999.rindex('M'))  #ValueError: substring not found (if the substring is not found it will return ValueError)
#         #5) replace (replaces a substring with another substring)
# str888='banana'
# print(str888.replace('a','o'))  #bonono
# print(str888.replace('na','123'))  #ba123123
##########################################
# cheking content:-creat a small app which takes string as an  input from user
#    and performs checking content bin built methods

x=input("enter a string: ")

#startswith(arg)
#print(x.startswith("buji"))

#endswith(arg)
#print(x.endswith("igke "))

# isalpha()
#print(x.isalpha()) Rahukisejyrdfofujgi  -->t  |Rahukisejyrdfofujgi.-->f 

#isdigit()
#print(x.isdigit())

#isalnum()
#print(x.isalnum())

#isspace()
#print(x.isspace())

#islower()
#print(x.islower())

#isupper()
#print(x.isupper())

#istitle()
#print(x.istitle())

######WHITESPACE HANDELING:-
# print(x)
# print(x.lstrip()) #will remove unnacessary empty space from left side
# print(x.rstrip()) #will remove unnacessary empty space from righ side
# print(x.strip()) #will remove from both side empty space 

