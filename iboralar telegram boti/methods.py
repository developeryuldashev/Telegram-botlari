from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from keyboards import *
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from connect import DBHelper
ortga_batton= ReplyKeyboardMarkup(
    [
       ['🔙 ortga']
    ],resize_keyboard=True
)

DB_NAME='iboralar_jadvali.db'
def start(update, context):
    user = update.message.from_user
    update.message.reply_html(f"Assalomu alaykum <b>{user.first_name}</b>,\n<b><em>Iboralar </em></b> telegram "
                                  f"botiga hush kelibsiz!",
                             reply_markup=keyboard)

def  start2(update, context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"{user.first_name}, <b><em>Iboralar </em></b> telegram botiga hush kelibsiz!",
                             reply_markup=keyboard)
db=DBHelper(DB_NAME)
def message(update,context):
    messag= update.message.text
    if update.message.text=="📝 Iboralar 🔍":
        buttons = region_buttons()

        update.message.reply_html(f'''<b> Marxamat kerakli iborani tanlang ✅! </b>''',
                                  reply_markup=InlineKeyboardMarkup(buttons))
    elif messag == "🔙 ortga":
        return start(update,context)
    elif messag == "📝📌 fikr bildirish":
        context.bot.send_message(chat_id=update.effective_chat.id,
                               text="Sizni fikringiz biz uchun muhim! ",
                                 reply_markup=ortga_batton)
    elif messag == "🤖 bot haqida 🤖":
        context.bot.send_message(chat_id=update.effective_chat.id,
                               text="Bot haqida malumot: o'quvchilar uchun: \n <b><em>Iboralar </em></b> "
                                    " telegram boti.\n"
                                    "\n🔍 Bu yerda sizni qiziqtirgan iborani "
                                    " ma'nosini ko'rishingiz  mumkin. ",parse_mode='HTML',
                                 reply_markup=ortga_batton)
    elif messag == "👨‍💻 aloqa":
        context.bot.send_message(chat_id=update.effective_chat.id,
                               text="<b>G'oya muallifi:</b> Termiz davlat universiteti Magistratura bo'limi "
                                    "5A111701-Ta'limtarbiya nazariyasi va metodikasi (boshlang'ich ta'lim)"
                                    " yo'nalishi 2-kurs magistranti \n<b>Xoliqova Parvina Abdumalik qizi</b>"
                                    "\n\nDasturchi: O'zbekiston Milliy Universiteti \n Axborot tizimlarining matematik va dasturiy "
                                    "taminot yo'nalishi 2- bosqich talabasi Yo'ldoshev Dilshod.\n Aloqa 📱: @developeryuldashev",
                                 parse_mode='HTML',reply_markup=ortga_batton)




    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text='Fikringiz uchun raxmat!',reply_markup=ortga_batton)
        context.bot.send_message(chat_id=1436644080,
                                 text=f"Fikr keldi \n\n{update.message.text}\n\ntg:@{update.message.from_user.username}")


def  region_buttons():
    regions = db.get_regions()
    buttons = []
    tmp_b = []
    for region in regions:
        tmp_b.append(InlineKeyboardButton(region['ibora'], callback_data=region['id']))
        if len(tmp_b) == 2:
            buttons.append(tmp_b)
            tmp_b = []
    return buttons

def inline_callback(update,context):
    query = update.callback_query
    # print(query.data)
    result = ""
    datas = db.get_regions()
    for i in datas:
        if str(i[0]) == query.data:
            result += "<b>"+i[1] + "</b>"+ ': '+ i[2]
            break

    if result:
        query.message.delete()
        context.bot.send_message(chat_id = update.effective_chat.id, text = result,parse_mode="HTML")
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text="malumot yuq")
