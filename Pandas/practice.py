import pandas as pd



# data = {
#     "Name": ["Rahul", "Aman", "Priya"],
#     "Age": [20, 22, 21]
# }
# df = pd.DataFrame(data)
# print(df)


# # column print
# data_list = [
#     ['John',28,'New york',6500],
#     ['Anna',40,'Paris',3400],
#     ['Peter',29,'Bareli',62000],
#     ['Linda',42,'Londan',85000]
# ]
# df2 = pd.DataFrame(data_list)
# columns = ["Name","Age","City","Salary"]
# df2=pd.DataFrame(data_list,columns=columns)
# # print(df2['Name'])
# # print(df2['Age'])
# print(df2[['Age','City']])


# # column add
# data_list = [
#     ['John',28,'New york',6500],
#     ['Anna',40,'Paris',3400],
#     ['Peter',29,'Bareli',62000],
#     ['Linda',42,'Londan',85000]
# ]
# df2 = pd.DataFrame(data_list)
# columns = ["Name","Age","City","Salary"]
# df2=pd.DataFrame(data_list,columns=columns)
# df2["Designation"] = ["Doctor","Eng","Doctor","Eng"]
# print(df2)


# # drop data
# data_list = [
#     ['John',28,'New york',6500],
#     ['Anna',40,'Paris',3400],
#     ['Peter',29,'Bareli',62000],
#     ['Linda',42,'Londan',85000]
# ]
# df2 = pd.DataFrame(data_list)
# columns = ["Name","Age","City","Salary"]
# df2=pd.DataFrame(data_list,columns=columns)
# df2["Designation"] = ["Doctor","Eng","Doctor","Eng"]
# df2=df2.drop(["City","Salary"],axis=1)
# print(df2)

