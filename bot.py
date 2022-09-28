import telebot
from flask import Flask, request
from telebot import types
import os

TOKEN = "5764245679:AAEPEmWAJS-grXNilswWHDg5oaQmSnm70rM"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


#Greeting message
@bot.message_handler(commands=["start"])
def greet(message):
    bot.reply_to(message, "Hi! my name is Marie and I would like to inform you about a crypto named solidecoin (SOLIDE).\n" + "With solidecoin, you have access to cheaper crypto transactions and many other benefits.\n" + "The Solide protocol is giving out free solidecoin to exclusive 100000 persons \n" + "and $2000000 has been benchmarked to be given free of charge.\n" + "Note this crypto is going out for free.\n" + "All benchmarked coins would be given out in just 72 hours.\n" + "To get solidecoin type /begin.")


@bot.message_handler(commands=['begin'])
def start_command(message):
   bot.send_message(
       message.chat.id,
       "SOLIDE exists on different social platforms.\n" + "It is very important that you follow all of solidecoin's social media accounts in order to receive solidecoin.To follow all solide socials type /follow.\n" + "When you have completed the task type /done")

@bot.message_handler(commands=['done'])
def greet(message):
    bot.reply_to(message, "Hi! please do not forget I will review to see if you completed the tasks.\n" + "If you have done all this type /next")


@bot.message_handler(commands=["Telegram"]) 
def send_multi_message(message):
    bot.send_message(message.chat.id, 'https://t.me/SolideCoins')

@bot.message_handler(commands=["Twitter"]) 
def send_multi_message(message):
    bot.send_message(message.chat.id, 'https://twitter.com/SolideCoins/')


@bot.message_handler(commands=["YouTube"]) 
def send_multi_message(message):
    bot.send_message(message.chat.id, ' https://youtube.com/channel/UC_MHslniyv0UHeiJsXO0v9A')

@bot.message_handler(commands=["Instagram"]) 
def send_multi_message(message):
    bot.send_message(message.chat.id, ' https://www.instagram.com/solidecoins/')


@bot.message_handler(commands=['follow'])
def send_follow_message(message):
   markup = types.ReplyKeyboardMarkup(row_width=2)
   itembtn1 = types.KeyboardButton("/Twitter")
   itembtn2 = types.KeyboardButton("/Instagram")
   itembtn3 = types.KeyboardButton("/YouTube")
   itembtn4 = types.KeyboardButton("/Telegram")
   markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
   bot.send_message(chat_id=message.chat.id, text="Follow to get solidecoin",reply_markup=markup)
    
#Does not respond to non-text content
@bot.message_handler(content_types=["photo", "sticker", "audio"])
def send_content_message(message):
    bot.reply_to(message, "This is not a text message, please text only!")

@bot.message_handler(commands=['next'])
def help_command(message):
    bot.send_message(message.chat.id, "Perfect, you are now qualified to get solidecoin ..\n" + "To claim your solidecoin follow the steps.\n" +
          "1)Kindly send your Ethereum address to this link https://forms.gle/ZsworxWTfsMhFxrL9.\n" +
          "2)Submit your referral code if any. if completed press /end")

@bot.message_handler(commands=['solide'])
def help_command(message):
   bot.send_message(
       message.chat.id,'https://solidecoins.com/developers/') 
  

@bot.message_handler(commands=["end"]) 
def send_multi_message(message):
    bot.send_message(message.chat.id, "You have a 10% total tokens sent to you using the last 5 digits of your Ethereum address as your referral.\n" + "You get instant deposits on your referral.\n" + "Thanks for being part of the solidecoin community, please anticipate and expect your solidecoin token.\n" + "Please note seasoned investors and developers should join the discord\n" + "to receive investment updates and be part of the developer's community.\n" + "Thanks for your time. Have a good day.\n" + "Marie.\n" + "To know more about solidecoin you can check out the solide website click /solide")  
  
#This throws an error message
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	  bot.reply_to(message, "Unrecognized command. Please try again!")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://shrouded-woodland-07616.herokuapp.com/' + "5764245679:AAEPEmWAJS-grXNilswWHDg5oaQmSnm70rM")
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


