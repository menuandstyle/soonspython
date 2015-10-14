#Lec08����ǥ����1.pdf
import re
pattern = re.compile("d")
result = pattern.search("dog")
print(result)
result2 = pattern.search("dog", 1)  #dog �� 1 ��° �ε������� ���϶�. ��, og �� ���϶�.
print(result2)
print("\n")


#��������� �����.
Str = '''sample1.
sample2.
sample3.''' #''' �̷��� ���� ���̶�� �� ǥ���Ѵ�.
p = re.compile('^.*$', re.M) #' ������ ' �� �ش��ϴ� �� $ ����.    #��Ƽ���ο� �ش��ϴ� M �̶� �ɼ��� �ش�.
result = p.search(Str);
print(result.group())
print("\n")


#fullmatch �� �������
pattern = re.compile("o[gh]")
result = pattern.fullmatch("dog")
print(result)
result2 = pattern.fullmatch("ogre")
print(result2)
result3 = pattern.fullmatch("doggie", 1, 3) #1��°, �׸��� 2��° �ε��� �� �� �ϰ� �񱳸� �Ѵ�.
print(result3)
print("\n")


#split �� �Ẹ��
pattern = re.compile("\W+")
result = pattern.split("words, words, words.")
print(result)
result2 = pattern.split("words, words, words.", 1)
print(result2)
print("\n")

pattern = re.compile("x*")
result = pattern.split("axbc")
print(result)
print("\n")


#sub �Ẹ�� : ���ڰ� �ƴ� �� �� ���ּ�, ���ڸ� ���Բ�
result = re.sub(r'\W','','a:b:c, d.')
print(result)
print("\n")


#Ž������ ��Ī
str =  '<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*)">', str)
print(result.group(1))
print(result)
result = re.search(r'href="(.*?)">', str)
print(result.group(1))
print(result)
print("\n")


#�ֹε�Ϲ�ȣ���� Ȯ���ϰ�, �յ޺κ��� �߶󺸱�
st = "123456-1234567"
pattern= re.compile("\d{6}-\d{7}")  #�ֹε�Ϲ�ȣ���� Ȯ���ϰ�
result = pattern.fullmatch(st)  #�յ޺κ��� �߶󺸱�
print(result)
#result2 = pattern