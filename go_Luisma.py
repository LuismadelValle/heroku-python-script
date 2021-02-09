
from telethon import TelegramClient, events
import time
import random
import asyncio
import re
import time
from random import uniform

on = True
adviser = 'Jaeger'
lvl = 1

state = False

loop = asyncio.get_event_loop()

api_id = 1384047
api_hash = 'ff7833fe3651498aa36eb6f6212f3d6a'
phone='LuismaPhone'
client=TelegramClient(phone,api_id,api_hash)

client.start()

@client.on(events.NewMessage(chats=('chtwrsbot'), incoming = True))
async def my_event_handler(event):
    if 'You were strolling around on your horse when you noticed' in event.raw_text:
        time.sleep(random.randint(30, 60))
        #await client.send_message('chtwrsbot', '/go')
        buttons = await event.get_buttons()
        for bline in buttons:
            for button in bline:
                if 'Intervene' in button.button.text:
                    await button.click()
    #if 'To accept their offer, you shall' in event.raw_text:
        #time.sleep(random.randint(30, 50))
        #await client.send_message('chtwrsbot', '/pledge')
    if 'has ordered Steel mold' in event.raw_text:
        await client.forward_messages(-1001467982915, event.message)
    if on and 'Advisers available for hire' in event.raw_text:
        lines = event.raw_text.splitlines()
        link = None
        gold = 999999
        link_re = re.compile('(/adv_\w{4})')
        gold_re = re.compile('(\d{3})')
        for line in lines:
            if f'lvl.{lvl} {adviser}' in line:
                act_link = link_re.search(line).group()
                act_gold = int(gold_re.search(line).group()) 
                if gold > act_gold:
                    link = act_link
                    gold = act_gold
        if link is not None:
            await client.send_message('chtwrsbot', link)
    elif on and 'Hire: /g_hire' in event.raw_text:
        link = re.search('(/g_hire \w{4})', event.raw_text).group()
        await client.send_message('chtwrsbot', link)
    if '/g_pay' in event.raw_text:
        state = True
        lines = event.raw_text.splitlines()
        for line in lines:
            time.sleep(uniform(8,12))
            link = re.search('/g_pay \w{4}', line).group()
            await client.send_message('chtwrsbot', link)   
    if state and '/g_pay' in text.raw_text:
        state = False
        await client.send_message(-1001467982915, 'invalid action')
    if 'Successfully funded!' in event.raw_text:
        await client.forward_message(-1001467982915, event.message)
            

@client.on(events.NewMessage(chats=(728204488)))
async def my_event_handler(event):
    global on
    global adviser
    global lvl
    m = re.search('([a-zA-Z]+) lvl (\d)', event.raw_text)
    if m is not None:
        on = True
        adviser, lvl = m.groups()
        adviser = adviser.capitalize()
    elif 'off' in event.raw_text:
        on = False
    elif 'on' in event.raw_text:
        on = True

@client.on(events.NewMessage(chats=(-1001467982915)))
async def my_event_handler(event):
    if 'g_pay' in event.raw_text:
        await client.send_message('chtwrsbot', event.raw_text)
    if 'invalid action' in event.raw_text:
        await client.send_message(-1001467982915, '@HhH_cuba Hectoooooooooooooor falta money')

loop.run_forever()


    
