#-*- coding: utf-8 -*-
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

a = {'name':'kim', 'phone':'1234567890', 'birth':'950505'}

#items()
b = a.items()
print(b)

#dictionary �ȿ��� dictionary �� �� �� �ִ�.
movieStars = {'ȫ�浿':{'���׶�':5.0, '�ϻ�':4.5},
              '��浿':{'������':5.0, '����':4.5},
              '��浿':{'����ġ':3.0, '�ϻ�':4.5}}
#ȫ�浿�� �� ��ȭ ������ ����غ���.
movieHong = movieStars.get('ȫ�浿')
print(movieHong)
#ȫ�浿�� �ϻ쿡 �� ���� �־��°�.

HongsAssasin = movieHong.get('�ϻ�')
print(HongsAssasin)

##########Lec01.pdf�ڷ��� ����##########


##########Lec02.pdf��� ����##########
answer = input("Would you like express shipping?")
if answer == "yes" :
    print("That will be an extra $10")