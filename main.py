import telebot
import os
import google.generativeai as genai

# التوكن الخاص بك
BOT_TOKEN = "8723205190:AAHe24TckCbxlUf-gO67H8K3Vjhh_pRr bN4"
# مفتاح Gemini (يفضل وضعه كمتغير بيئة لاحقاً للأمان)
GEMINI_API_KEY = "حط_هنا_مفتاح_Gemini_بتاعك" 

bot = telebot.TeleBot(BOT_TOKEN)

# إعداد نموذج الذكاء الاصطناعي
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except:
    print("يرجى التأكد من مفتاح Gemini API")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك في بوت مساعد المدرسين! 🍎\nأنا جاهز لمساعدتك في تحضير الدروس والإجابة على الأسئلة التعليمية.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # إرسال سؤال المدرس للذكاء الاصطناعي
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "عذراً، أنا تحت التحديث الآن أو هناك مشكلة في الاتصال. حاول مرة أخرى.")

print("البوت يعمل الآن...")
bot.infinity_polling()
      
