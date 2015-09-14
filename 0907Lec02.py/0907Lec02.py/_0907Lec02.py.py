data=['a', 'b', 'c', ['abcd', 'efg']]
#�迭�� ù ���� 0, �迭�� ������ ���� -1 �� ���ڸ� ������.
print(data[0])
print(data[-1])

#efg ����ϱ�
print(data[3][-1])

b=[1, 2, 3]
c=['Life', 'is', 'too', 'short']
f=b+c
#�迭�鳢�� ���ϱ�
print(b+c)
print(f)
#�迭�� ��� ���ϱ�
print(b*3)

#����Ʈ ����
guests = ['a','b','c','d']
guests[0] = 'greenjoa'
guests[1] = ['greenjoa1', 'greenjoa2']
guests[1:2] = ['greenjoa1', 'greenjoa2']
print(guests)

#2�� �ε����� 'e' ����
guests.insert(2, 'e')
print(guests)

#guests �迭���� 'c' ����
guests.remove('c')
print(guests)

#ù��° �� �� ����
del guests[0]
print(guests)

#�ε��� ���, �ش� ���� �ִ� �ε����� ������ ���� �߻�
print(guests.index('d'))

#���̵� ���� �� �� �ִ� ����Ʈ
idlist = ['id0', 'id1', 'id2']

#�н����� ���� �� �� �ִ� ����Ʈ
passlist = ['pass1', 'pass2', 'pass3']

#���̵�� �н����带 ���ϱ�
list0 = idlist + passlist
print(list0)

#����Ʈ ��� ������ �ϱ�, ����,
#������ ������ �ȵȴ�. �׻� �鿩���⸦ ���־�� for ���� ���̶�� �� �˰� �ȴ�.
#���̽㿡���� �鿩���Ⱑ �ʹ��ʹ�, �����ʹ�, ��¥�����ʹ����� �߿��ϴ�. ���̽㿡���� {} �� ���� �����̴�.
#��, �׸��� for ���� ������ ������ �ݷ� : �� ����.
for steps in list0 :
    print(steps)
for steps in range(6) :
    print(list0[steps])

#sort �� reverse
scores = [85, 62, 63, 45, 90]
scores.sort()
print(scores)
scores.reverse()
print(scores)

#���� �ټ� ���� ������ �̾� ���ο� �迭�� �����, ����ϱ�
# ( ž���̺긦 ����� �迭�� ����ϱ� )
nEntries = len(scores)
newsc = [1, 1, 1, 1, 1]
for steps in range(nEntries) :
    newsc[steps] = scores[steps]
print(newsc)

#isinstance �Լ� ����
for steps in data :
    if isinstance(steps, list) : #steps �� list ��? �´ٸ� if ���� �����ϰ�,
        for step in steps :
            print(step)
    else :
        print(steps)

#extend ����ϱ� : ����Ʈ�� ���ϴ� �Լ�
scores.extend([50, 60])
print(scores)
#append �� extend ����������?
scores.append([50, 60])
print(scores)

#����Ʈ�� Ʃ���� ���� : Ʃ���� ������ �� �ȴ�.
