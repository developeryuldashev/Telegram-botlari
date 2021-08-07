from telegram.ext import Updater,CommandHandler, MessageHandler
from keyboards import keyboard
from connect import *
from telegram import ReplyKeyboardMarkup
ortga_batton= ReplyKeyboardMarkup(
    [
       ['🔙 ortga']
    ],resize_keyboard=True
)

def  start(update, context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Assalomu alaykum {user.first_name}, Mavhum otlar lug'ati telegram botiga hush kelibsiz!",
                             reply_markup=keyboard)
def  start2(update, context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"{user.first_name}, Mavhum otlar lug'ati telegram botiga hush kelibsiz!",
                             reply_markup=keyboard)


def message(update, context):
    db = Databasa()
    code = db.read()
    message = update.message.text
    # print(update)
    if message == "📝So'z qidirish 🔍":
        db.help(0)
        context.bot.send_message(chat_id=update.effective_chat.id,
                               text="bu yerda siz izlagan so'zlaringizni topasiz! ",
                                 reply_markup=ortga_batton)
    elif message == "🔙 ortga":
        return start2(update,context)
    elif message == "📝📌 fikr bildirish":
        db.help(1)
        context.bot.send_message(chat_id=update.effective_chat.id,
                               text="Sizni fikringiz biz uchun muhim! ",
                                 reply_markup=ortga_batton)
    elif message == "🤖 bot haqida 🤖":
        db.help(0)
        context.bot.send_message(chat_id=update.effective_chat.id,
                               text="Bot haqida malumot: o'quvchilar uchun: \n Mavhum otlar telegram boti.\n\n🔍 Bu yerda sizni qiziqtirgan mavhum otlarni  qidirishingiz mumkin. ",
                                 reply_markup=ortga_batton)
    elif message == "👨‍💻 aloqa":
        db.help(0)
        context.bot.send_message(chat_id=update.effective_chat.id,
                               text="<b>G'oya muallifi:</b> Termiz davlat universiteti Magistratura bo'limi "
                                    "5A111701-Ta'limtarbiya nazariyasi va metodikasi (boshlang'ich ta'lim)"
                                    " yo'nalishi 2-kurs magistranti \n<b>Yo'ldosheva Hosiyat Madat qizi</b>"
                                    "\n\n<b>Dasturchi:</b> O'zbekiston Milliy Universiteti \n Axborot tizimlarining matematik va dasturiy "
                                    "taminot yo'nalishi 2- bosqich talabasi <b>Yo'ldoshev Dilshod.</b>\n Aloqa 📱: @developeryuldashev", parse_mode='HTML',
                                 reply_markup=ortga_batton)

    elif code[0] == 1:
        context.bot.send_message(chat_id=update.effective_chat.id,
                               text="Fikringiz uchun rahmat",
                                 reply_markup=ortga_batton)
        context.bot.send_message(chat_id=1436644080,
                               text=f"Fikr keldi \n\n{message}\n\ntg:@{update.message.from_user.username}")
    else:
        message = message.lower()
        all_data = db.search(message)
        # print(all_data)
        if all_data:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=all_data[0])
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="❌ afsuski bunday so'z yuq.\n Agar bu so'zni muhim deb hisoblasangiz 😉:  📝📌 fikr bildirish bo'limi orqali qoldiring.!")

