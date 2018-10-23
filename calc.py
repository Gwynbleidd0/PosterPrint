import math
color=[[35,32,30,29,28,24],[50,48,46,45,43,40],[20,18,15,14,12,11],[40,35,30,28,22,20],[45,40,38,37,33,30]]
paper=[2,3,4,5,6,7,8,25]
rezka=[0,40,60,80,100,120,200]

price=0
#count_lists=int(input('Введите количество листов:\n'))
#count_lists=count_lists/2+0.1
#count_lists=round(count_lists)
#print(count_lists)
rezka_answer=int(input('Выберите формат бумаги\n1)A4(2 части)\n2)А5(4 части)\n3)99*210(6 частей)\n4)А6(8 частей)\n5)10 частей\n6)А7(16 частей)\n7)визитка5*9(30 частей)\n'))
count_lists=int(input('Введите количество листов:\n'))
if rezka_answer==1:
    count_lists=count_lists/2
if rezka_answer==2:
    count_lists=count_lists/4
if rezka_answer==3:
    count_lists=count_lists/6
if rezka_answer==4:
    count_lists=count_lists/8
if rezka_answer==5:
    count_lists=count_lists/10
if rezka_answer==6:
    count_lists=count_lists/16
if rezka_answer==7:
    count_lists=count_lists/30
count_lists=math.ceil(count_lists)
print(count_lists)
color_per=int(input('Выберите количество цветов:\n1)Цветная+Пустая\n2)Цветная+Цветная\n3)Черно-белая+Пустая\n4)Черно-белая+Черно-белая\n5)Цветная+Черно-белая\n'))
t=0
if (count_lists>5) and (count_lists<10):
    t=1
if (count_lists>=10) and (count_lists<50):
    t=2
if (count_lists>=50) and (count_lists<100):
    t=3
if (count_lists>=100) and (count_lists<250):
    t=4
if (count_lists>=250):
    t=5
price=price+color[color_per-1][t]*count_lists
paper_plot=int(input('Выберите плотность бумаги:\n1)130гр/м\n2)150гр/м\n3)170гр/м\n4)200гр/м\n5)250гр/м\n6)300гр/м\n7)350гр/м\n8)самоклейка\n'))
price=price+paper[paper_plot-1]*count_lists
#rezka_answer=int(input('Выберите формат бумаги\n1)A4(2 части)\n2)А5(4 части)\n3)99*210(6 частей)\n4)А6(8 частей)\n5)10 частей\n6)А7(16 частей)\n7)визитка5*9(30 частей)\n'))
price=price+rezka[rezka_answer-1]
print('Итоговая цена:'+str(price)+' руб')
