import telegram
from key_buttons import tele_button,youtubec,traningfootball


def main_meny_keyboard():
    Keyboard = ([
        [telegram.KeyboardButton(tele_button[0]),],
        [telegram.KeyboardButton(tele_button[1]),],
        [telegram.KeyboardButton(tele_button[2]),],
        [telegram.KeyboardButton(tele_button[3]),],
    ])
    return telegram.ReplyKeyboardMarkup(
        Keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def youtybec_menu_keyboard():
    Keyboard = ([
        [telegram.KeyboardButton(youtubec[0]),],
        [telegram.KeyboardButton(youtubec[1]),],
        [telegram.KeyboardButton(youtubec[2]),],
        [telegram.KeyboardButton(youtubec[3]),],
        [telegram.KeyboardButton(youtubec[4]),],
    ])
    return telegram.ReplyKeyboardMarkup(
        Keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def traningfootball_menu_keyboard():
    Keyboard = ([
        [telegram.KeyboardButton(traningfootball[0],)],
        [telegram.KeyboardButton(traningfootball[1],)],
        [telegram.KeyboardButton(traningfootball[2],)],
    ])
    return telegram.ReplyKeyboardMarkup(
        Keyboard, resize_keyboard=True, one_time_keyboard=False
    )