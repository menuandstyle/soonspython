#-*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

a = {'name':'kim', 'phone':'1234567890', 'birth':'950505'}

#items()
b = a.items()
print(b)

#dictionary 안에는 dictionary 가 들어갈 수 있다.
movieStars = {'홍길동':{'베테랑':5.0, '암살':4.5},
              '고길동':{'스파이':5.0, '괴물':4.5},
              '노길동':{'전우치':3.0, '암살':4.5}}
#홍길동이 준 영화 평점만 출력해보자.
movieHong = movieStars.get('홍길동')
print(movieHong)
#홍길동은 암살에 몇 점을 주었는가.

HongsAssasin = movieHong.get('암살')
print(HongsAssasin)

##########Lec01.pdf자료형 마감##########


##########Lec02.pdf제어문 시작##########
answer = input("Would you like express shipping?")
if answer == "yes" :
    print("That will be an extra $10")