#dir 연습하기
data = ['a', 'b', 'c']
print(dir(data))

#enumerate 연습하기
data2 = list(enumerate("greenjoa"))
print(data2)

#filter 이용해서 배열값들 중에서 짝수만 출력하기
list2 = [1,2,3,4,5,6,7,8,9,10]
def zzaksu(l):
    result=[]
    for i in l:
        if (i%2)==0:
            result.append(i)
    return result
print(zzaksu(list2))

#id 값을 출력하기
a=3
print(id(3))
print(id(a))

#lambda 로 짝수만 출력하기
l = [lambda list:[1,3,5,7,9], lambda list:[2,4,6,8,10]]
print(l[1](list))

#list 함수로 새로운 리스트를 만들기
a=[1,2,3]
b=list(a)
c=a
print(id(a))
print(id(b))
print(id(c))

#map 내장함수 해보기
def two_times(x): return x*2
print(list(map(two_times, [1,2,3,4])))

#repr 내장함수 해보기
print(eval(repr("hi".upper())))

#sort 내장함수 연습으로, 무작위로 리스트에 값을 넣어 정렬하기
sortlist=['r','te','Wg','a','c','b']
print(sorted(sortlist))
#리스트 자료형에도 sort라는 함수가 있다. 하지만 리스트 자료형의 sort함수는 리스트 객체 그 자체를 소트할 뿐이지 소트된 결과를 리턴하지는 않는다.
a=[3,1,2]
result = a.sort()
print(result)   #아마 출력되는 것이 없을 것.

#zip 내장함수 연습하기
data = {'홍길동':[80,70,60,92],
        '김길동':[24,35,18.10],
        '고길동':[10,20,8,5]}  #꼬레와 딕셔나리데스.
print(data['홍길동'])
print(data['김길동'])
print(data['고길동'])
print(sorted(data))
print(data.keys())
print(data.values())
#ㅇ민과 상민의 코드가 클래스팅에 올라갔습니다.
