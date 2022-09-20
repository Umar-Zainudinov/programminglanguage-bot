import telebot
from telebot import types

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://itproger.com"))
    bot.send_message(message.chat.id,
                     "Отличный выбор, нажмите на кнопку ниже и начинайте изучения курсов прямо сейчас",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['insta'])
def instagram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com/p/CeEiB4lNkxS/"))
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир разработчика прямо сейчас", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['vk'])
def vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить группу Вк", url="https://vk.com/budushiprogramist"))
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже и погрузитесь в мир разработчика прямо сейчас", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['vpn'])
def vpn(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Скачать лучший впн в хром",
                                          url="https://chrome.google.com/webstore/detail/proxy-%20-free-vpn-deeprism/bihhflimonbpcfagfadcnbbdngpopnjb?hl=ru"))
    markup.add(types.InlineKeyboardButton("Скачать лучший впн в яндекс",
                                          url="https://addons.opera.com/ru/extensions/details/proxy-free-vpn-deeprism/"))
    bot.send_message(message.chat.id, "Нажмите на кнопку ниже чтобы скачать впн", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Создание игр')
    btn2 = types.KeyboardButton('Мобильные приложения')
    btn3 = types.KeyboardButton('Веб разработка')
    btn4 = types.KeyboardButton('Софт для компьютеров')
    btn5 = types.KeyboardButton('Обработка данных')
    btn6 = types.KeyboardButton('Создание ИИ')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакое направление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "начать тест заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Создание игр')
        btn2 = types.KeyboardButton('Мобильные приложения')
        btn3 = types.KeyboardButton('Веб разработка')
        btn4 = types.KeyboardButton('Софт для компьютеров')
        btn5 = types.KeyboardButton('Обработка данных')
        btn6 = types.KeyboardButton('Создание ИИ')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        final_message = "Решил попробовать что-то ещё? \nВыбери какое направление тебя интересует:"

    elif get_message_bot == "создание игр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Под мобильные телефоны')
        btn2 = types.KeyboardButton('Компьютеры и консоли')
        btn3 = types.KeyboardButton('Виртуальная реальность')
        btn4 = types.KeyboardButton('Web игра')
        btn5 = types.KeyboardButton("Начать тест заново")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Отлично, геймдев крутая тема, но под что хочется разрабатывать?"

    elif get_message_bot == "под мобильные телефоны":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по Unity", url="https://itproger.com/tag/unity"))
        final_message = "Для разработки игр под мобильные устройства зачастую используется язык c#  и игровой движок <a href='https://itproger.com/tag/unity'>Unity</a>\nДвижок прост в изучении и вы можете просмотреть курс по кнопке ниже"

    elif get_message_bot == "компьютеры и консоли":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Небольшие игры')
        btn2 = types.KeyboardButton('Крупные проекты')
        btn3 = types.KeyboardButton('Начать тест заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чтобы разрабатывать игры на пк и консоли тебе нужно выбрать масштаб твоих проектов"

    elif get_message_bot == "небольшие игры":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть урок по созданию пк игры на Unity", url="https://youtu.be/rMlCciqXrb8"))
        markup.add(types.InlineKeyboardButton("Посмотреть урок по созданию игры на приставки ", url="https://youtube.com/playlist?list=PLwuxM-RwWBLBsDm-goWecnBe4mv8GAaey"))
        final_message = "Для разработки небольших игр под пк и консоли можно использовать язык c# на движке unity  <a href='https://youtu.be/rMlCciqXrb8'></a>\nДвижок прост в изучении и вы можете посмотреть урок по кнопке ниже."

    elif get_message_bot == "крупные проекты":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по Unreal Engine", url="https://youtu.be/-X6L0GXTjbU"))
        final_message = "Для разработки крупных игр под пк зачастую используется язык c++ и движок Unreal Engine <a href='https://youtu.be/-X6L0GXTjbU'></a>\nДвижок немного по сложнее в изучении и вы можете просмотреть курспо кнопке ниже"

    elif get_message_bot == "виртуальная реальность":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по виртуальной реальности на Unity", url="https://youtu.be/k5Xk9zSbc1I"))
        final_message = "Для разработки игр под виар зачастую используется язык с# и движок Unity <a href='https://youtu.be/k5Xk9zSbc1I'></a>\nДвижок прост в изучении и вы можете просмотреть курс по кнопке ниже"

    elif get_message_bot == "web игра":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по Web играх", url="https://youtu.be/-X6L0GXTjbU"))
        final_message = "Для разработки web игр используется язык javascript и html<a href='https://itproger.com/news/sozdanie-igri-zmeyka-na-chistom-javascript-i-html5'></a>\nЯзык лёгок в  изучении и вы можете просмотреть урок по кнопке ниже"

    elif get_message_bot == "мобильные приложения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('IOS')
        btn2 = types.KeyboardButton('Android')
        btn3 = types.KeyboardButton('Начать тест заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Отлично, mobile-разработка крутая тема, но надо выбрать под какую операционую систему будешь программировать?"

    elif get_message_bot == "ios":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по языку Swift", url="https://itproger.com/course/swift"))
        final_message = "Для разработки приложений на ios используется язык swift<a href='https://itproger.com/course/swift'></a>\nЯзык прост в  изучении так как apple сделала всё для этого и вы можете просмотреть курс по кнопке ниже.\nПримечание: нужен pc или ноутбук от apple"

    elif get_message_bot == "android":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по языку Java", url="https://itproger.com/course/java-android"))
        final_message = "Для разработки приложений на android используется много языков но я рекомендую java<a href='https://itproger.com/course/java-android'></a>\nЯзык прост в изучении и вы можете просмотреть курс по кнопке ниже."

    elif get_message_bot == "веб разработка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Внешний вид сайта (front-end)')
        btn2 = types.KeyboardButton('Работа с сервером (backend)')
        btn3 = types.KeyboardButton('Начать тест заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Отлично, веб разработка крутая тема, но какую часть сайта ты хочешь разрабатывать?"

    elif get_message_bot == "внешний вид сайта (front-end)":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курсы по front-end", url="https://itproger.com/tag/javascript"))
        final_message = "Для front-end часто используется языки javascrip, html, css и т.д.<a href='https://itproger.com/news/sozdanie-igri-zmeyka-na-chistom-javascript-i-html5'></a>\nЯзыки легки в  изучении и вы можете просмотреть список курсов и выбрать для себя подходящий по кнопке ниже"

    elif get_message_bot == "работа с сервером (backend)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Небольшой сайт или фриланс')
        btn2 = types.KeyboardButton('Стартапы и небольшие компании')
        btn3 = types.KeyboardButton('Большие компании')
        btn4 = types.KeyboardButton('Начать тест заново')
        markup.add(btn1, btn2, btn3, btn4)
        final_message = "Чтобы разрабатывать сайты (backend) тебе нужно выбрать масштаб твоих проектов"

    elif get_message_bot == "небольшой сайт или фриланс":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс PHP", url="https://itproger.com/course/php-mysql"))
        final_message = "Для разработки небольших сайтов используется язык php<a href=''></a>\nЯзык лёгок в  изучении и вы можете просмотреть курс по кнопке ниже"

    elif get_message_bot == "стартапы и небольшие компании":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по Python(backend)", url="https://itproger.com/course/django"))
        final_message = "Для создания стартапов и небольших компаний для бэкэнда используется язык python(фреймворк django)<a href='https://itproger.com/course/django'></a>\nЯзык лёгок в  изучении и вы можете просмотреть курс по кнопке ниже"

    elif get_message_bot == "большие компании":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по C#(backend)", url="https://itproger.com/course/asp-net"))
        final_message = "Для создания сайтов для больших компаний подходит язык C#<a href='https://itproger.com/course/asp-net'></a>\nЯзык лёгок в  изучении и вы можете просмотреть курс по кнопке ниже"

    elif get_message_bot == "софт для компьютеров":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Windows')
        btn2 = types.KeyboardButton('Mac')
        btn3 = types.KeyboardButton('Все платформы')
        btn4 = types.KeyboardButton('Начать тест заново')
        markup.add(btn1, btn2, btn3, btn4)
        final_message = "Чтобы разрабатывать софты дял пк выбери операционую систему"

    elif get_message_bot == "windows":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по С#", url="https://itproger.com/course/csharp-app"))
        final_message = "Для создания софтов на windows подходит язык C#<a href='https://itproger.com/course/csharp-app'></a>\nЯзык лёгок в  изучении и вы можете просмотреть курс по кнопке ниже"

    elif get_message_bot == "mac":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по Swift", url="https://itproger.com/course/swift"))
        final_message = "Для создания софтов для Mac подходит язык Swift<a href='https://itproger.com/course/swift'></a>\nЯзык немного сложен в  изучении и вы можете просмотреть курс по кнопке ниже"

    elif get_message_bot == "все платформы":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по ", url="https://itproger.com/course/java"))
        final_message = "Для создания софтов для все операционых систем особенно для linux подходит язык java<a href='https://itproger.com/course/java'></a>\nЯзык лёгок в  изучении и вы можете просмотреть курс по кнопке ниже"

    elif get_message_bot == "обработка данных":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по обработке данных на python", url="https://youtube.com/playlist?list=PLD-piGJ3Dtl1Kh7jHGyEQRcA5hBe45GT5"))
        final_message = "Для обработки данных для подходит язык python<a href='https://youtube.com/playlist?list=PLD-piGJ3Dtl1Kh7jHGyEQRcA5hBe45GT5'></a>\nЯзык лёгок в  изучении и вы можете просмотреть курс по кнопке ниже"

    elif get_message_bot == "создание ии":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посмотреть курс по ии на python", url="https://youtube.com/playlist?list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh"))
        final_message = "Для создания ии подходит язык <a href='https://youtube.com/playlist?list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh'></a>\nЯзык лёгок в  изучении и вы можете просмотреть курс по кнопке ниже"

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Создание игр')
        btn2 = types.KeyboardButton('Мобильные приложения')
        btn3 = types.KeyboardButton('Веб разработка')
        btn4 = types.KeyboardButton('Софт для компьютеров')
        btn5 = types.KeyboardButton('Обработка данных')
        btn6 = types.KeyboardButton('Создание ИИ')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
