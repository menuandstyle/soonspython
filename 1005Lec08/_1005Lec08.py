##클래스 다중상속
#class A():
#    def __init__(self, a):
#        self.a = a
#    def show(self):
#        print('show:', self.a)

#class B(A):
#    def __init__(self, b, **arg):
#        super().__init__(**arg)
#        self.b = b
#    def show(self):
#        print('show:', self.b)
#        super().show()

#class C(A):
#    def __init__(self, c, **arg):
#        super().__init__(**arg)
#        self.c = c
#    def show(self):
#        print('show:', self.c)
#        super().show()

#class D(B, C):
#    def __init__(self, d, **arg):
#        super().__init__(**arg)
#        self.d = d
#    def show(self):
#        print('show:', self.d)
#        super().show()

#data = D(a=1, b=2, c=3, d=4)
#data.show()

#super(B, data).show()




##Private Variables
#class Mapping:
#    def __init__(self, iterable):
#        self.items_list=[1,2,3,4]
#        self.__update(iterable)

#    def update(self, iterable):
#        for item in iterable:
#            self.items_list.append(item)

## private copy of original update() method
#    __update = update   #이렇게도 사용할 수 있다!

#class MappingSubclass(Mapping): #Mapping 객체를 상속받음.

#    def update(self, keys, values):
#        # provides new signature for update()
#        # but does not break __init__()
#        for item in zip(keys, values):
#            self.items_list.append(item)

#data = MappingSubclass(['i m fine! ' 'thank you and you'])  #매핑시키고
#print(data.items_list)  #출력해본다

#data.update('new', 'update')   #업데이트시키고
#print(data.items_list)  #출력해본다. 신기한 방식으로 append 된 것을 확인할 수 있다.




##예외정보를 튜플로 반환하는 연습
#import sys
#number1 = float(input("enter a number : "))
#number2 = float(input("enter a number : "))
#try :
#    result = number1/number2
#    print(result)
#except :
#    error = sys.exc_info()[0]
#    print(error)
#finally :
#    print("Done")




##exit() 가 되는 위치를 찾기
##정답: finally 까지 다 수행함
#import sys
#number1 = float(input("enter a number : "))
#number2 = float(input("enter a number : "))
#try :
#    result = number1 / number2
#    print(result)
#except :
#    error = sys.exc_info()[0]
#    print(error)
#    sys.exit()
#finally:
#    print("Done")#내 과제2 과제를, 예외처리하고 실행시켜보기import pickle

try:
    import xlsxwriter	#엑셀 파일을 사용하기 위해 xlsxwriter를 import 한다.
    import mod1 #이것은 내가 만든 모듈로, 리스트 내의 중복되는 값을 제거하는 함수가 담겨있다.
except:
    error = sys.exc_Info()[0]
    print(error)

fileName = "201401.txt"
fileName2 = "thirdField.txt"

alls = [] #필드 저장을 위한 빈 리스트를 만든다.

print("2014년 한달 동안 도서관에서 대출된 이력사항의 세 번째 칼럼들을 정리하여 보여드립니다.")
print("자료가 너무 방대하여 시간이 오래 걸립니다.")

with open(fileName, "r") as myfile, open(fileName2, "wb") as thirdField:
	#원본 데이터 파일과, 세 번째 칼럼들을 담을 파일을 각각 읽기, 쓰기 형식으로 연다.
	#pickle 은비트기때문에b 를붙여줘야한다. wb, rb
    for content in myfile:
        (c1, c2, c3, c4, c5) = content.strip().split("|")	# | 로 데이터 한 줄마다 칼럼들을 분할한다.
        alls.append(c3)	#세번째 필드들이 나오는 순서대로 list 에 저장한다. 문자열이 아닌 list 에 저장한다.

    dup_removed_alls = mod1.remove_duplicates(alls) #리스트 alls 내의 중복되는 값들을 하나로 통일시키기 위해 import 한 모듈 내부의 함수를 사용하였다. < mod1.py > 참조.
    pickle.dump(dup_removed_alls, thirdField)	#dump 함수를 사용해 thirdField.txt 텍스트 파일에, 중복되는 값들을 하나만 남기고 나머지는 제거한 깔끔한 형태의 리스트 alls 안의 값들을 쓴다.

with open(fileName2, "rb") as thirdField:
    result = pickle.load(thirdField)	#세 번째 칼럼들을 출력한다.
print(result)



print("\n저중에서 원하시는 필드값을 입력하세요. 해당 데이터로 구성되는 엑셀파일을 만들어드립니다.")
f = input()
fileName3 = f + ".xlsx"	#사용자로부터 파일 이름을 입력받아, 자동으로 엑셀 파일을 생성한다.
workbook = xlsxwriter.Workbook(fileName3)
worksheet = workbook.add_worksheet()
row = 0
col = 0
print("자료가 너무 방대하여 시간이 오래 걸립니다.")
with open(fileName, "r") as myfile:
    for content in myfile:
        (c1, c2, c3, c4, c5) = content.strip().split("|")	# | 로 데이터 한 줄마다 칼럼들을 분할한다.
        if (c3 == f):	#분할된 칼럼들 중 세 번째 칼럼이 사용자가 원하는 필드값과 일치하면
            worksheet.write(row, col, c1)	#엑셀파일의 한 행에 네 개의 열에다가 분할한 칼럼  정보들을 입력한다.
            worksheet.write(row, col+1, c2)
            worksheet.write(row, col+2, c3)
            worksheet.write(row, col+3, c4)
            row += 1	#엑셀파일의 다음 행으로 넘어간다.
    workbook.close()    #꼭 닫아주어야 한다. 그러지 않으면 엑셀 파일이 생성되지 않는다.
