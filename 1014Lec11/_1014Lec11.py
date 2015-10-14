#Lec08정규표현식1.pdf
import re
pattern = re.compile("d")
result = pattern.search("dog")
print(result)
result2 = pattern.search("dog", 1)  #dog 의 1 번째 인덱스부터 비교하라. 즉, og 랑 비교하라.
print(result2)
print("\n")


#문장단위로 끊어보자.
Str = '''sample1.
sample2.
sample3.''' #''' 이렇게 여러 줄이라는 걸 표현한다.
p = re.compile('^.*$', re.M) #' 마지막 ' 에 해당하는 건 $ 였다.    #멀티라인에 해당하는 M 이란 옵션을 준다.
result = p.search(Str);
print(result.group())
print("\n")


#fullmatch 의 사용형식
pattern = re.compile("o[gh]")
result = pattern.fullmatch("dog")
print(result)
result2 = pattern.fullmatch("ogre")
print(result2)
result3 = pattern.fullmatch("doggie", 1, 3) #1번째, 그리고 2번째 인덱스 방 안 하고만 비교를 한다.
print(result3)
print("\n")


#split 을 써보기
pattern = re.compile("\W+")
result = pattern.split("words, words, words.")
print(result)
result2 = pattern.split("words, words, words.", 1)
print(result2)
print("\n")

pattern = re.compile("x*")
result = pattern.split("axbc")
print(result)
print("\n")


#sub 써보기 : 문자가 아닌 건 다 없애서, 문자만 남게끔
result = re.sub(r'\W','','a:b:c, d.')
print(result)
print("\n")


#탐욕적인 매칭
str =  '<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*)">', str)
print(result.group(1))
print(result)
result = re.search(r'href="(.*?)">', str)
print(result.group(1))
print(result)
print("\n")


#주민등록번호인지 확인하고, 앞뒷부분을 잘라보기
st = "123456-1234567"
pattern= re.compile("\d{6}-\d{7}")  #주민등록번호인지 확인하고
result = pattern.fullmatch(st)  #앞뒷부분을 잘라보기
print(result)
#result2 = pattern