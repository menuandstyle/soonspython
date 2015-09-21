#class Service:
#    secret = "영구는 배꼽이 두 개다"
#    def sum(self, a, b):
#        result = a+b
#        print("%s + %s = %s 입니다." %(a, b, result))
#pey = Service()
#print(pey.secret)




class Movie:
    count = 0
    title="글래디에이터"
    director="리들리 스콧"
    def __init__(self, title, director):
        self.title = title
        self.director = director
        #self.count+=1
        Movie.count+=1
        print(self.title + "생성자 호출")

    def __del__(self):
        print(self.title + "소멸자 호출")

    def showInfo(self):
        print(self.title + " " + self.director)

    @staticmethod
    def showCount1():
        print(Movie.count)

    @staticmethod
    def showCount2(cls):    #cls: CLaSs
        print(cls.count)

#m1 = Movie("베테랑1", "류승완1");
#m2 = Movie("베테랑2", "류승완2");
#m3 = Movie("베테랑3", "류승완3");
#m4 = Movie("베테랑4", "류승완4");
#print(type(m4))
#m4 = m3 #얕은 복사
#print(id(m4)) #id: 주소값
#print(id(m3))
#m4.showInfo()

m1 = Movie("a", "b")
m2 = Movie("c", "d")
m3 = Movie("c", "d")
m4 = Movie("c", "d")
m5 = Movie("c", "d")
Movie.showCount1()
Movie.showCount2()




#