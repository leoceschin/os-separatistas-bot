import discord
import youtube_dl
import random
#import music

client = discord.Client()
#musicPlayer = Music(client)

@client.event
async def on_ready():
    print ("Estou Online!")

@client.event
async def on_message(message):
    if message.content.lower().startswith('!shop'):
        await client.send_message(message.channel, "Shopping não!!!")

    if message.content.lower().startswith('!roll'):
        dice = random.randint(1, 6)
        resposta = ""
        if dice == 1:
            resposta = "Voce tirou {}!".format(dice)
        elif dice == 2:
            resposta = "Voce tirou {}!".format(dice)    
        elif dice == 3:
            resposta = "Voce tirou {}!".format(dice)
        elif dice == 4:
            resposta = "Voce tirou {}!".format(dice)
        elif dice == 5:
            resposta = "Voce tirou {}!".format(dice)
        else:
            resposta = "Voce tirou {}!".format(dice)

        await client.send_message(message.channel, resposta)

    #if message.content.lower().startswith('!music'):
    #    msgArray = []
    #    msgArray = message.content.split()
    #    musicPlayer.entra_canal().toca_musica(msgArray[1])

    if message.content.lower().startswith('!music'):
        msgArray = []
        msgArray = message.content.split()
        voice = await client.join_voice_channel(client.get_channel('425083604721336324'))
        player = await voice.create_ytdl_player(msgArray[1])
    player.start()

@client.event
async def on_member_join(member):
    channelId = client.get_channel("425083604721336322")
    msg = "Alá! o {} chegou!".format(member.mention)
    await client.send_message(channelId, msg)

client.run('NDI1MTExNDIzMzI5NTAxMjE1.DZCrcA.e-OZAY-6rvHa3TQP9TmF6ss7N_4')