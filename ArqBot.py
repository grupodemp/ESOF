from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from datetime import date

import RPi.GPIO as gpio

import pygame, sys
import pygame.camera
import time, random
import requests
import json


gpio.setmode(gpio.BCM)

gpio.setup(26, gpio.OUT) #Luz1
gpio.setup(19, gpio.OUT) #Luz2
gpio.setup(13, gpio.OUT) #Luz3
gpio.setup(21, gpio.OUT) #Refri1
gpio.setup(20, gpio.OUT) #Refri2
gpio.setup(16, gpio.OUT) #Refri3

luz = [26,19,13]
refri = [21,20,16]

SAVEDIR = "/home/pi/Desktop/campy"

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (720,480))

x=1


def verify(bot,update):
    user = update.message.from_user.username
    print(user)
    if user != 'danielgomesgo':
        update.message.reply_text('Você não tem permissões necessárias para utilizar o ArqBot')
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open('/home/pi/Desktop/notpass.png', 'rb'))
        while 1:
            update.message.reply_text('Sai daqui')
def hello(bot, update):
    update.message.reply_text(
        'Utilize /manual para ver as opções')
    
def start(bot, update):
    update.message.reply_text('Olá {}, eu sou o ArqBot e vou te ajudar em algumas tarefas!'.format(update.message.from_user.first_name))
    verify(bot,update)
    update.message.reply_text('Utilize o /manual')
def TakeShot(bot, update):
   update.message.reply_text("Tirando uma foto...")
   cam.start()
   image = cam.get_image()
   cam.stop()

   timestamp = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
   filename = ("%s/%s.jpg" % (SAVEDIR,timestamp))
   print ("saving into %s" % filename)
   pygame.image.save(image, filename)
   
   bot.sendPhoto(chat_id=update.message.chat_id, photo=open(filename, 'rb'))

def clima(bot, update, args):
   cidade = ' '.join(args).upper()
   resposta = ("Pesquisando clima de %s" %cidade)
   update.message.reply_text(resposta)
   
   requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=e5d9b5f5d36defff90206c1f4c8679f8')

   tempo = json.loads(requisicao.text)
   print('Condição do tempo: ', tempo['weather'][0]['main'])
   print('Temperatura: ', float(tempo['main']['temp']) - 273.15)
   tempox = str(tempo['weather'][0]['main'])
 
   temperatura = float(tempo['main']['temp'])-273.15
   temperatura = str(float('%.2f' %temperatura))
   print(tempox)
   print(temperatura)
   if (cidade == 'ROB'):
   		update.message.reply_text("Acho que está rolando um clima entre nós")
   		update.message.reply_text("Eu sou muito quente")
   else:
   		update.message.reply_text(tempox)
   		update.message.reply_text(temperatura)
def acendeluz(bot, update, args):
    print(args)
    a = ''.join(args)
    print(a)
    if a == '1':
        gpio.output(26, gpio.HIGH)
        update.message.reply_text("Luz 1 acesa")
    elif a == '2':
        gpio.output(19, gpio.HIGH)
        update.message.reply_text("Luz 2 acesa")
    elif a == '3':
        gpio.output(13, gpio.HIGH)
        update.message.reply_text("Luz 3 acesa")

    
def apagaluz(bot, update, args):
    print(args)
    a = ''.join(args)
    print(a)
    if a == '1':
        gpio.output(26, gpio.LOW)
        update.message.reply_text("Luz 1 apagada")
    elif a == '2':
        gpio.output(19, gpio.LOW)
        update.message.reply_text("Luz 2 apagada")
    elif a == '3':
        gpio.output(13, gpio.LOW)
        update.message.reply_text("Luz 3 apagada")

def ligarefrigerador(bot, update, args):
    print(args)
    num = ''.join(args)
    print(num)
    if num == '1':
        gpio.output(21, gpio.HIGH)
        update.message.reply_text("Refrigerador 1 ligado")
    elif num == '2':
        gpio.output(20, gpio.HIGH)
        update.message.reply_text("Refrigerador 2 ligado")
    elif num == '3':
        gpio.output(16, gpio.HIGH)
        update.message.reply_text("Refrigerador 3 ligado")
        
def desligarefrigerador(bot, update, args):
    print(args)
    num = ''.join(args)
    print(num)
    if num == '1':
        gpio.output(21, gpio.LOW)
        update.message.reply_text("Refrigerador 1 desligado")
    elif num == '2':
        gpio.output(20, gpio.LOW)
        update.message.reply_text("Refrigerador 2 desligado")
    elif num == '3':
        gpio.output(16, gpio.LOW)
        update.message.reply_text("Refrigerador 3 desligado")
        
def data(bot, update):
    hj = date.today()
    hj_dia = str(hj.day)
    hj_mes = str(hj.month)
    hj_ano = str(hj.year)   
    hj_data = [hj_dia, hj_mes, hj_ano]
    print(hj_data)
    hj_data = '/'.join(hj_data)
    update.message.reply_text(hj_data)
	
def addtarefa(bot, update, args):
    arq = open("tarefas.txt", "r")
    texto = args
    print(texto)
    a = ' '.join(texto)
    print(a)
    conteudo = arq.readlines()
    conteudo.append(a)
    arq = open("tarefas.txt", "w")
    arq.writelines(conteudo)
    arq.write("\n")
    arq.close()
    update.message.reply_text("Tarefa adicionada!")
    
def vertarefas(bot, update):
    arq = open("tarefas.txt", "r")
    linhas = '\n'.join(arq.readlines())
    if (linhas == ''):
        update.message.reply_text("Nenhuma tarefa a ser exibida")
        arq.close()
    else:
        update.message.reply_text("Estas são as suas tarefas:")
               
        update.message.reply_text(linhas)
    arq.close()
    
def rmtarefas(bot, update):
    arq = open('tarefas.txt', 'w')
    arq.close()
    update.message.reply_text("Tarefas apagadas!")
        
            
def manual(bot, update):
    update.message.reply_text("""   
       Utilize os comandos:
       /start para iniciar;
       /hello para cumprimentar o bot;
       /data para ver a data de hoje;
       /takeshot para receber uma foto instantanea;
       /clima para ver clima de alguma cidade
       /addtarefa para adicionar uma nova tarefa;
       /vertarefas para ver todas as suas tarefas;
       /rmtarefas para apagar a lista de tarefas;
       /acendeluz + número para acender a lâmpada selecionada;
       /ligarefrigerador + número para ligar o refrigerador selecionado;
       /apagaluz + número para apagar a lâmpada selecionada;
       /desligarefrigerador + número para desligar o refrigerador selecionado.""")

updater = Updater('430702176:AAEJPafezay7XIVxX8TvNauUyEIOJgwvW5o')

def main():
    updater.dispatcher.add_handler(CommandHandler('takeshot', TakeShot))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('manual', manual))
    updater.dispatcher.add_handler(CommandHandler('clima', clima, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('data', data))
    updater.dispatcher.add_handler(CommandHandler('addtarefa', addtarefa, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('vertarefas', vertarefas))
    updater.dispatcher.add_handler(CommandHandler('rmtarefas', rmtarefas))
    updater.dispatcher.add_handler(CommandHandler('acendeluz', acendeluz, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('apagaluz', apagaluz, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('ligarefrigerador', ligarefrigerador, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('desligarefrigerador', desligarefrigerador, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('verify', verify))
        
main()

updater.start_polling()
updater.idle()
