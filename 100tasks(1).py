#coding:utf-8
#we start several tasks everydaty to accomplish and strenthen what we have studied.
#the tasks source is from
# http://www.runoob.com/python/python-exercise-example1.html
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
diff = []
same = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a !=b) and (a !=c) and (b != c):
                #print (a,b,c,"different character")
                diff.append((a,b,c))
            else:
                #print (a,b,c,"contain same number")
                same.append((a,b,c))
print 'different num:' , diff
print 'same contain num:' , same



#企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？


def profit(i):
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if i > arr[idx]:
            r += (i - arr[idx]) * rat[idx]
            return (i - arr[idx]) * rat[idx]
            i = arr[idx]
            print r

q = profit(input("利润："))
print q



#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#答案网上有，今天浪一下，不想分析，

for i in range(1,85):
    if 168 % i == 0:
        j = 168 / i;
        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)
"""
#输入某年某月某日，判断这一天是这一年的第几天？
x = input("year:")
y = input("month:")
z = input("day:")
month = [1,2,3,4,5,6,7,8,9,10,11,12]
if x % 4 == 0:
    a = 29
else:
    a = 28
daylist = [31, a, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#注意，liststart from 0
if y in month and z <= daylist[y-1]:
    y = y-1
    while (y > 0):
        y = y - 1
        z += daylist[y]


    print ("this is %dth day")%z
else:
    print ("wrong date")


