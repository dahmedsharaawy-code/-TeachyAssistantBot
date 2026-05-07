import telebot
import os
import google.generativeai as genai

# قراءة التوكن من Variables الموقع ومسح أي مسافات زيادة أوتوماتيكياً
BOT_TOKEN = os.environ.get('BOT_TOKEN', '').strip()
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '').strip()

# التحقق من وجود التوكن
if not BOT_TOKEN:
    print("خطأ: لم يتم العثور على BOT_TOKEN في المتغيرات")
else:
    bot = telebot.TeleBot(BOT_TOKEN)

    # إعداد Gemini
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
    except Exception as e:
        print(f"خطأ في إعداد Gemini: {e}")

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "أهلاً بك! أنا مساعدك الذكي، أرسل سؤالك وسأجيبك فوراً.")

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        try:
            response = model.generate_content(message.text)
            bot.reply_to(message, response.text)
        except Exception as e:
            bot.reply_to(message, "عذراً، حدث خطأ في الاتصال. حاول مرة أخرى.")

    # تشغيل البوت
    if __name__ == "__main__":
        print("البوت يعمل الآن...")
        bot.polling(none_stop=True)
