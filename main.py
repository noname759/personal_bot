from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = '7461614480:AAEQXlEnZAa_GK3ZypKZV_JFmJd-NOUwSJo'

def start(update: Update, context: CallbackContext) -> None:
    with open('photo.jpg', 'rb') as photo_file:
        update.message.reply_photo(photo_file, caption='Привет я человек')

    button1 = InlineKeyboardButton("talk", callback_data='1')
    button2 = InlineKeyboardButton("contact", callback_data='2')
    button3 = InlineKeyboardButton("voice", callback_data='3')

    keyboard = [[button1, button2], [button3]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

def voice(update: Update, context: CallbackContext) -> None:
    with open('hello.ogg', 'rb') as voice_file:
        update.message.reply_voice(voice_file, caption="")

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    choice = query.data
    query.answer()

    if choice == '1':
        query.edit_message_text(text='Мой аккаунт @Saw_Cuten')
    elif choice == '2':
        query.edit_message_text(text='+992 935844412 \n Нету второго номера :(')
    elif choice == '3':
        query.edit_message_text(text="Вы выбрали кнопку voice")
        query.message.reply_voice(open('hello.ogg', 'rb'), caption="Голосовое сообщение")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('contact', lambda update, context: contact(update.message)))
    dispatcher.add_handler(CommandHandler('talk', lambda update, context: talk(update.message)))
    dispatcher.add_handler(CommandHandler('voice', voice))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
