import telebot
from flask import Flask

app= Flask(__name__)

chave_API="6526434080:AAHaT_qARephRnaX7geuZavbTYyynvPODUs"
bot = telebot.TeleBot(chave_API)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
   bot.send_message(mensagem.chat.id,"Fica numa de numa vais ja ter a tua pizza")


@bot.message_handler(commands=["Hamburguer"])
def Hnaburguer(mensagem):
   bot.send_message(mensagem.chat.id,"Fica numa de numa vai ja ter o teu buega de se lambuzar")


@bot.message_handler(commands=["Salada"])
def Salada(mensagem):
   bot.send_message(mensagem.chat.id,"Tché tas a se dar de fino. Assim tas pedi salada tipo que tas de dieta?! Clica mbora aqui para voltar no inicio ->/iniciar")



@bot.message_handler(commands=["Opcao1"])
def opcao1(mensagem):
    texto="""
          O que voce quer? (Clique no item):
          /pizza pizza
          /Hamburguer Hamburguer
          /Salada Salada """
    bot.send_message(mensagem.chat.id,texto)


@bot.message_handler(commands=["Opcao2"])
def opcao2(mensagem):
   bot.send_message(mensagem.chat.id,"Para enviar uma reclamacao, mande um email para ...")


@bot.message_handler(commands=["Opcao3"])
def opcao3(mensagem):
   bot.reply_to(mensagem,"Um abraco tambem para ti")
   bot.send_message(mensagem.chat.id,"HHHHAAAA")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)#serve para decidir quando é que a funcao def responder_mensagens(mensagem): de ser chamada
def responder_mensagens(mensagem):
    texto="""Escolha uma opcao para continuar(clique no item):
    /Opcao1 Fazer um pedido
    /Opcao2 Reclamar de um pedido
    /Opcao3 Mandar um abraco pro ...
    Responder qualquer outra coisa nao vai funcionar, clique em uma das opcoes
          
"""
    bot.reply_to(mensagem,texto)
    


bot.polling()
app.run(debug=True)
