import os
from telegram.ext import Updater, ConversationHandler, CommandHandler, MessageHandler, Filters

INITIAL, MIDDLE, FINAL = range(3)


def start(bot, updater):
    updater.message.reply_text('Hello')
    return INITIAL


def say_hello(bot, updater):
    updater.message.reply_text('INITIAL')
    return MIDDLE


def say_howdy(bot, updater):
    updater.message.reply_text('MIDDLE')
    return FINAL


def say_goodbye(bot, updater):
    updater.message.reply_text('FINAL')


def cancel(bot, updater):
    updater.message.reply_text('good bye')
    return  ConversationHandler.END


def main():
    TOKEN = os.environ['TELEGRAM_TOKEN']
    PORT =  int(os.environ.get('PORT', '8443'))
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    command = CommandHandler('help', help)

    conv_handler = ConversationHandler(
        entry_points= [CommandHandler('start', start)],
        states= {   INITIAL: [MessageHandler(Filters.text, say_hello), CommandHandler('init',  start)],
                  MIDDLE: [MessageHandler(Filters.text, say_howdy)],
                  FINAL: [MessageHandler(Filters.text, say_goodbye)]},
        fallbacks= [CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(command)

    #updater.start_polling()

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://summerpracrise.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
