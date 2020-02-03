#!/usr/bin/env python
# coding: utf-8


import openpyxl
import pandas as pd

data = pd.read_csv('data.csv', names = ['id_cl', 'month', 'id_send', 'id_rec', 'volume', 'd'], sep = '\t')
data = data.filter(items = ['id_cl', 'month', 'id_send', 'id_rec', 'volume'])   

#работаем с 'задача.xlsx' 

wb = openpyxl.load_workbook('задача.xlsx')
wb.sheetnames
sheet = wb['fc']
prognoz = []

#для каждой строки из 'задача.xlsx'  смотрим ее историю перевозок из 'data.csv'

for line in sheet['A2:C26294']:    
    contractor_id = line[0].value
    division_sender_id = line[1].value
    division_receiver_id = line[2].value
    list = [contractor_id, division_sender_id, division_receiver_id]
    
    filt = data [ data['id_cl'] == contractor_id ]
    filt = filt[ data['id_send'] == division_sender_id ]
    filt = filt[ data['id_rec'] == division_receiver_id ]
    filt = filt[ data['volume'] != 0 ] #исключаем перевозки в которых объем =0 
    filt = filt.query('month > 201500') #будем анализировать данные за последний год
    
# у нас есть данные отображающие только не нулевые перевозки за последние 7 месяцев
# смотрим сколько и в каких месяце было перевозок
    k = filt['month'].value_counts()
# Приводим данные к виду: номер месяца - количество перевозок в этом месяце
    k = str(k)
    k = k.split("\n")
    k.pop()
    stat_cl = [0, 0, 0, 0, 0, 0, 0]
    
    for ch in range(len(k)):
        l = k[ch]
        l = l.split("    ")
        l = [float(x) for x in l]
        l = [int(x) for x in l]
        
        if l[1] > 3:            #если в месяц было больше двух поставок, то оставляем значение '3'
            l[1] = 3
        else:
            l[1] = l[1]
        l[0] = l[0] - 201501
        
        stat_cl[l[0]] =  l[1]
    #print(stat_cl)
        
        
    
# получили временной ряд: номер месяца(индекс элемента списка) - кол-во перевозок в этом месяце
# т.к. значения с каждым месяцем более значимы,
# для анализа будем вычеслять "линейно взвешенное скользящее среднее",
# позволяет придать каждому элементу ряда свой коэффициент,
# считаем последние значения исходной функции более значимыми чем предыдущие
# по значению "взвешенной скользящее средней" принимаем решение будет ли поставка в следующем месяце
        
    def count(series, weights):
        result = 0.0
        weights.reverse()
        for n in range(len(weights)):
            result += series[-n-1] * weights[n]
        if result >= 0.7:
            result = 1
        else:
            result = 0
        return result
    i_prognoz = count(stat_cl, [0.05, 0.05, 0.1, 0.1, 0.2, 0.2, 0.3])
    prognoz.append(i_prognoz) # заносим полученый прогноз в список
prognoz.insert(0, 'non')
prognoz.insert(1, 'non')

#заносим полученные данные в 'задача.xlsx'
for i in range(2,26295):
    nom = ('D{}').format(i)   
    sheet[nom] = prognoz[i]
    
wb.save('задача.xlsx')




