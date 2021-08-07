from telegram.ext import  Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext import Filters
from methods import *


updater = Updater(token='1700662784:AAEW5X6O2sTZoNCG73jvjjCHZNJHL9XPktQ', use_context=True)
dispatcher=updater.dispatcher
#   handlerlar qismi
start_handler=CommandHandler('start',start)
message_handler = MessageHandler(Filters.text, message)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)






updater.start_polling()





