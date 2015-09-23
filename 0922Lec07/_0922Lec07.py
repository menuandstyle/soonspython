#from abc import ABCMeta, abstractmethod

#class Terran(metaclass=ABCMeta):
#    def __init__(self, name):
#        self.name = name

#    #공통적으로 구현해야하는 메소드는 @abstractmethod 라고 해준다.
#    @abstractmethod
#    def attack(self):
#        pass

#class Tank(Terran):
#    def __init__(self, name, demage):
#        super().__init__(name)
#        self.damage = damage
#    def attack(self):
#        print("탱크를 쏩니다.")

#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(name)
#        self.hp = hp
#    def attack(self):
#        print("총을 쏩니다.")

##Attack 이라는 전역함수
#def Attack(terran):
#    terran.attack()

#t1 = Tank("tank", 0)
#t2 = Marine("marine", 100)
##Terran 이라는 객체는 실제로 없다.
##Tank, Marine 이라는 객체는 실제한다.

##객체지향의 특성: 추상화, 은닉화, 캡슐화, 다형성
##다형성: 다양한 객체들이 하나의 명령, 하나의 메세지로 움직인다.

#tlist = [Tank("tank1", 0), Tank("tank2", 0), Marine("marine", 100)]
#for item in tlist:
#    Attack(item)
#Attack(t1)
#Attack(t2)




#list 기능은 그대로 가지고 있고, 도 가지고 있는 list 를 하나 만들고 싶습니다.
class MyList(list):
    name=""
    def __init__(self, name):
        super().__init__([])
        self.name = name
    def __str__(self):
        return self.name + ":" + super().__str__()
list1 = MyList("greenjoa")
list1.append(10)
list1.append(50)
list1.append(60)
list1.append(70)
list1.append(100)
print(list1)
print(dir(list1))   #list1 이 가질 수 있는 멤버들이 표시가 된다. 여기서 내가 넣은 것은 그것들 중 name 이란 기능밖에 없다.