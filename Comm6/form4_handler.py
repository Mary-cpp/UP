from bottle import post, request, template
import math
from datetime import datetime

@post('/time_series', method='post')
def my_form():
    row1 = request.forms.get('X')
    row2 = request.forms.get('Y')
    x = []
    y = []
    x1 = list(row1.split(' '))
    y1 = list(row2.split(' '))
    #рассчет показателей ряда
    avRowLvlX = avRowLvl(x1)
    avRowLvlY = avRowLvl(y1)
    abtcX = AbsGrwthTempC(x1)
    abtcY = AbsGrwthTempC(y1)
    abtbX = AbsGrwthTempB(x1)
    abtbY = AbsGrwthTempB(y1)
    aagX = avAbsGrowth(x1)
    aagY = avAbsGrowth(y1)
    gtbX = GrwthTempC(x1)
    gtbY = GrwthTempC(y1)
    gtcX = GrwthTempB(x1)
    gtcY = GrwthTempB(y1)
    agtbX = avGrwthTempB(x1)
    agtbY = avGrwthTempB(y1)
    agtcX = avGrwthTempC(x1)
    agtcY = avGrwthTempC(y1)
    for i in range(len(x1)):
        x.append(x1[i])
        y.append(y1[i])
    #Заносим все параметры в массив, для вывода на страницу сайта
    arr = (x, y, avRowLvlX, avRowLvlY, abtcX, abtcY, abtbX, abtbY, aagX, aagY, gtbX, gtbY, gtcX, gtcY, agtbX, agtbY, agtcX, agtcY)
    return template('task4.tpl', title='Time Series', year=datetime.now(), title2 ='Enter the number series', message = 'Task Statement:', output = arr)

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
    agtc = []
    for i in range(len(list)):
        if i == 0:
            count = 0
            agtc.append(count)
        else:
            count = int(list[i])-int(list[i-1])
            agtc.append(count)
            print('Abcolute Chain Increment[%a]: %a' % (i,count) , end='\n')
    return agtc

#Абсолютный прирост базисный
def AbsGrwthTempB(list):
    count = 0
    agtb = []
    for i in range(len(list)):
        if i == 0:
            count = 0
            agtb.append(count)
        else:
            count = int(list[i])-int(list[0])
            agtb.append(count)
            print('Abcolute Basis Increment[%a]: %a' % (i,count) , end='\n')
    return agtb

#Темп роста базисный
def GrwthTempB(list):
    count = 0
    gtb = []
    for i in range(len(list)):
        if i == 0:
            count = 1*100
            gtb.append(count)
            print('Basis Increment[%a]: %a ' % (i+1,count) , end='\n')
        else:
            count = (int(list[i])/int(list[0]))*100
            gtb.append(count)
            print('Basis Increment[%a]: %a ' % (i+1,count) , end='\n')
    return gtb

#Темп роста цепной
def GrwthTempC(list):
    count = 0
    gtc = []
    for i in range(len(list)):
        if i == 0:
            count = 1
            gtc.append(count)
            print('Chain Increment[%a]: %a' % (i+1,count) , end='\n')
        else:
            count = int(list[i])/int(list[i-1])*100
            gtc.append(count)
            #ДОБАВИТЬ ПРОЦЕНТЫ!!!!
            print('Chain Increment[%a]: %a' % (i+1,count) , end='\n')
    return gtc

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
    return agtb1

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
    return agtb1

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
    print ('Summ of th row = %a' %(summ), end='\n')

#Сумма X*I
def mult(lista, listb):
    m = 0
    for i in range(len(lista)):
        m += float(lista[i])*float(listb[i])
    print ('Result of the rows X & Y multiplication = %a' %(m), end='\n')

#Сумма x^2
def sum2(list):
    sum = 0
    for i in range (len(list)):
        sum += math.pow(float(list[i]),2)
    print ('squared summ of th row = %a' %(sum), end='\n')

#Коэффициент а2
def a2(lista, listb):
    a2 = (summ(listb)*summ(lista)-len(list)*mult(lista,listb))/(mat.pow(sum(lista),2)-len(list)*sum2(lista))

#Коэффициент а1
def a1(lista,listb):
    a1 =(summ(lista)-a2(lista,listb)*summ(lista))/len(lista)

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





