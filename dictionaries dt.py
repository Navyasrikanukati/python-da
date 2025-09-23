#  Introduction to Dictionaries:-

# 	Definition: A dictionary in Python is a collection of key-value pairs.

# 	Syntax: {key1: value1, key2: value2, ...}

# # 	Characteristics: Unordered, mutable, and indexed by keys
# dic1={
#     1:1,
#       2:4,
#       3:9,
#       4:16,
#       5:25
#       }
# print(dic1)
# print(type(dic1))

# dict2=dict()
# print(dict2)
# print(type(dict2))

# dic3={}
# print(dic3)
# print(type(dic3))


# dic4={
#     "fruit1":"apple",
#     "fruit2":"grapes",
#     'fruit3':"bunana",
#     "fruit4":"papaya"
# }
# print(dic4)

# dic5=dict( male="navya",sachin="cicketer",manju="comman girle")
# print(dic5)

# hubby=["virat","ramcharan","ntr","allu arjun","jai balayya","masha babu"]
# wifes=["anushka","upasana","pranathi","seha","yyy","namrtha"]
# dict6=dict(zip(hubby,wifes))
# # print(dict6)

# # students=["navya","uma","neha","kiran","sameer","aehmad","vijay","mirze","bunny"]
# # dict7=dict.fromkeys(students,"samantha")
# # print(dict7)
# # dict8=dict([
# #     ("laila", "maju"), 
# #     ("heer", "ranjtha"), 
# #     ("navya", "sri"),
# #     ("amutha", "pandu")
# # ])
# # print(dict8)

# #acessing elements
# #print(dict6)
# #print ram wife name
# #print(dict6['ramcharan'])
# #print(dict6["seha"])
# #print(dict6[3])
# print(dict6.keys())
# print(type(dict6.keys()))
# #all values
# print(dict6.values())
# #all iteams
# print(dict6.items())


#asscssing elements using get()
dict={
    'pari':"action",
    'lion':"animal",
    'babool':"tree",
    "banana":'tree',
    "antalia":"house",
    "jannat":"heaven",
    "lands end":"place",
    "guido van rossum":"python"
 }
# print(dict['lands end'])
# print(dict["guido van rossum"])

# print(dict.get('lands end'))
# print(dict.get('antalia'))

# #MODIFYING DICT
# dict["polio"]="disease"
# print(dict)

# #update
# dict['pari']="angel"
# print(dict)
# dict["jamu"]=(1,2,3)
# #remove elment
# dict.pop("pari")
# print(dict)
# dict.pop('antalia')
# print(dict)

# del dict["banana"]
# print(dict)

# dict.clear()
# print(dict)

# dict.popitem()
# print(dict)


# dict.update({"alia":"randir","sumona":"rajesh","navya":"sri"})
# print(dict)

# dict.setdefault("amruthaa")
# print(dict)

