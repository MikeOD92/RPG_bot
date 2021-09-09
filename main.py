##### imports
from replit import db
import discord
import os
import requests
import json
import random
import asyncio

### Client 
# client = discord.Client()

##### charsheet class

class Charsheet:



  def __init__(self, sheet):
  #  name, look, armor, hitpoints, damage, strength, dexterity, constitution, inteligence, wisdom, charisma ):
      self.sheet = {
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
    # self.name = ""
    # self.look = ""
    # self.armor = 0
    # self.hitpoints = 0 
    # self.damage = 0
    # self.strength = 0
    # self.dexterity = 0
    # self.constitution = 0
    # self.inteligence = 0
    # self.wisdom = 0
    # self.charisma = 0

  def generate(self):
    print ("this function will build out the chacter sheet with the players dice roll when we instansiate a need instance of the charsheet class")
    ## we can shave the final instance of the new class in the DB under a key with the message sender how starts this process name
   

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

      # player_vars = []
      player_sheet = Charsheet({})

      await message.channel.send('Hello Travler')
      # player_sheet.generate() should this be a function on the sheet or should we loop over the player_shet var, or just build and array that follows the sheet patterna and then spread that array into the player sheet var and save in DB. 
      await message.channel.send('What is your name ?')
      name = await client.wait_for('message')
      # player_vars.append(name.content)
      player_sheet.sheet[name] = name.content

      await message.channel.send('Descibe your appearance.')
      look = await client.wait_for('message')
      # player_vars.append(look.content)
      player_sheet.sheet['look'] = look.content

      await message.channel.send('for now in character create roll without the /')
      # armor 
      # player_vars.append(0)
      player_sheet.sheet['armor'] = 0
      #hitpoints
      # player_vars.append(0)
      player_sheet.sheet['hitpoint'] = 0
      #damage
      # player_vars.append(0)
      player_sheet.sheet['damage'] = 0

      await message.channel.send("roll for your strength")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      # player_vars.append(dice_roll)
      player_sheet.sheet['strength'] = dice_roll

      await message.channel.send("roll for your dexterity")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      # player_vars.append(dice_roll)
      player_sheet.sheet['dexterity'] = dice_roll


      await message.channel.send("roll for your constitution")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      # player_vars.append(dice_roll)
      player_sheet.sheet['contitution'] = dice_roll


      await message.channel.send("roll for your inteligence")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      # player_vars.append(dice_roll)
      player_sheet.sheet['inteligence'] = dice_roll


      await message.channel.send("roll for your wisdom")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      # player_vars.append(dice_roll)
      player_sheet.sheet['wisdom'] = dice_roll


      await message.channel.send("roll for your charisma")
      roll = await client.wait_for('message')
      dice_roll = await self.dice(roll.content, message)

      # player_vars.append(dice_roll)
      player_sheet.sheet['chrisma'] = dice_roll


      # player_sheet = Charsheet(*player_vars)

      # await message.channel.send(player_sheet.keys())
      await message.channel.send('player sheet:')
      await message.channel.send(player_sheet.sheet.items())
      # for i in player_sheet.sheet:
      #   await message.channel.send(f"{i} : {player_sheet[i]}")

    


client = MyClient()
client.run(os.environ['TOKEN'])

    
  


