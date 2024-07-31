from telegram.ext import Updater, CommandHandler


TOKEN = '7461614480:AAEQXlEnZAa_GK3ZypKZV_JFmJd-NOUwSJo'

def start(update, context):
    message = 'Привет я человек!'
    '\n\n/message мои контакты'
    '\n/contact мои контакты'

    with open('photo.jpg', 'rb') as file:
        update.message.reply_photo(file, message)

def contact(update, context):
    message = '+992 935844412 \n нет второго номера:( )'

def talk(update, context):
    message = 'я занят не звоните!!'


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('contact', contact))
    dispatcher.add_handler(CommandHandler('talk', talk))

    updater.start_polling()
    updater.idle()
    

if __name__=='__main__':
    main()

