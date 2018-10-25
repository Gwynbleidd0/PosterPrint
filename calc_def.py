import math
color=[[35,32,30,29,28,24],[50,48,46,45,43,40],[20,18,15,14,12,11],[40,35,30,28,22,20],[45,40,38,37,33,30]]
paper=[2,3,4,5,6,7,8,25]
rezka=[0,40,60,80,100,120,200]
def calc_price(rezka_answer,count_lists,color_per,paper_plot,rezka,color,paper):

    price=0
    if rezka_answer=='A4(2 части)':
        count_lists=count_lists/2
    if rezka_answer=='A5(4 части)':
        count_lists=count_lists/4
    if rezka_answer=='99*210(6 частей)':
        count_lists=count_lists/6
    if rezka_answer=='А6(8 частей)':
        count_lists=count_lists/8
    if rezka_answer=='10 частей':
        count_lists=count_lists/10
    if rezka_answer=='А7(16 частей)':
        count_lists=count_lists/16
    if rezka_answer=='визитка5*9(30 частей)':
        count_lists=count_lists/30
    count_lists=math.ceil(count_lists)
    print(count_lists)
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
    #Перевод цвета
    if color_per=='Цветная+Пустая':
        color_per=1
    elif color_per=='Цветная+Цветная':
        color_per=2
    elif color_per=='Черно-белая+Пустая':
        color_per=3
    elif color_per=='Черно-белая+Черно-белая':
        color_per=4
    elif color_per=='Цветная+Черно-белая':
        color_per=5
    #Перевод плотности
    if paper_plot=='130гр/м':
        paper_plot=1
    elif paper_plot=='150гр/м':
        paper_plot=2
    elif paper_plot=='170гр/м':
        paper_plot=3
    elif paper_plot=='200гр/м':
        paper_plot=4
    elif paper_plot=='250гр/м':
        paper_plot=5
    elif paper_plot=='300гр/м':
        paper_plot=6
    elif paper_plot=='350гр/м':
        paper_plot=7
    elif paper_plot=='самоклейка':
        paper_plot=8
    #Перевод резки
    if rezka_answer=='A4(2 части)':
        rezka_answer=1
    elif rezka_answer=='А5(4 части)':
        rezka_answer=2
    elif rezka_answer=='99*210(6 частей)':
        rezka_answer=3
    elif rezka_answer=='А6(8 частей)':
        rezka_answer=4
    elif rezka_answer=='10 частей':
        rezka_answer=5
    elif rezka_answer=='А7(16 частей)':
        rezka_answer=6
    elif rezka_answer=='визитка5*9(30 частей)':
        rezka_answer=7

    price=price+color[color_per-1][t]*count_lists
    price=price+paper[paper_plot-1]*count_lists
    price=price+rezka[rezka_answer-1]
    return(str(price))
    
