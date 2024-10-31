import telebot
from newsapi import NewsApiClient
from datetime import datetime
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY") 

bot = telebot.TeleBot(TELEGRAM_TOKEN)
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

categories = {
    'general': 'Generales',
    'business': 'Negocios',
    'technology': 'Tecnología',
    'sports': 'Deportes',
    'entertainment': 'Entretenimiento',
    'science': 'Ciencia',
    'health': 'Salud'
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [types.KeyboardButton(f'/noticias_{cat}') for cat in categories.keys()]
    markup.add(*buttons)
    
    welcome_text = """
    ¡Bienvenido al Bot de Noticias! 🗞️
    
    Puedes obtener noticias usando los siguientes comandos:
    """
    for key, value in categories.items():
        welcome_text += f"\n/noticias_{key} - Noticias de {value}"
    
    bot.reply_to(message, welcome_text, reply_markup=markup)

def get_news(category):
    try:
        news = newsapi.get_top_headlines(
            country='es',  
            category=category,
            language='es'
        )
        return news
    except Exception as e:
        print(f"Error al obtener noticias: {e}")
        return None

@bot.message_handler(func=lambda message: message.text.startswith('/noticias_'))
def send_news(message):
    category = message.text.split('_')[1]
    if category in categories:
        news = get_news(category)
        if news and news['articles']:
            response = f"📰 Últimas noticias de {categories[category]}:\n\n"
            
            for article in news['articles'][:5]:  # Limitamos a 5 noticias
                title = article.get('title', 'Sin título')
                url = article.get('url', '')
                description = article.get('description', 'Sin descripción')
                
                response += f"🔹 *{title}*\n"
                response += f"{description}\n"
                response += f"[Leer más]({url})\n\n"
                
            bot.reply_to(message, response, parse_mode='Markdown', disable_web_page_preview=True)
        else:
            bot.reply_to(message, "Lo siento, no pude obtener noticias en este momento.")
    else:
        bot.reply_to(message, "Categoría no válida.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Comandos disponibles:
    
    /start - Iniciar el bot
    /help - Mostrar esta ayuda
    /noticias_[categoria] - Ver noticias por categoría
    """
    bot.reply_to(message, help_text)

if __name__ == "__main__":
    print("Bot iniciado...")
    bot.polling(none_stop=True)