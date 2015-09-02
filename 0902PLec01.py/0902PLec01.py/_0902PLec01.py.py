# 숫자 출력 포맷
#print ("I have %d cats and %d dogs"% (5,6))
# \ 는 엔터를 쳤는데도 문장이 이어질 때, 윗줄과 아랫줄을 문장으로써 이어주는 역할
#print("Here are the numbers!" + \
#    " The first is {0:d} The second is{1:4d} ".format(7, 8))


# 형변환하기
#print("한글") <-이걸 넣게 되면 한글로 변환을 못한다구 뜨면서 cmd 창이 엉망이 된다.
#그래서 고급저장옵션 으로 가서 인코딩을 utf8 로 바꿔야 한다. 그럼 이제 된다.
#여러 줄의 주석 처리시 ctrl+kc:주석처리 ctrl+ku:주석해제 로 간편하게 쓰도록 한다.
#print("한글")
#salary = input("Please enter your salary: ")
#bonus = input("Please enter your bonus: ")
#payCheck = salary + bonus
#payCheck = float(salary) + float(bonus)
#print(payCheck)
#print(type(payCheck))
#round(payCheck, 2)


# 문자열 인덱싱
#name="greenjoa"
#print(name[0])
#print(name[-1])
#print(name[-2])


# 문자열 슬라이싱
# 후에 파일 파싱할 때 유용하게 쓰인다
#name="greenjoa"
#print(name[0:3])
#0<=name<3
#info="201012345greenjoa"
#sid=info[:0]
#sname = info[9:]
#print(sid+""+sname)


# 정렬
#a="I eat %10s apples." %"five"
#b="I eat %-10s apples." %"five"
#print(a)
#print(b)
#c="Error is %d%%." %98
#print(c)


# 문제
yeah = input("Wanna exit?: ")
print(yeah.upper())