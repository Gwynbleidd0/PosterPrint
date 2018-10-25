import vk_api
import calc_def
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def main():
    """ Пример использования longpoll
        https://vk.com/dev/using_longpoll
        https://vk.com/dev/using_longpoll_2
    """
    
#    vk_session = vk_api.VkApi(token = 'aeb7a7e62e220a95cf2c76702cf1b9c50735ab93b688a95a203c98c678e3d60d48ec521967c551a9c7b40')
#    vk_session = vk_api.VkApi(token = '973e44f4661ce7e6f56115203bdf7cffe2904eb0e6e29936ded6ee3a5055545e1e3dc2c4f834d19c7a881') 
    vk_session = vk_api.VkApi(token = 'aeb7a7e62e220a95cf2c76702cf1b9c50735ab93b688a95a203c98c678e3d60d48ec521967c551a9c7b40')
    vk = vk_session.get_api()
    user_id_d={}
    user_id_td={}
    user_id_t={}
    user_id_t2={}
    user_id_t3={}
    user_id_t4={}
    user_id_rezka={}
    user_id_countlist={}
    user_id_color={}
    user_id_plotnost={}
    user_id_price={}
    user_id_zakaz={}
    keyboard1 = VkKeyboard()
    keyboard1.add_button('Посчитать заказ', color=VkKeyboardColor.DEFAULT)
    keyboard1.add_line()  # Переход на вторую строку
    keyboard1.add_button('Информация', color=VkKeyboardColor.NEGATIVE)
    keyboard2 = VkKeyboard(one_time=True)
    keyboard2.add_button('A4(2 части)', color=VkKeyboardColor.DEFAULT)
    keyboard2.add_button('А5(4 части)', color=VkKeyboardColor.DEFAULT)
    keyboard2.add_button('99*210(6 частей)', color=VkKeyboardColor.DEFAULT)
    keyboard2.add_button('А6(8 частей)', color=VkKeyboardColor.DEFAULT)
    keyboard2.add_line()  # Переход на вторую строку
    keyboard2.add_button('10 частей', color=VkKeyboardColor.DEFAULT)
    keyboard2.add_button('А7(16 частей)', color=VkKeyboardColor.DEFAULT)
    keyboard2.add_button('визитка5*9(30 частей)', color=VkKeyboardColor.DEFAULT)
    keyboard3 = VkKeyboard(one_time=True)
    keyboard3.add_button('Цветная+Пустая', color=VkKeyboardColor.DEFAULT)
    keyboard3.add_button('Цветная+Цветная', color=VkKeyboardColor.DEFAULT)
    keyboard3.add_line()
    keyboard3.add_button('Черно-белая+Пустая', color=VkKeyboardColor.DEFAULT)
    keyboard3.add_button('Черно-белая+Черно-белая', color=VkKeyboardColor.DEFAULT)
    keyboard3.add_button('Цветная+Черно-белая', color=VkKeyboardColor.DEFAULT)
    keyboard4 = VkKeyboard(one_time=True)
    keyboard4.add_button('130гр/м', color=VkKeyboardColor.DEFAULT)
    keyboard4.add_button('150гр/м', color=VkKeyboardColor.DEFAULT)
    keyboard4.add_button('170гр/м', color=VkKeyboardColor.DEFAULT)
    keyboard4.add_button('200гр/м', color=VkKeyboardColor.DEFAULT)
    keyboard4.add_line()  # Переход на вторую строку
    keyboard4.add_button('250гр/м', color=VkKeyboardColor.DEFAULT)
    keyboard4.add_button('300гр/м', color=VkKeyboardColor.DEFAULT)
    keyboard4.add_button('350гр/м', color=VkKeyboardColor.DEFAULT)
    keyboard4.add_button('самоклейка', color=VkKeyboardColor.DEFAULT)
    keyboard5 = VkKeyboard(one_time=True)
    keyboard5.add_button('Добавить к заказу', color=VkKeyboardColor.DEFAULT) 
    keyboard5.add_button('Посчитать итоговую стоимость', color=VkKeyboardColor.DEFAULT)
    keyboard5.add_line()
    keyboard5.add_button('Посмотреть заказ', color=VkKeyboardColor.DEFAULT)
    keyboard5.add_button('Удалить позицию', color=VkKeyboardColor.DEFAULT)            
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            print('Текст: ', event.text)
            if event.text=='Начать':
                vk.messages.send(user_id=event.user_id,message='Тест 1.',keyboard=keyboard1.get_keyboard())
                user_id_d[event.user_id]=0
                user_id_t[event.user_id] = False
                user_id_t2[event.user_id]=False
                user_id_t3[event.user_id]=False
                user_id_t4[event.user_id]=False
                user_id_rezka[event.user_id]=0
                user_id_countlist[event.user_id]=0
                user_id_color[event.user_id]=0
                user_id_plotnost[event.user_id]=0
                user_id_zakaz[event.user_id]=[]
            if event.text=='Информация':
                vk.messages.send(user_id=event.user_id,message='Тест 1.',keyboard=keyboard1.get_keyboard())
            if event.text=='Удалить позицию':
                vk.messages.send(user_id=event.user_id,message='Введите номер пункта')
                user_id_d[event.user_id] = event.message_id
                user_id_td[event.user_id]=True
            if (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_td.get(event.user_id,False):
                delete_number=int(event.text)
                if delete_number==1:
                    user_id_zakaz[event.user_id][0]=''
                    user_id_zakaz[event.user_id][1]=0
                elif delete_number==2:
                    user_id_zakaz[event.user_id][2]=''
                    user_id_zakaz[event.user_id][3]=0
                elif delete_number==3:
                    user_id_zakaz[event.user_id][4]=''
                    user_id_zakaz[event.user_id][5]=0
                elif delete_number==4:
                    user_id_zakaz[event.user_id][6]=''
                    user_id_zakaz[event.user_id][7]=0
                elif delete_number==5:
                    user_id_zakaz[event.user_id][8]=''
                    user_id_zakaz[event.user_id][9]=0
                else:
                    vk.messages.send(user_id=event.user_id,message='Введите корректное число',keyboard=keyboard5.get_keyboard())
                zakaz=''
                i=0
                j=1
                k=1
                while i<len(user_id_zakaz[event.user_id]):
                    if user_id_zakaz[event.user_id][i]!='':
                        zakaz=zakaz+str(k)+'.'+user_id_zakaz[event.user_id][i]+user_id_zakaz[event.user_id][j]+'\n'
                        k=k+1
                    i=i+2
                    j=j+2
                vk.messages.send(user_id=event.user_id,message=zakaz,keyboard=keyboard5.get_keyboard())     
                user_id_td[event.user_id]=False
            if event.text=='Посчитать итоговую стоимость':
                itog_price=0
                i=1
                while i<len(user_id_zakaz[event.user_id]):
                    itog_price=itog_price+int(user_id_zakaz[event.user_id][i])
                    i=i+2
                vk.messages.send(user_id=event.user_id,message='Отлично. Итоговая цена:'+str(itog_price)+' руб',keyboard=keyboard1.get_keyboard())
            if event.text=='Посмотреть заказ':
                zakaz=''
                i=0
                j=1
                k=1
                while i<len(user_id_zakaz[event.user_id]):
                    if user_id_zakaz[event.user_id][i]!='':
                        zakaz=zakaz+str(k)+'.'+user_id_zakaz[event.user_id][i]+user_id_zakaz[event.user_id][j]+'\n'
                    i=i+2
                    j=j+2
                    k=k+1
                vk.messages.send(user_id=event.user_id,message=zakaz,keyboard=keyboard5.get_keyboard())                
            if event.text=='Посчитать заказ':
                vk.messages.send(user_id=event.user_id,message='Выберите формат.',keyboard=keyboard2.get_keyboard())  
                print(event.message_id )
                user_id_t[event.user_id] = True
                user_id_d[event.user_id] = event.message_id
                user_id_zakaz[event.user_id]=[]
            if event.text=='Добавить к заказу':
                if len(user_id_zakaz[event.user_id])<10:
                    vk.messages.send(user_id=event.user_id,message='Выберите формат.',keyboard=keyboard2.get_keyboard())  
                    print(event.message_id )
                    user_id_t[event.user_id] = True
                    user_id_d[event.user_id] = event.message_id
                else:
                    vk.messages.send(user_id=event.user_id,message='Вы превысили допустимое количество позиций.Пожалуйста завершите текущий заказ или удалите ненужные позиции',keyboard=keyboard5.get_keyboard())        
            if (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t.get(event.user_id,False):
                vk.messages.send(user_id=event.user_id,message='Отлично. Теперь введите кол-во листов')
                user_id_d[event.user_id] = event.message_id
                user_id_rezka[event.user_id]=event.text
                user_id_t[event.user_id]=False
                user_id_t2[event.user_id]=True
            if (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t2.get(event.user_id,False):
                vk.messages.send(user_id=event.user_id,message='Хорошо. Теперь выберите конфигурацию цвета',keyboard=keyboard3.get_keyboard())
                user_id_countlist[event.user_id] = event.text
                user_id_d[event.user_id] = event.message_id
                user_id_t2[event.user_id]=False
                user_id_t3[event.user_id]=True
            if (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t3.get(event.user_id,False):
                vk.messages.send(user_id=event.user_id,message='Хорошо. Теперь выберите плотность бумаги',keyboard=keyboard4.get_keyboard())
                user_id_color[event.user_id] = event.text
                user_id_d[event.user_id] = event.message_id
                user_id_t3[event.user_id]=False
                user_id_t4[event.user_id]=True
            if (event.to_me and event.message_id>user_id_d.get(event.user_id,0))and user_id_t4.get(event.user_id,False):
                user_id_plotnost[event.user_id]=event.text
                rezka_answer=user_id_rezka[event.user_id]
                count_lists=user_id_countlist[event.user_id]
                color_per=user_id_color[event.user_id]
                paper_plot=user_id_plotnost[event.user_id]

                try:
                    count_lists=int(count_lists)
                    user_id_price[event.user_id]=calc_def.calc_price(rezka_answer,count_lists,color_per,paper_plot,calc_def.rezka,calc_def.color,calc_def.paper)
                    user_id_zakaz[event.user_id].append(user_id_rezka[event.user_id]+', бумага '+user_id_plotnost[event.user_id]+'/'+user_id_countlist[event.user_id]+'шт Стоимость:')
                    user_id_zakaz[event.user_id].append(user_id_price[event.user_id])
                    vk.messages.send(user_id=event.user_id,message='Отлично, желаете что-то добавить?',keyboard=keyboard5.get_keyboard())
#                    vk.messages.send(user_id=event.user_id,message=user_id_zakaz[event.user_id][0]+user_id_zakaz[event.user_id][1],keyboard=keyboard5.get_keyboard())
                except TypeError:
                    vk.messages.send(user_id=event.user_id,message='Даны неподдерживаемые ответы. Пожалуйста воспользуйтесь vk-клавиатурой',keyboard=keyboard1.get_keyboard())
                user_id_countlist[event.user_id] = event.text
                user_id_d[event.user_id] = event.message_id
                user_id_t4[event.user_id]=False
            print()




if __name__ == '__main__':
    main()
