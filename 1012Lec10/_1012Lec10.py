import pickle
import shutil
import glob, os.path

import os
import sys
#os.system("python test.py a b c")
#print(sys.argv)

##예외 처리에서 다음 강제 스크립트 종료법도 잘 쓰인다.
##sys.exit()

#print(sys.path)

#class Student:
#    def __init__(self, name, age):
#        self.name = name;
#        self.age = age;
#    def show(self):
#        print(self.name, " : ", self.age)

#stu = Student("greenjoa", 23) #Student 클래스의 객체를 하나 생성
#stu.show()




##여기서부터는 pickle.dump 로 저장하고 pickle.load 로 불러오는 방법을 써본다.
#f = open("test.txt", 'wb')
#data = {1: 'python', 2: 'you need'}
#pickle.dump(data, f)
#f.close()
#f = open("test.txt", 'rb')
#data = pickle.load(f)
#print(data)




#print(os.environ)




#현재 디렉토리의 부모 디렉토리를 가고 싶다.
#os.chdir('cd ..')   #이거 맞나?

#for (path, dir, files) in os.walkr('.'):
#    for filename in files:
#        print(file.name)

#현재 디렉토리에서 하위 디렉토리까지 .txt 라는 파일만 골라 복사를 해서 현재 디렉토리에 sample 이라는 디렉토리를 만들고 그 안에 넣는다.
#os.mkdir("sample")  #일단 현 디렉토리에 sample 디렉토리를 만들고
#all = glob.glob("*")  #현재 디렉토리에 있는 파일중 전체를찾아서
#os.chdir("sample")  #sample 디렉토리로 현 위치를 변경하고
#shutil.copy("test.txt", "sample")   #all 리스트 안의 파일들을 복사해준다.
#윗줄들은 내가 만들어본 건데 실패.

#dirname(path) : 입력받은 파일이나 디렉토리의 경로를 반환

#glob 는 find 구문처럼 사용
#print(glob.glob('*.py'))
#print(glob.glob('??.*'))

#11 페이지 예제
#ndir = nfile = 0
#def traverse(dir, depth):
#    global ndir, nfile
#    for obj in glob.glob(dir + '/*'):
#        if depth == 0:
#        prefix = '|--'
#    else:
#        prefix = '|' + ' ' * depth + '|--'
#    if os.path.isdir(obj):
#        ndir += 1
#        print(prefix + os.path.basename(obj))
#        traverse(obj, depth+1)
#    elif os.path.isfile(obj) :
#        nfile +=1
#        print(prefix + os.path.basename(obj))
#    else:
#        print(prefix + 'unknown object:',obj)

#if __name__ == '__main__':
#    traverse('..', 0)
#    print('\n',ndir,'directories,',nfile, 'files')


import tempfile
with tempfile.TemporaryFile('w+') as fp:    #생성된 파일명 : fp.name
    fp.write('Hello world!')
    fp.seek(0)
    data = fp.readable()
    print(data)
    
import time
#t1 = time.time()
#time.sleep(10)
#t2.time.time()
#spendtime=t2-t1
#print(spendtime)
#시간 형식을 내가 원하는 형식으로 만들 수 있어야 한다.
#원하는 형식으로 시간을 만드는 게 시험에 나오는 것 같다.
print(time.strftime("%y %B %d %A %p %H", time.localtime()))

import calendar
calendar.calendar(1992)
calendar.prcal(1992)
print(calendar.weekday(1992,6,17))

import random
print(random.sample(range(1000), 5))
#0 부터 100까지의 수에 해당하는 난수 열 개를 골라서 그것을 섞어서 하나를 골라보자.
alls = random.sample(range(100), 10)
ii = random.sample(range(10), 1)
ii = ii[0]-1;
print(alls[ii])

data = [('Red', 3), ('Blue', 1), ('Green', 4), ('Yellow', 2)]
datalist = []
#Red 를 3 번, Blue 를 1 번, Green 을 4 번, Yellow 를 2 번 append 해서 출력해보자
for val, cnt in data:
    #cnt 만큼 val 를 append 하면 된다
    for i in range(cnt):
        datalist.append(val)       
print(datalist)

import webbrowser
url = 'http://google.com'
webbrowser.open_new_tab(url)

#여기까지가 중간고사 범위!