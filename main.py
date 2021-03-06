import telebot
import pyowm
from config import BOT_TOKEN, OWM_TOKEN
from util.weather import get_forecast
from util.billboard_hit import get_song
from util.news import get_article


bot = telebot.TeleBot(BOT_TOKEN)
owm = pyowm.OWM(OWM_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome")


@bot.message_handler(commands=['help'])
def command_help(message):
    bot.send_message(message.chat.id, "š¤ /start\n" 
                                      "ā /weather - current weather condition\n" 
                                      "š /billboard - top ten billboard chart\n"
                                      "š° /news - latest bbc article\n")


@bot.message_handler(commands=['weather'])
def command_weather(message):
    sent = bot.send_message(message.chat.id, "šŗ Enter the City or Country\nš"
                            "In such format:  Toronto  or  japan")
    bot.register_next_step_handler(sent, send_forecast)


def send_forecast(message):
    forecast = get_forecast(message.text)
    bot.send_message(message.chat.id, forecast)


@bot.message_handler(commands=["billboard"])
def command_billboard(message):
    bot.send_message(message.chat.id, "Top Ten Billboard Songs")
    bot.send_message(message.chat.id, get_song(), parse_mode="HTML")


@bot.message_handler(commands=["news"])
def command_news(message):
    bot.send_message(message.chat.id, "BBC Latest News")
    bot.send_message(message.chat.id, get_article(), parse_mode="HTML")


bot.polling()

