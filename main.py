from telegram.ext import Updater, CommandHandler

TOKEN = '7461614480:AAEQXlEnZAa_GK3ZypKZV_JFmJd-NOUwSJo'

def start(update, context):
    massage = ('Привет я человек '
               '\n\n/contact - Мои контакты'
               '\n/talk-общение сомной ')

    with open('photo_2024-07-31_17-21-48.jpg', 'rb') as file:
        update.message.reply_photo(file, massage)
def talk(update, context):
    talk = 'Мой аккаунт @Saw_Cuten'
    update.message.reply_text(message)

def contact(update, context):
    message = '+992 935844412  \n Нету второго номера :( )'
    update.message.reply_text(message)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('contact', contact))
    dispatcher.add_handler(CommandHandler('talk', talk))


    updater.start_polling()
    updater.idle()
    

if name=='main':
    main()
