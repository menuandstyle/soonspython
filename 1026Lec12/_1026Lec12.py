#����ǥ����2.pdf




##findall  �̿��ϱ�
#import re

#str = """Window
#Unix
#Linux
#Solaris"""   #��Ƽ�������� ���ڿ��� �־�����. ���ӵ� �����ο��ȣ �� �� (""") �̿�
#p = re.compile('^.+', re.M) #M �� �־��� ����, Multiline ��Ƽ���ο� �ش��ϴ� �÷��� ��
#print(p.fildall(str))




##group �� �̸� �����ϱ�
#import re

#m = re.match(r"(?P<first_name>\w+) (?P<last name>\w+)", "Malcolm Reynolds")
#print(m.group('first_name', 'last_name'))
#print(m.groups())




##group �� ����Ʈ�� �ֱ�
#import re

#m = re.match(r"(\d+)\.?(\d+)?", "24")
#print(m.groups())
#print(m.group(0))




##group �� dictionary �� ����ϱ�
#import re

#m = re.match(r"(?P<first_name>\w+) <?P<last_name>\w+)", "Malcolm Reynolds")
#print(m.groupdict())




##Lookahead assertion 
#import re

##p = re.compile(".+:")
#p = re.compile(".+(?=:)")   #�ݷп� �ش��ϴ� �� �����, �ݷп� �ش��ϴ� �� �տ� �� ������ ��������� �ְڴ�, ��� �ϴ� ���
#m = p.search("http://google.com")
#print(m.group())




##���� ���丮�� c ���丮�� �Űܺ���
#import os
#import re
#import glob
#os.chdir('C;/Python34/')  #chdir : ���� ���� ������ �̵�
#glob.glob("*") #glob : ���� ���丮�� �ִ� ���� ã�ƿ���




##Lookbehind assertion
#import re

#p = re.compile("(?<=abc)def")
#m = p.search("abcdef")
#print(m.group())




##��ġ�Ǵ� ��Ʈ���� ���۰� �� ��ġ�� �ε����� ��ȯ : start() / end()
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




#Urllib.request : Url �� �����ϱ� ���� ���̺귯��
import urllib.request
import re

with urllib.request.urlopen("http://www.python.org/") as f:
    print(f.read())
    print(f.read(300))


    str = print(f.read(300).decode("utf-8"))
    m = re.search(r'<title>(.*)</title>', str).group()
    print(m)
    #Ÿ��Ʋ�� �ش��ϴ� �͸� �̾Ƴ�����..........................�ٵ� �� �ð��� ���� ������.