#import printData

#data = ["홍길동", ["베테랑", ["류승완", "황정민", "유아인"]], "고길동", ["암살"]]
#printData.printData(data)

import os

#cwd: Current Working Directory 현재 작업디렉토리

#현재 작업디렉토리의 주소를 프린트해줌
print(os.getcwd())

#os.mkdir("sample")
os.chdir(".//sample")

#system() 이라는 함수로 시스템 명령을 내릴 수 있다.
#os.system("dir\\w")

os.system("python setup.py sdist")
os.system("python setup.py install")