import os
import telebot

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Ola! Tudo bem? Meu nome e Oli! Eu sou a assistente virtual da Olist. Nao se preocupe, eu vou te ajudar nas tuas duvidas. \n Digite o numero da opcao referente ao segmento para te ajudarmos a fazer o cadastro do seu produto:\n1. Tecnologia\n2. Beleza\n3. Viagem\n4. Moveis\n5. Pet\n6. Educacao\n7. Outros")

@bot.message_handler(commands=['1','2','3','4','5','6','7'])
def send_message(message):
    bot.reply(message,"Ha! Que legal! Qual produto voce quer cadastrar?")

@bot.message_handler(func=lambda message: True)
def send_message(message):
    bot.reply(message,"Entendi. Vou te mandar um video com uma explicacao completa sobre o cadastro do seu produto.\n\nSe prepare para incluir as seguintes informacoes sobre seu produto: \n-Titulo\n-Foto(s) com fundo branco\n-Descricao\n-Categoria\n-Medida da embalagem\n\nNao esqueca que o titulo, as fotos e a descricao, devem ser bem claros e objetivos.\n https://www.youtube.com/watch?v=8rp2py-eK2I")

bot.polling()
