import smtplib
from email.message import EmailMessage
import discord
import os
import asyncio
import json
from discord.ext import commands

with open('data.json') as f:
  data = json.load(f)
  
perfix = "Blank"

def get_prefix(client, message):

    prefixes = [perfix]

    return commands.when_mentioned_or(*prefixes)(client, message)

client = commands.Bot(command_prefix = get_prefix)

@client.event
async def on_ready():
    print('Bot Is Online And Ready To Roll!')
    print('----------------Info----------------')
    print('Username:', client.user.name)
    print('ID:', client.user.id)

client.remove_command('help')


def email_alert(subject, body, to):
  msg = EmailMessage()
  msg.set_content(body)
  msg['subject'] = subject
  msg['to'] = to

  user = "Email@gmail.com"
  msg['from'] = user
  password = "AppPassword"

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(user, password)
  server.send_message(msg)

  server.quit()

@client.event
async def on_message(message):
  if message.channel.id in data["Channels"]:
    os.system("clear")
    email_alert("Discord Channel", f"{message.channel.name}, {message.content}", "https://www.dialmycalls.com/blog/send-text-messages-email-address")

client.run("Token", bot=False)
