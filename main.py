import discord

cliente = discord.Client()

@cliente.event
async def on_ready():
    print ("Estou Online!")

@cliente.event
async def on_message(message):
    if message.content.lower().startswith('!shop'):
        await cliente.send_message(message.channel, "Shopping não!!!")    


cliente.run('NDI1MTExNDIzMzI5NTAxMjE1.DZCrcA.e-OZAY-6rvHa3TQP9TmF6ss7N_4')