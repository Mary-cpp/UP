from bottle import post, request
import math

@post('/time_series', method='post')
def my_form():
    x = request.forms.get('X')
    y = request.forms.get('Y')
    row1 = list(x.split(' '))
    row2 = list(y.split(' '))
    #return "Thanks! The answer will be sent to the mail %s" % avGrwthTemp(row)
    return avGrwthTempC(row1)

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
        summ+=list[i]

#Сумма X*I
def mult(lista, listb):
    m = 0
    for i in range(len(list)):
        m += lista[i]*listb[i]

#Сумма x^2
def sum2(list):
    sum = 0
    for i in range (len(list)):
        sum += math.pow(list[i],2)

#Коэффициент а1
def a2(lista, listb):
    a2 = (summ(row2)*summ(row1)-len(list)*mult(row1,row2))/(mat.pow(sum(row1),2)-len(list)*sum2(row1))
    return a1

#Коэффициент а1
def a1(lista,listb):
    a1 =(summ(row2)-a2(row1,row2)*summ(row1))/len(lista)


#Среднеквадратичное отклонение



