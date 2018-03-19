import discord
import youtube_dl

client = discord.Client()

@client.event
async def on_ready():
    print ("Estou Online!")

@client.event
async def on_message(message):
    if message.content.lower().startswith('!shop'):
        await client.send_message(message.channel, "Shopping não!!!")

    if message.content.lower().startswith('!music'):
        msgArray = []
        msgArray = message.content.split()
        voice = await client.join_voice_channel(client.get_channel('425083604721336324'))
        player = await voice.create_ytdl_player(msgArray[1])
        player.play()

            

@client.event
async def on_member_join(member):
    channelId = client.get_channel("425083604721336322")
    msg = "Alá! o {} chegou!".format(member.mention)
    await client.send_message(channelId, msg)

    

client.run('NDI1MTExNDIzMzI5NTAxMjE1.DZCrcA.e-OZAY-6rvHa3TQP9TmF6ss7N_4')