import telebot

# Создаем объект бота с указанным токеном доступа
TOKEN = '5816161752:AAFY0NXqD7eRj4mvpZEQA_jJX7xlK1cA1b0'
bot = telebot.TeleBot(TOKEN)

# Список вопросов и ответов
questions = [
    {
        "text": "Какая столица Украины?",
        "answers": ["Киев", "Москва", "Лондон", "Париж"],
        "correct_answer": 0
    },
    {
        "text": "Кто из этих людей был первым президентом США?",
        "answers": ["Томас Джефферсон", "Джон Адамс", "Джордж Вашингтон", "Бенджамин Франклин"],
        "correct_answer": 2
    },
    {
        "text": "Кто из этих компьютерных игр был разработан раньше?",
        "answers": ["Doom", "Quake", "Half-Life", "Counter-Strike"],
        "correct_answer": 0
    },
    {
        "text": "Какой газ преобладает в атмосфере Земли?",
        "answers": ["Кислород", "Азот", "Углекислый газ", "Неон"],
        "correct_answer": 1
    },
    {
        "text": "Какой город является столицей Греции?",
        "answers": ["Салоники", "Патры", "Афины", "Ираклион"],
        "correct_answer": 2
    }
]

# Словарь, где мы будем сохранять данные пользователей
users_data = {}

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Получаем идентификатор чата пользователя
    chat_id = message.chat.id
    # Создаем новую переменную с информацией о пользователе
    user_data = {"question_index": 0, "money": 0}
    # Сохраняем эту переменную в словарь данных пользователей
    users_data[chat_id] = user_data
    # Отправляем первый вопрос пользователю
    send_question(user_data, chat_id)

# Обработка выбора ответа на вопрос
@bot.callback_query_handler(func=lambda call: True)
def answer_handler(call):
    # Получаем идентификатор чата пользователя
    chat_id = call.message.chat.id
    # Получаем данные пользователя из словаря данных пользователей
    user_data = users_data.get(chat_id)
    # Если данные пользователя не найдены - игнорируем выбор ответа
    if not user_data:
        return
    if (call.data) == 'stop_game':
        bot.send_message(chat_id, f"Игра остановлена. Вы выиграли {user_data['money']}, но миллионером так и не стали")
        del users_data[chat_id]
    # Если ответ правильный, добавляем деньги и переходим к следующему вопросу
    elif int(call.data) == questions[user_data["question_index"]]["correct_answer"]:

        user_data["question_index"] += 1

        if (user_data["question_index"] == 0):
            user_data["money"] = 0
        elif (user_data["question_index"] == 1):
            user_data["money"] = 100000
        elif (user_data["question_index"] == 2):
            user_data["money"] = 200000
        elif (user_data["question_index"] == 3):
            user_data["money"] = 300000
        elif (user_data["question_index"] == 4):
            user_data["money"] = 500000

        if user_data["question_index"] == len(questions):
            # Если пользователь ответил на все вопросы, объявляем его победителем
            bot.send_message(chat_id, "Поздравляю! Вы стали миллионером!")
        else:
            # Если не все вопросы отвечены, отправляем следующий вопрос
            send_question(user_data, chat_id)
    else:
        # Если ответ неправильный, игрок проигрывает все деньги
        bot.send_message(chat_id, "К сожалению, вы ответили неправильно и проиграли все деньги.")
        user_data["money"] = 0
        user_data["question_index"] = 0

# Обработка команды /stop
@bot.message_handler(commands=['stop'])
def stop_handler(message):
    # Получаем идентификатор чата пользователя
    chat_id = message.chat.id
    # Получаем данные пользователя из словаря данных пользователей
    user_data = users_data.get(chat_id)
    # Если данные пользователя найдены - отправляем сообщение с количеством выигранных денег и удаляем данные пользователя из словаря
    if user_data:
        bot.send_message(chat_id, f"Вы выиграли {user_data['money']}")
        del users_data[chat_id]

# Обработка команды /stop_game_button
@bot.callback_query_handler(func=lambda call: call.data == "stop_game")
def stop_game_handler(call):
    # Получаем идентификатор чата пользователя
    chat_id = call.message.chat.id
    # Получаем данные пользователя из словаря данных пользователей
    user_data = users_data.get(chat_id)
    # Если данные пользователя найдены - отправляем сообщение с количеством выигранных денег и удаляем данные пользователя из словаря
    if user_data:
        bot.send_message(chat_id, f"Игра остановлена. Вы выиграли {user_data['money']}, но миллионером так и не стали")
        del users_data[chat_id]

# Функция отправки вопроса
def send_question(user_data, chat_id):
    # Получаем текущий вопрос из списка вопросов
    question = questions[user_data["question_index"]]
    # Создаем список кнопок с вариантами ответов
    keyboard = telebot.types.InlineKeyboardMarkup()
    for i, answer in enumerate(question["answers"]):
        keyboard.add(telebot.types.InlineKeyboardButton(answer, callback_data=str(i)))
    # Добавляем кнопку "Остановить игру"
    keyboard.add(telebot.types.InlineKeyboardButton(f"Забрать {user_data['money']}", callback_data="stop_game"))
    # Отправляем сообщение с вопросом и кнопками
    bot.send_message(chat_id, question["text"], reply_markup=keyboard)

# Запускаем бота
bot.polling(none_stop=True)
