number = [1,2,3,4,5,6,7,8,9]

for i in number :
    print(2*i)


for i in range(10):
    print(i)

for i in range(2,20):
    print(i)

for a in range(2,20):
    for b in range(2,20):
        print(a, "X", b, "=", a*b)

for a in range(2,20):
    for b in range(2,20):
        print('%d X %d = %d' %(a,b, a*b))


print('나는 사과를 %d개 먹었습니다' %2)
print('나는 사과를 %d개 먹고, 배는 %d개 먹었습니다' %(2,3))