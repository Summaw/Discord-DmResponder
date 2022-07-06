import discord

client = discord.Client()
sent = []

@client.event
async def on_ready():
 print('Bot is ready')

@client.event
async def on_message(message):
    print(message.content)
    if isinstance(message.channel, discord.channel.TextChannel) and message.author != client.user and 'hi' in message.content.lower() and message.author.id not in sent:
        await message.author.send('Hi!')
        
    elif isinstance(message.channel, discord.channel.DMChannel) and message.author != client.user and message.author.id not in sent:
        sent.append(message.author.id)
        await message.author.send('Do you know about olympus?')
        await client.wait_for("message", check=lambda m: m.author == message.author)
        await message.channel.send('Well you can learn about at https://discord.gg/theolympus')

client.run("")
