from telegram import  ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from bs4 import BeautifulSoup as BS
from telegram.ext import CallbackContext
import requests

keyboard=ReplyKeyboardMarkup([
    ['Andijon','Buxoro'],
    ["Farg'ona","Jizzax"],
    ['Namangan','Navoiy'],
    ['Qashqadaryo','Surxondaryo'],
    ['Sirdaryo','Samarqand'],
    ["Qoraqalpog'iston","Xorazm"],
    ['Toshkent viloyati','Toshkent']

],resize_keyboard=True)

def start(update, context):
    user = update.message.from_user
    # reply_markup = InlineKeyboardMarkup(keyboard)
    reply_markup=keyboard
    update.message.reply_html(
        'Assalomu Aleykum <b>{}</b> 🤝. uzbweather_bot ga xush kelibsiz !!! \n  \nSizga foydamiz tegganidan xursandmiz😊. Iltimos hududni tanlang:'.format(
            user.full_name), reply_markup=reply_markup)

    return 1


def andijon(update, context:CallbackContext):
    print("siz andijonni tanladingiz")
    r = requests.get('https://sinoptik.ua/погода-андижан')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Andijon belgilandi. Bugun Andijonda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def buxoro(update, context):
    r = requests.get('https://sinoptik.ua/погода-бухара')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Buxoro belgilandi. Bugun Buxoroda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def fargona(update, context):
    r = requests.get('https://sinoptik.ua/погода-фергана')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Farg'ona belgilandi. Bugun Farg'onada ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def jizzax(update, context):
    r = requests.get('https://sinoptik.ua/погода-джизак')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Jizzax belgilandi. Bugun Jizzaxda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def namangan(update, context):
    r = requests.get('https://sinoptik.ua/погода-наманган')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Namangan belgilandi. Bugun Namanganda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def navoiy(update, context):
    r = requests.get('https://sinoptik.ua/погода-навои')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Navoiy belgilandi. Bugun Navoiyda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def qashqadaryo(update, context):
    r = requests.get('https://sinoptik.ua/погода-карши')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Qashqadaryo belgilandi. Bugun Qashqadaryoda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def qoraqalpogiston(update, context):
    r = requests.get('https://sinoptik.ua/погода-нукус')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Qoraqalpog'iston belgilandi. Bugun Qoraqalpog'istonda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def samarqand(update, context):
    r = requests.get('https://sinoptik.ua/погода-самарканд')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Samarqand belgilandi. Bugun Samarqandda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def sirdaryo(update, context):
    r = requests.get('https://sinoptik.ua/погода-сырдарья')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Sirdaryo belgilandi. Bugun Sirdaryoda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def surxondaryo(update, context):
    r = requests.get('https://sinoptik.ua/погода-термез')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    #############################################
    t_min = minimum[0].text
    t_max = maximum[0].text

    #############################################
    update.message.reply_text(
        "Surxondaryo belgilandi. Bugun Surxondaryoda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def toshkent_viloyati(update, context):
    r = requests.get('https://sinoptik.ua/погода-кибрай')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min = minimum[0].text
    t_max = maximum[0].text

    update.message.reply_text(
        "Toshkent viloyati belgilandi. Bugun Toshkent viloyatida ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def toshkent(update, context):
    r = requests.get('https://sinoptik.ua/погода-ташкент')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min = minimum[0].text
    t_max = maximum[0].text

    update.message.reply_text(
        "Buxoro belgilandi. Bugun Buxoroda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def xorazm(update, context):
    r = requests.get('https://sinoptik.ua/погода-ургенч')
    html = BS(r.content, 'html.parser')
    minimum = html.findAll("div", {"class": "min"})
    maximum = html.findAll("div", {"class": "max"})

    t_min = minimum[0].text
    t_max = maximum[0].text
    print(t_max)

    update.message.reply_text(
        "Xorazm belgilandi. Bugun Xorazmda ob-havo 🌦👇:" + '\n' + "Eng past daraja⬇️ :" + t_min + ',' + '\n' + "Eng yuqori daraja⬆️ :" + t_max,
        reply_markup=keyboard)


def help_command(update, context):
    update.message.reply_text("Yordam uchun @Dilshod2708 ga murojaat qiling .")


def admin(update, context):
    update.message.reply_text("Admin👨🏻‍💻 bilan bog'lanish - @@Dilshod2708 ")


# def main():
#######################################################################################
updater = Updater(token='2067264061:AAHGTALp8LIfwHIGnDNh61ye19-nIPOsitk',use_context=True)
conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [
                MessageHandler(Filters.regex('^(Andijon)$'), andijon),
                MessageHandler(Filters.regex('^(Buxoro)$'), buxoro),
                MessageHandler(Filters.regex("^(Farg'ona)$"), fargona),
                MessageHandler(Filters.regex('^(Jizzax)$'), jizzax),
                MessageHandler(Filters.regex('^(Namangan)$'), namangan),
                MessageHandler(Filters.regex('^(Navoiy)$'), navoiy),
                MessageHandler(Filters.regex('^(Qashqadaryo)$'), qashqadaryo),
                MessageHandler(Filters.regex("^(Qoraqalpog'iston)$"), qoraqalpogiston),
                MessageHandler(Filters.regex('^(Samarqand)$'), samarqand),
                MessageHandler(Filters.regex('^(Sirdaryo)$'), sirdaryo),
                MessageHandler(Filters.regex('^(Surxondaryo)$'), surxondaryo),
                MessageHandler(Filters.regex('^(Toshkent viloyati)$'), toshkent_viloyati),
                MessageHandler(Filters.regex('^(Toshkent)$'), toshkent),
                MessageHandler(Filters.regex('^(Xorazm)$'), xorazm),

            ]
        },
        fallbacks=[MessageHandler(Filters.text, start)]
    )

updater.dispatcher.add_handler(conv_handler)
#######################################################################################
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('admin', admin))

updater.start_polling()
# updater.idle()



