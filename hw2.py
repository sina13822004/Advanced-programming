def list_tuple_dict(mydict: dict) -> list:
#myDict = {"A": 1, "B": 2, "C": 3}
    convertedList = []
for i in myDict:
    convertedList.append([i, myDict[i]])
print(convertedList)
