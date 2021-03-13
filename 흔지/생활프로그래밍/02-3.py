y = lambda x : 3*x
print(y(12))

add = lambda a,b : a+b
print(add(2,3))

LittlePrince = '''여섯 살 적에 나는 '체험한 이야기'라는 제목의, 원시림에 관한 책에서 기막힌 그림 하나를 본 적이 있따. 맹수를 집어삼키고 있는 보아뱀 그림이었다. 위의 그림은 그것을 옮겨 그린 것이다. 그 책에는 이렇게 씌어 있었다.'''
print(LittlePrince[:10])
short=lambda x : x[:10]
print(short(LittlePrince))

def add(a,b):
    return a+b
print(add(1,2))

def calculator(a,b):
    return a+b, a-b, a*b, a/b
print(calculator(12,3))
print(type(calculator(12,3)))

c = 17/7
print(type(c))
print(round(c,1))

for i in [1,2,3,4,5,6,7,8,9]:
    if i%2 ==0 :
        print(i, '짝수')
    else:
        print(i,'홀수')

for a in [1,2,3,4,5,6,7,8,9]:
    if a%2 is not 0:
        print(a,'홀수')
    else :
        print(a,'짝수')



def service_price():
    service = input('서비스의 종류를 입력하세요, a/b/c:')
    valueAdded = input('부가세를 포함합니까? y/n :')
    if valueAdded == 'y':
        if service == 'a':
            result = 23 *1.1
        if service == 'b':
            result = 40*1.1
        else :
            result = 67*1.1
    else :
        if service == 'a':
            result = 23
        if service == 'b':
            result = 40
        else :
            result = 67
    print(round(result,1), '만 원입니다.')
service_price()

def addPrint(a,b):
    print(a+b)
def addReturn(a,b):
    return(a+b)
print('The result is', addPrint(1,2))
print('The result is', addReturn(3,4))


#연습문제01
14%4