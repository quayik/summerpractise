import os
from telegram.ext import Updater, ConvsersationHandler, CommandHandler, MessageHandler, Filters

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

def main():
    updater = Updater('897775594:AAETQPy4uS2Bhgpc6trJY8IYqm4r998edx8')

    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {INITIAL: [MessageHandler(Filters.text, say_hello), CommandHandler('init',  start)],
                  MIDDLE: [MessageHandler(Filters.text, say_howdy)],
                  FINAL: [MessageHandler(Filters.text, say_goodbye)]},
        fallbacks= [CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_handler)

    updater.start.polling()
    updater.idle()
    #updater.start.webhook()


if __name__ == '__main__':
    main()
