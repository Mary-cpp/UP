from bottle import post, request
import math

@post('/time_series', method='post')
def my_form():
    x = request.forms.get('X')
    y = request.forms.get('Y')
    row1 = list(x.split(' '))
    row2 = list(y.split(' '))
    #return "Thanks! The answer will be sent to the mail %s" % avGrwthTemp(row)
    return a2(row1,row2)

#Средний уровень ряда 
def avRowLvl(list):
    sum = 0
    i = 0
    k = 0
    for i in range(len(list)):
        sum+= int(list[i])
        k+=1
    avRowLvl = sum/k
    return avRowLvl

#Средний абсолютный прирост
def avAbsGrowth(list):
    k = 0
    lenghth = len(list)
    first = int(list[0])
    last = int(list[lenghth-1])
    for i in range(len(list)):
        k+=1
    avAbsGrowth = (last-first)/(k-1)
    return avAbsGrowth

#Абсолютный прирост цепной
def AbsGrwthTempC(list):
    count = 0
    for i in range(len(list)):
        if i == 0:
            count = 0
        else:
            count = int(list[i])-int(list[i-1])
            print('Abcolute Chain Increment[%a]: %a' % (i,count) , end='\n')

#Абсолютный прирост базисный
def AbsGrwthTempB(list):
    count = 0
    for i in range(len(list)):
        if i == 0:
            count = 0
        else:
            count = int(list[i])-int(list[0])
            print('Abcolute Basis Increment[%a]: %a' % (i,count) , end='\n')

#Темп роста базисный
def GrwthTempB(list):
    count = 0
    for i in range(len(list)):
        if i == 0:
            count = 1*100
            print('Basis Increment[%a]: %a ' % (i+1,count) , end='\n')
        else:
            count = (int(list[i])/int(list[0]))*100
            #ДОБАВИТЬ ПРОЦЕНТЫ!!!
            print('Basis Increment[%a]: %a ' % (i+1,count) , end='\n')

#Темп роста цепной
def AbsGrwthTempC(list):
    count = 0
    for i in range(len(list)):
        if i == 0:
            count = 1
            print('Chain Increment[%a]: %a' % (i+1,count) , end='\n')
        else:
            count = int(list[i])/int(list[i-1])*100
            #ДОБАВИТЬ ПРОЦЕНТЫ!!!!
            print('Chain Increment[%a]: %a' % (i+1,count) , end='\n')

#Средний темп роста базисный
def avGrwthTempB(list):
    count = 0
    k = 0.0
    agtb = 1
    agtb1 = 0
    for i in range(len(list)):
        if i == 0:
            count = 1*100
            agtb = count * agtb
            k+=1
        else:
            count = (int(list[i])/int(list[0]))*100
            agtb = count * agtb
            k+=1
    agtb1 = pow(agtb,1.0/k)
    print("Average Growth Basis Temp = ", agtb1  , end='\n')

#Средний темп роста цепной
def avGrwthTempC(list):
    count = 0
    k = 0.0
    agtb = 1
    agtb1 = 0
    for i in range(len(list)):
        if i == 0:
            count = 0
            agtb = count * agtb
            k+=1
        else:
            count = (int(list[i])/int(list[i-1]))*100
            agtb = count * agtb
            k+=1
    agtb1 = pow(agtb,1.0/k)
    print("Average Growth Basis Temp = ", agtb1  , end='\n')

#Темп прироста цепной
def GrwthRateC(list):
    grwthRate = 0.0
    count = 0
    for i in range(len(list)):
        if i == 0:
            count = 0
            print('Abcolute Chain Growth[%a]: %a' % (i+1,grwthRate) , end='\n')
        else:
            count = int(list[i])-int(list[i-1])
            grwthRate = (count/float(list[i]))*100
            print('Abcolute Chain Increment[%a]: %a' % (i,grwthRate) , end='\n')

#Темп прироста базисный
def GrwthRateB(list):
    grwthRate = 0.0
    count = 0.0
    for i in range(len(list)):
        if i == 0:
            count = 0
            print('Abcolute Basis Growth[%a]: %a' % (i+1,grwthRate) , end='\n')
        else:
            count = float(list[i])-float(list[0])
            grwthRate = (count/float(list[i]))*100
            print('Abcolute Basis Growth[%a]: %a' % (i+1,grwthRate) , end='\n')

#Колеблемость

#===========================================================================================
#Вспомогательные вычисления

#Сумма значений 
def summ(list):
    summ = 0
    for i in range(len(list)):
        summ+=int(list[i])

#Сумма X*I
def mult(lista, listb):
    m = 0
    for i in range(len(lista)):
        m += float(lista[i])*float(listb[i])

#Сумма x^2
def sum2(list):
    sum = 0
    for i in range (len(list)):
        sum += math.pow(float(list[i]),2)

#Коэффициент а2
def a2(lista, listb):
    a2 = (summ(listb)*summ(lista)-len(list)*mult(lista,listb))/(mat.pow(sum(lista),2)-len(list)*sum2(lista))
    return a2

#Коэффициент а1
def a1(lista,listb):
    a1 =(summ(lista)-a2(lista,listb)*summ(lista))/len(lista)
    return a1

#Среднеквадратичное отклонение
def sqro(lista, listb):
    y = 0.0
    y2 = 0.0
    summ = 0
    for i in range(len(lista)):
        y = a1(lista,listb) + a2(lista,listb)*float(lista[i])
        y2 = math.pow((float(listb[i])-y),2)
        summ += y
    sqro = math.pow((summ-(len(list)-2)),1/2)

#Колеблемость
def vol(lista,listb):
    vol = (sqro(lista, listb)/avRowLvl(listb))*100
    print ('Колеблемость ряда = %a ' %a (vol), end = '\n')





