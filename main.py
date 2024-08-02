from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkupgi
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = '7461614480:AAEQXlEnZAa_GK3ZypKZV_JFmJd-NOUwSJo'

def start(update: Update, context: CallbackContext) -> None:
    message = 'Привет я человек'
    button1 = InlineKeyboardButton("talk", callback_data='1')
    button2 = InlineKeyboardButton("contact", callback_data='2')
    button3 = InlineKeyboardButton("voice", callback_data='3')
    button4 = InlineKeyboardButton("group", callback_data='4')

    keyboard = [[button1, button2], [button3, button4]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

def voice(update: Update, context: CallbackContext) -> None:
    with open('.jpg', 'rb') as photo_file, open('.ogg', 'rb') as voice_file:
        update.message.reply_photo(photo_file, caption=message)
        update.message.reply_voice(voice_file, caption="Голосовое сообщение")

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    choice = query.data
    query.answer()
    query.edit_message_text(text=f"Вы выбрали кнопку {choice}")

def talk(update: Update, context: CallbackContext) -> None:
    message = 'Мой аккаунт @Saw_Cuten'
    update.message.reply_text(message)

def contact(update: Update, context: CallbackContext) -> None:
    message = '+992 935844412 \n Нету второго номера :('
    update.message.reply_text(message)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('contact', contact))
    dispatcher.add_handler(CommandHandler('talk', talk))
    dispatcher.add_handler(CommandHandler('voice', voice))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
