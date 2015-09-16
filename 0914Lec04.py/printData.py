#def getNames():
#    names=["greenjoa1", "greenjoa2", "greenjoa3"]
#    newName = input("Enter last guest:")
#    names.append(newName)
#    return names

#def printNames(names):
#    for name in names:
#        print(name)
#    return

#def main():
#    printNames(getNames())
#    return

#main()




#def printData(data):
#    for item in data:
#        #홍길동, 암살, 베테랑 각각 출력되게 하기
#        if isinstance(item, list):
#           for items in item:
#               print(items)
#        else:
#            print(item)

#data = ["홍길동", ["암살", "베테랑"], "고길동", ["암살"]]




#파이썬에서 재귀함수 쓰기
def printData(data, level=0):
    for item in data:
        #홍길동, 베테랑, 류승완, 황정민, 유아인, 고길동, 암살 출력되게 하는 재귀함수 쓰기
        if isinstance(item, list):
            printData(item, level+1)
        else:
            for i in range(level):
                print("\t", end="")
            print(item)

data = ["홍길동", ["베테랑", ["류승완", "황정민", "유아인"]], "고길동", ["암살"]]
printData(data)


import printData