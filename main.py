import os

import telebot
from telebot import types, custom_filters
from members import is_member
import win32print
import win32api

bot=telebot.TeleBot('6159680530:AAHhyp72GrNF7fOfF7TBRn0RcM-8NGwvBhg')
filenames={}
queue=[]
#creating a button

# @bot.message_handler(commands = ['start'])
# def url(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton(text='Новый Физтех ИТМО', url='https://physics.itmo.ru/en')
#     markup.add(btn1)
#     bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт Нового Физтеха ИТМО", reply_markup = markup)
#




@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.chat.id, "👋 Привет! Я твой бот-помощник по всему, что связано с Новым Физтехом ИТМО! ", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"Привет! Я бот для печати на принтерах Нового Физтеха ИТМО, для того, чтобы начать работу со мной, введите команду /start")

@bot.message_handler(chat_id=[1395787106] ,commands=['admin'])
def admin_rep(message):
    bot.send_message(message.chat.id, 'You are admin!')

@bot.message_handler(commands=['admin'])
def not_admin(message):
    bot.send_message(message.chat.id, 'You are not allowed to use these functions ')

bot.add_custom_filter(custom_filters.ChatFilter())

@bot.message_handler(content_types=['document'])
def print(message):
    if is_member(message.from_user.id):
        #bot.send_message(message.chat.id,'You are allowed to print! ')
        #bot.send_message(message.chat.id,(str)(message.text))
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            global filenames
            filenames[message.chat.id] = message.document.file_name
            src = 'C:/Users/User/Desktop/python/print_bott/' + message.document.file_name
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
                btn1 = types.KeyboardButton('Xerox WorkCentre 3215')
                btn2 = types.KeyboardButton('Принтер 2')
                btn3 = types.KeyboardButton('Принтер 3')
                markup.add(btn1, btn2, btn3)
                bot.reply_to(message, "Щас всё распечатаем), выберите принтер, которым хотите воспользоваться",reply_markup=markup)
        except Exception as e:
            bot.reply_to(message, (str)(e))

    else:
        bot.send_message(message.chat.id, 'You are not allowed to print. To enter the New PhysTech community, you need to add your telegram id to your account on New PhysTech cite as it is done in the instruction below')
        with open('C:/Users/User/Desktop/python/print_bott/instruction.jpg', 'rb') as instr_pic_file:
            instruction_pic = instr_pic_file.read()

        bot.send_photo(message.chat.id, instruction_pic)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Узнать расписание Нового Физтеха ИТМО')
        btn2 = types.KeyboardButton('Печать документов')
        btn3 = types.KeyboardButton('Wiki Нового Физтеха')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите интересующую вас опцию', reply_markup=markup) #ответ бота
    elif message.text == 'Узнать расписание Нового Физтеха ИТМО':
        bot.send_message(message.chat.id, 'Для того, чтобы посмотреть расписание, перейдите по '+'[ссылке](https://docs.google.com/spreadsheets/d/1w1nIVkxW2ibAPV_BCkV3-B8czREx_1fN5lmTyl9XkJQ/edit#gid=1941185286)', parse_mode='Markdown')
    elif message.text == 'Печать документов':
        bot.send_message(message.chat.id, 'Пришлите боту в чат документ, который вы хотите распечатать')
    elif message.text == 'Wiki Нового Физтеха':
        bot.send_message(message.chat.id, 'Для того, чтобы попасть на Wiki Нового Физтеха, перейдите по '+ '[ссылке](https://wiki.physics.itmo.ru/Main_Page)', parse_mode='Markdown')
    elif message.text=='Xerox WorkCentre 3215':
        try:
            name = 'Xerox WorkCentre 3215'
            printdefaults = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
            ## начинаем работу с принтером ("открываем" его)
            handle = win32print.OpenPrinter(name, printdefaults)
            global filenames
            win32print.StartDocPrinter(handle, 1, [filenames[message.chat.id], None, "raw"])

            win32api.ShellExecute(0, "print",filenames[message.chat.id], '/d:"%s"' % name, ".", 0)

            bot.send_message(message.chat.id,'Готово!')
        except Exception as e:
            #global filenames
            bot.send_message(message.chat.id,(str)(e))
        finally:
            # src = 'C:/Users/User/Desktop/python/print_bot/' + filenames[message.chat.id]
            # os.remove(src)
            # filenames.pop(message.chat.id)
            queue.append(filenames[message.chat.id])
            if len(queue)>=3:
                src = 'C:/Users/User/Desktop/python/print_bott/' + queue[0]
                for key in filenames:
                    if filenames[key]==queue[0]:
                        filenames.pop(key)
                os.remove(src)
                queue.pop(0)


bot.polling(none_stop=True, interval=0)