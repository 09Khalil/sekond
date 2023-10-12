from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from meny import (
    main_meny_keyboard,
    youtybec_menu_keyboard,
    traningfootball_menu_keyboard
)
from key_buttons import tele_button, youtubec, traningfootball

HISTORY_FOOTBALL = tele_button[0]
PRAVILA_FOOTBALL = tele_button[1]
YOUTUBEC = tele_button[2]
TRANINGFOOTBALL = tele_button[3]
DROTS = youtubec[0]
AMKAL = youtubec[1]
JFOOTBALL = youtubec[2]
MUHA = youtubec[3]
PROVFOOTBALL = traningfootball[0]
ANTON = traningfootball[1]
BACK = youtubec[4]

def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать {update.effective_user.username}\nэтот бот поможет вам с информацией Футболе,',
        reply_markup=main_meny_keyboard()
    )

def history_football(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Зарождение футболаПервые правила игры в футбол были введены 7 декабря 1863 года Футбольной ассоциацией Англии. Сегодня правила' 
        'футбола устанавливает Международный совет футбольных ассоциаций (IFAB), в который входят ФИФА (4 голоса), а также представители' 
        'английской, шотландской, североирландской и валлийской футбольных ассоциаций.',
    )
def pravila_football(update:Update, contetx:CallbackContext):
    update.message.reply_text(
        f'Есть 17 официальных правил игры, каждое из которых содержит список оговорок и руководящих принципов.'
        'Эти правила предназначены для применения на всех уровнях футбола, хотя есть некоторые изменения для таких групп, как юниоры,' 
        'взрослые, женщины и люди с ограниченными физическими возможностями.',
    )

def reply_youtubec(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Choose football',
        reply_markup=youtybec_menu_keyboard()
    )

def reply_traningfootball(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Choose traning',
        reply_markup=traningfootball_menu_keyboard()
    )

def reply_drots(update:Update, contetx:CallbackContext):
    update.message.reply_text(
        f'https://www.youtube.com/@twodrots'
    )

def reply_amkal(update:Update, contetx:CallbackContext):
    update.message.reply_text(
        f'https://www.youtube.com/@GermanElClassico'
    )

def reply_jfootbal(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'https://www.youtube.com/@freekicksRUS'
    )

def reply_muha(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'https://www.youtube.com/@mmflixstudio'
    )

def reply_provfootball(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'https://www.youtube.com/@Profifootball22'
    )

def reply_anton(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'https://www.youtube.com/@AntonMaltcev'
    )

def reply_back(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Вы вернулись в главное меню.',
        reply_markup=main_meny_keyboard()
    )

def reply_back(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Вы вернулись в главное меню.',
        reply_markup=main_meny_keyboard()
    )

updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HISTORY_FOOTBALL),
    history_football
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PRAVILA_FOOTBALL),
    pravila_football
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(YOUTUBEC),
    reply_youtubec      
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(TRANINGFOOTBALL),
    reply_traningfootball
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(DROTS),
    reply_drots
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(AMKAL),
    reply_amkal
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JFOOTBALL),
    reply_jfootbal
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MUHA),
    reply_muha
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PROVFOOTBALL),
    reply_provfootball
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ANTON),
    reply_anton
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    reply_back
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    reply_back
))

updater.start_polling()
updater.idle()
print('khalil')