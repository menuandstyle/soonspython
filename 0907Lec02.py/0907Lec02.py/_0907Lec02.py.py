data=['a', 'b', 'c', ['abcd', 'efg']]
#배열의 첫 방은 0, 배열의 마지막 방은 -1 의 숫자를 가진다.
print(data[0])
print(data[-1])

#efg 출력하기
print(data[3][-1])

b=[1, 2, 3]
c=['Life', 'is', 'too', 'short']
f=b+c
#배열들끼리 더하기
print(b+c)
print(f)
#배열에 상수 곱하기
print(b*3)

#리스트 변경
guests = ['a','b','c','d']
guests[0] = 'greenjoa'
guests[1] = ['greenjoa1', 'greenjoa2']
guests[1:2] = ['greenjoa1', 'greenjoa2']
print(guests)

#2번 인덱스에 'e' 삽입
guests.insert(2, 'e')
print(guests)

#guests 배열에서 'c' 삭제
guests.remove('c')
print(guests)

#첫번째 방 값 삭제
del guests[0]
print(guests)

#인덱스 출력, 해당 값이 있는 인덱스가 없으면 에러 발생
print(guests.index('d'))

#아이디 값이 세 개 있는 리스트
idlist = ['id0', 'id1', 'id2']

#패스워드 값이 세 개 있는 리스트
passlist = ['pass1', 'pass2', 'pass3']

#아이디와 패스워드를 합하기
list0 = idlist + passlist
print(list0)

#리스트 멤버 엑세스 하기, 에서,
#공백이 없으면 안된다. 항상 들여쓰기를 해주어야 for 문의 것이라는 걸 알게 된다.
#파이썬에서는 들여쓰기가 너무너무, 완전너무, 진짜정말너무많이 중요하다. 파이썬에서는 {} 이 없기 때문이다.
#아, 그리고 for 문이 끝나는 곳에서 콜론 : 이 들어간다.
for steps in list0 :
    print(steps)
for steps in range(6) :
    print(list0[steps])

#sort 와 reverse
scores = [85, 62, 63, 45, 90]
scores.sort()
print(scores)
scores.reverse()
print(scores)

#상위 다섯 개의 점수를 뽑아 새로운 배열로 만들고, 출력하기
# ( 탑파이브를 만들어 배열을 출력하기 )
nEntries = len(scores)
newsc = [1, 1, 1, 1, 1]
for steps in range(nEntries) :
    newsc[steps] = scores[steps]
print(newsc)

#isinstance 함수 쓰기
for steps in data :
    if isinstance(steps, list) : #steps 가 list 냐? 맞다면 if 문을 수행하고,
        for step in steps :
            print(step)
    else :
        print(steps)

#extend 사용하기 : 리스트를 더하는 함수
scores.extend([50, 60])
print(scores)
#append 와 extend 의차이점은?
scores.append([50, 60])
print(scores)

#리스트와 튜플의 차이 : 튜플은 변경이 안 된다.
