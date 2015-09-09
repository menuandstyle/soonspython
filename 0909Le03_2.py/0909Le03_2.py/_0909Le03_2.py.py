#if 문에서 처리할 내용이 한 줄일 경우
pocket = ['paper', 'money', 'smartphone']
if 'money' in pocket: print("현금영수증을 부탁하지요")

#구구단 출력하기
#보통 print() 를 하면 줄바꿈이 되지만,
#end=" " 를 하면 줄바꿈이 되지 않는다.
for i in range(2, 10):
    for j in range(1, 10):
        #숫자와 문자열을 다 함께 출력하는 방법을 알아야 한다.
        #아래 문장은 더없이 중요하다.
        print('%d * %d = %2d'% (i, j, i*j))
    print("")

#turtle
import turtle
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)

nSides = 7
for steps in range(nSides) :
    turtle.forward(100)
    turtle.right(360/nSides)
    for moresteps in range(nSides) :
        turtle.forward(50)
        turtle.right(360/nSides)