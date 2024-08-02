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
        update.message.reply_voice(voice_file, caption="Голосовое сообщение")

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    choice = query.data
    query.answer()

    if choice == '1':
        talk(query, context)  
    elif choice == '2':
        contact(query, context) 
    elif choice == '3':
        query.edit_message_text(text="Вы выбрали кнопку voice")
        query.message.reply_voice(open('hello.ogg', 'rb'), caption="Голосовое сообщение")

def talk(query, context: CallbackContext) -> None:
    message = 'Мой аккаунт @Saw_Cuten'
    query.message.reply_text(message) 

def contact(query, context: CallbackContext) -> None:
    message = '+992 935844412 \n Нету второго номера :('
    query.message.reply_text(message) 

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('contact', contact))
    dispatcher.add_handler(CommandHandler('talk', talk))
    dispatcher.add_handler(CommandHandler('voice', voice))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
