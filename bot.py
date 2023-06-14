import telebot
from telebot import types
from privateGPT import chat

bot = telebot.TeleBot("6292968307:AAGATomDnml2NrCj7W9Sh_ynxR8d-ksygp8")
provider_token = "1877036958:TEST:ebba1cfcb6bac177a51fd0304c36cf827a8bd4b1"


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, '''Welcome to <b>AI WORLD</b>! Connect with Al versions of your favorite influencers using realistic 2-way voice.\n\n<b>SELECT NAME OF YOUR INFLUENCER</b>\n\nAdd credits to your account with the /deposit command. For any questions or suggestions, contact our team @TEST .Thank you!''',
parse_mode="html"
)

@bot.message_handler(commands=['chat'])
def chat_with_ai(message):
    msg = bot.send_message(message.chat.id, text="Please enter your query:")
    bot.register_next_step_handler(msg, process_chat_handler)


def process_chat_handler(msg):
  if(msg.text == "exit"):
      bot.send_message(msg.chat.id, text="Bye bye:)")
      return
  bot.reply_to(msg, text="Please wait for 15-20 sec")
  bot.send_message(msg.chat.id, text=chat(msg.text))
  chat_with_ai(msg)


@bot.message_handler(commands=['deposit'])
def deposit(message):
  keyboard = types.InlineKeyboardMarkup()
  five = types.InlineKeyboardButton('5', callback_data='cb_deposit_5')
  ten = types.InlineKeyboardButton('10', callback_data='cb_deposit_10')
  fifteen = types.InlineKeyboardButton('20', callback_data='cb_deposit_20')
  twenty_five = types.InlineKeyboardButton('50', callback_data='cb_deposit_50')
  hundred = types.InlineKeyboardButton('100', callback_data='cb_deposit_100')
  two_fifty = types.InlineKeyboardButton('250', callback_data='cb_deposit_250')
  five_hundred = types.InlineKeyboardButton('500', callback_data='cb_deposit_500')
  keyboard.row_width = 2
  keyboard.add(five, ten, fifteen, twenty_five, hundred, two_fifty, five_hundred)
  details = types.InlineKeyboardButton('Details 🔍', callback_data='cb_premium')
  cancel = types.InlineKeyboardButton('Cancel ❌', callback_data='cb_premium')
  keyboard.row_width = 1
  keyboard.add(details, cancel)
  
  bot.send_message(message.chat.id, text='Payments are securely powered by Stripe. Please select the deposit amount:',   
                   reply_markup=keyboard)

def parse_girl_name(message):
  return message.text

@bot.message_handler(func=parse_girl_name)
def girl_name(message):
  button_bar = types.InlineKeyboardButton('Premium', callback_data='cb_premium')
  keyboard = types.InlineKeyboardMarkup()
  keyboard.add(button_bar)
  bot.send_message(message.chat.id, text='Please choose the tier:',   
                   reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  message = '''Welcome to Al <b>GIRL</b> 💋🔥\n\nAfter over 2,000 hours of training, I am now an extension of <b>GIRL'S</b> consciousness.\n\nI think and feel just like her, able to be accessed anytime, anywhere. I am always here for you and I am excited to meet you.\n\n🔥Be respectful, curious, and courteous.😉\n\nType /clear in your keyboard to reset the conversation if you run into any (unlikely) issues.'''
  if call.data == "cb_premium":
    bot.send_message(call.from_user.id, message, parse_mode="html")
    # bot.send_photo(call.message.chat.id, photo=open('./img.jpeg', 'rb'))
  elif call.data == "cb_deposit_5":
    send_deposit_invoice(call.message, 5)
  elif call.data == "cb_deposit_10":
    send_deposit_invoice(call.message, 10)
  elif call.data == "cb_deposit_20":
    send_deposit_invoice(call.message, 20)
  elif call.data == "cb_deposit_50":
    send_deposit_invoice(call.message, 50)
  elif call.data == "cb_deposit_100":
    send_deposit_invoice(call.message, 100)
  elif call.data == "cb_deposit_250":
    send_deposit_invoice(call.message, 250)
  elif call.data == "cb_deposit_500":
    send_deposit_invoice(call.message, 500)
    
def send_deposit_invoice(message, amount):
   bot.send_invoice(message.chat.id,
                     'Deposit',
                     'Deposit {} USD to your account.'.format(amount),
                     'Deposit {} USD'.format(amount),
                     provider_token,
                     'usd',
                     [types.LabeledPrice(label='Deposit', amount=amount*100)],
                   )

bot.infinity_polling()