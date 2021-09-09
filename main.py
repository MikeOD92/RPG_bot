##### imports
from replit import db
import discord
import os
import requests
import json
import random
import asyncio

### bot/ client  class 
class MyClient(discord.Client):

  async def on_ready(self):
    print('Logged in as')
    print(self.user.name)
    print('------')
  
  async def dice(self, input, message):
      roll = input.split('roll', 1)[1]

      if(roll.split('d')[0] == " " or roll.split('d')[0] == "" ):
        num = 1
      else:
        num = int(roll.split('d')[0])

      sides = int(roll.split('d')[1])

      await message.channel.send(str(message.author) + " rolled " +str(roll))
      
      total = 0

      while num > 0:
        rolled_num = random.randint(1,sides)
        total = rolled_num + total
        await message.channel.send(rolled_num)
        num -= 1

      await message.channel.send('total val is ' + str(total))  
      return total

  async def on_message(self, message):

    if message.author.id == self.user.id:
      return
    
    msg = message.content

    if msg.startswith('/hey'):
      await message.channel.send(f'Hello it is I {self.user.name}')
    
    if msg.startswith('/roll'):
      roll = msg.split('/roll', 1)[1]

      if(roll.split('d')[0] == " " or roll.split('d')[0] == "" ):
        num = 1
      else:
        num = int(roll.split('d')[0])

      sides = int(roll.split('d')[1])

      await message.channel.send(str(message.author) + " rolled " +str(roll))
      
      total = 0

      while num > 0:
        rolled_num = random.randint(1,sides)
        total = rolled_num + total
        await message.channel.send(rolled_num)
        num -= 1

      await message.channel.send('total val is ' + str(total))  
      return total
### build character sheet with charsheet class
    if msg.startswith('/create-char'):

      player_sheet = {
        "name": '',
        "look": '',
        "armor": 0,
        "hitpoints": 0, 
        "damage": 0,
        "strength": 0,
        "dexterity": 0,
        "constitution": 0,
        "inteligence": 0,
        "wisdom": 0,
        "charisma": 0
      }


      await message.channel.send('Hello Travler')
      await message.channel.send('What is your name ?')
      name = await client.wait_for('message')

      player_sheet["name"] = name.content

      await message.channel.send('Descibe your appearance.')
      look = await client.wait_for('message')

      player_sheet['look'] = look.content

      await message.channel.send('for now in character create roll without the /')
      # armor 
      player_sheet['armor'] = 0
      #hitpoints
      player_sheet['hitpoint'] = 0
      #damage
      player_sheet['damage'] = 0

      await message.channel.send("roll for your strength")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      player_sheet['strength'] = dice_roll

      await message.channel.send("roll for your dexterity")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      player_sheet['dexterity'] = dice_roll


      await message.channel.send("roll for your constitution")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      player_sheet['contitution'] = dice_roll


      await message.channel.send("roll for your inteligence")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      player_sheet['inteligence'] = dice_roll


      await message.channel.send("roll for your wisdom")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      player_sheet['wisdom'] = dice_roll


      await message.channel.send("roll for your charisma")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      player_sheet['chrisma'] = dice_roll

      await message.channel.send('player sheet:')
      await message.channel.send(player_sheet.items())

    


client = MyClient()
client.run(os.environ['TOKEN'])

    
  


