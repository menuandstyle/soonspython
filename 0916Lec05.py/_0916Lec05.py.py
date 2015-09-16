#Lec03.pdf 파일다루기 부터
#주의사항 1.Close() 를 꼭 해주어야한다. 자동해제되는 경우 제외. ex)myFile.close() 

#fileName = "greenjoa.txt"
#with 로 오픈하겠다.
#w+ : 읽고 쓰는 작업을 하겠다.
#with open(fileName, "w+") as myfile :
#    myfile.writelines("201311221 안순원")
#    myfile.writelines("201311222 이순원")
#    myfile.writelines("201311223 박순원")
#    myfile.writelines("201311224 김순원")


#전체를 다 읽어오기
#with open(fileName, "r") as myfile:
#    content = myfile.read()
#    print(content)


#라인 단위로 읽어오기
#with open(fileName, "r") as myfile:
#    #라인 단위로 읽어오는 첫 번째 방법 : readlines()
#    content = myfile.readlines()
#    #라인 단위로 읽어오는 두 번째 방법 : for line in content:
#    for line in content:
#        print(line)
#    myfile.close()


#클래스팅에서 파일입출력 예제 하나 다운로드 받기
#' 파일입출력예제1.txt ' 출력하기
#fileName = "파일입출력예제1.txt"
#READ = "r"
#with open(fileName, READ) as myfile:
#    fileContents = myfile.read()
#    print(fileContents)


##Monica 의 대사만 추려서 출력하기
#fileName = "파일입출력예제1.txt"
#fileName2 = "monica.txt"
##그리고 monica 의 대사만 monica.txt 에 저장한다.
#with open(fileName, "r") as myfile, open(fileName2, "w") as monica:
#            for content in myfile:
#                (role, etc) = content.strip().split(":")
#                if (role == "Monica") :
#                    monica.write(etc)
#                    monica.write("\n")


#help(str.split)


#https://docs.python.org/3/
#여기는 나와 파이썬 사용자들이 각자가 만든 걸 자유롭게 올릴 수 있는 공간이다.


##Monica 의 대사만 추려서 출력하기
#fileName = "파일입출력예제1.txt"
#fileName2 = "monica2.txt"
##그리고 monica 의 대사만 monica.txt 에 저장한다.
#with open(fileName, "r") as myfile, open(fileName2, "w") as monica:
#            for content in myfile:
#                (role, etc) = content.strip().split(":",1)  #max split 은 1 로 주었다.
#                if (role == "Monica") :
#                    monica.write(etc)
#                    monica.write("\n")


##이제는 주인공들 나오는 순서대로 list 에 저장해본다. 문자열이 아닌 list 에 저장한다.
#fileName = "파일입출력예제1.txt"
#fileName2 = "roleList.txt"
#roles = []  #빈 리스트가 만들어졌다.
##그리고 monica 의 대사만 monica.txt 에 저장한다.
#with open(fileName, "r") as myfile, open(fileName2, "w") as roleList:
#            for content in myfile:
#                (role, etc) = content.strip().split(":",1)  #max split 은 1 로 주었다.
#                roles.append(role)
#print(roles)


import pickle
#pickle 은 비트기 때문에 b 를 붙여줘야한다. wb, rb
#이제는 주인공들 나오는 순서대로 list 에 저장해본다. 문자열이 아닌 list 에 저장한다.
fileName = "파일입출력예제1.txt"
fileName2 = "roleList.txt"
roles = []  #빈 리스트가 만들어졌다.
#그리고 monica 의 대사만 monica.txt 에 저장한다.
with open(fileName, "r") as myfile, open(fileName2, "wb") as roleList:
    for content in myfile:
        (role, etc) = content.strip().split(":",1)  #max split 은 1 로 주었다.
        roles.append(role)
    pickle.dump(roles, roleList)

with open(fileName2, "rb") as roleList:
    result = pickle.load(roleList)
print(result)
#pickle.dump, pickle.load 이 두 가지를 가지고 읽어내면 된다.


#csv 란 excel 에서 만들 수 있는 확장자