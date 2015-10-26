#정규표현식2.pdf




##findall  이용하기
#import re

#str = """Window
#Unix
#Linux
#Solaris"""   #멀티라인으로 문자열이 주어졌다. 연속된 이중인용부호 세 개 (""") 이용
#p = re.compile('^.+', re.M) #M 이 주어진 것은, Multiline 멀티라인에 해당하는 플래그 값
#print(p.fildall(str))




##group 에 이름 지정하기
#import re

#m = re.match(r"(?P<first_name>\w+) (?P<last name>\w+)", "Malcolm Reynolds")
#print(m.group('first_name', 'last_name'))
#print(m.groups())




##group 에 디폴트값 주기
#import re

#m = re.match(r"(\d+)\.?(\d+)?", "24")
#print(m.groups())
#print(m.group(0))




##group 을 dictionary 로 출력하기
#import re

#m = re.match(r"(?P<first_name>\w+) <?P<last_name>\w+)", "Malcolm Reynolds")
#print(m.groupdict())




##Lookahead assertion 
#import re

##p = re.compile(".+:")
#p = re.compile(".+(?=:)")   #콜론에 해당하는 건 지우고, 콜론에 해당하는 것 앞에 것 까지만 결과값으루 주겠다, 라고 하는 경우
#m = p.search("http://google.com")
#print(m.group())




##현재 디렉토리를 c 디렉토리로 옮겨보기
#import os
#import re
#import glob
#os.chdir('C;/Python34/')  #chdir : 인자 안의 폴더로 이동
#glob.glob("*") #glob : 현재 디렉토리에 있는 파일 찾아오기




##Lookbehind assertion
#import re

#p = re.compile("(?<=abc)def")
#m = p.search("abcdef")
#print(m.group())




##매치되는 스트링의 시작과 끝 위치의 인덱스를 반환 : start() / end()
#import re 

#email = "tony@tiremove_thisger.net"
#m = re.search("remove_this", email)
#result = email[:m.start()] + email[m.end():]
#print("start() : ", m.start())
#print("end() : ", m.end())
#print(result)




##Making a Phonebook
#text = """"Ross: McFluff: 834.345.1254: 155 Elm Street
#Ronald: Heathmore: 892.345.3428 436: Finley Avenue
#Frank: Burger: 925.541.7625 662: South Dogwood Way
#Heather: Albrecht: 548.326.4584 919: Park Place"""

#entries = re.split("\n", text)
#result = [re.split(":?", entry, 4) for entry in entries]
#print(result)




#Urllib.request : Url 을 오픈하기 위한 라이브러리
import urllib.request
import re

with urllib.request.urlopen("http://www.python.org/") as f:
    print(f.read())
    print(f.read(300))


    str = print(f.read(300).decode("utf-8"))
    m = re.search(r'<title>(.*)</title>', str).group()
    print(m)
    #타이틀에 해당하는 것만 뽑아내보기..........................근데 이 시간에 나는 몬했음.