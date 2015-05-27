# -*- coding: utf-8 -*-
import math
import random
import sys
#求最大值的函数
#f(x) = 10 * sin( 5x ) + 7 * cos( 4x ) x in [0,10]
#refer：http://blog.csdn.net/u010902721/article/details/23531359
def b2d(b): #二进制转十进制
    t = 0
    for j in range(len(b)):
        t += b[j] * (math.pow(2, j))
    t = t * 10 /1023
    return t



def calobjvalue(pop): #计算目标函数值
    def decodechrom(pop):
        temp = []
        for i in range(len(pop)):
            t = b2d(pop[i])
            temp.append(t)
        return temp

    #temp1 = []
    objvalue = []
    temp1 = decodechrom(pop)
    for i in range(len(temp1)):
        x = temp1[i]
        objvalue.append(10 * math.sin(5 * x) + 7 * math.cos(4 * x))
    return objvalue

def calfitvalue(objvalue): #转化为适应值
    fitvalue = []
    temp = 0.0
    cmin = 0
    for i in range(len(objvalue)):
        if(objvalue[i] + cmin > 0):
            temp = cmin + objvalue[i]
        else:
            temp = 0.0
        fitvalue.append(temp)
    return fitvalue

def best(pop, fitvalue):#找出适应函数值中最大值，和对应的个体
    bestindividual = []
    bestfit = fitvalue[0]
    for i in range(1,len(pop)):
        if(fitvalue[i] > bestfit):
            bestfit = fitvalue[i]
            bestindividual = pop[i]
    return [bestindividual, bestfit]

def selection(pop, fitvalue): #自然选择
    def sum(fitvalue):
        total = 0
        for i in range(len(fitvalue)):
            total += fitvalue[i]
        return total

    def cumsum(fitvalue):
        for i in range(len(fitvalue)):
            t = 0
            j = 0
            while (j <= i):
                t += fitvalue[j]
                j = j + 1
            fitvalue[i] = t
    newfitvalue = []
    totalfit = sum(fitvalue)
    for i in range(len(fitvalue)):
        newfitvalue.append(fitvalue[i] / totalfit) #to-do:ZeroDivisionError
    cumsum(newfitvalue)
    ms = []
    for i in range(len(pop)):
        ms.append(random.random())
    ms.sort()
    fitin = 0
    newin = 0
    newpop = pop
    while newin < len(pop):
        if(ms[newin] < newfitvalue[fitin]):
            newpop[newin] = pop[fitin]
            newin = newin + 1
        else:
            fitin = fitin + 1
    pop = newpop

def crossover(pop, pc): #个体间交叉，实现基因交换
    for i in range(len(pop) - 1):
        if(random.random() < pc):
            cpoint = random.randint(0, len(pop[0]))
            temp1 = []
            temp2 = []
            temp1.extend(pop[i][0 : cpoint])
            temp1.extend(pop[i+1][cpoint : len(pop[i])])
            temp2.extend(pop[i+1][0 : cpoint])
            temp2.extend(pop[i][cpoint : len(pop[i])])
            pop[i] = temp1
            pop[i+1] = temp2

def mutation(pop, pm): #基因突变
    for i in range(len(pop)):
        if(random.random() < pm):
            mpoint = random.randint(0,len(pop[0])- 1)
            if (pop[i][mpoint] == 1):
                pop[i][mpoint] = 0
            else:
                pop[i][mpoint] = 1

def ga(generation, pop, pc, pm, popsize): #遗传算法
    results = []
    bestindividual = []
    bestfit = 0
    fitvalue = []
    for i in range(generation):
        objvalue = calobjvalue(pop) #计算目标函数值
        fitvalue = calfitvalue(objvalue) #计算个体适应值
        [bestindividual, bestfit] = best(pop, fitvalue) #选出最好个体和函数值
        results.append([bestfit, b2d(bestindividual)])#保存每次繁殖最好结果
        selection(pop, fitvalue) #自然选择, 优胜劣汰
        crossover(pop, pc) #交叉繁殖
        mutation(pop, pm) #基因突变
    return results

if __name__=='__main__':
    popsize = 100 #种群数量
    generation = 1000 #繁殖代数
    chromlength = 10 #基因长度
    pc = 0.6 #个体交叉概率
    pm = 0.05 #基因突变概率
    pop = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1] for i in range(popsize)]
    results = ga(generation, pop, pc, pm, popsize)
    results.sort() 
    print "y = %r, x = %r" % (results[-1][0], results[-1][1])#打印最佳值