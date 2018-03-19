import discord
import youtube_dl
import asyncio

class MusicPlayer():
    def __init__(self, client:discord.Client):
        self.client = client
        
    async def entra_canal(self):
        canalId = client.get_channel('425083604721336324')
        self.voice = await client.join_voice_channel(canalId)
    
    async def toca_musica(self, string):
        player = await self.voice.create_ytdl_player(string)
        player.start()
              
    async def para_musica():
        player = await self.voice.create_ytdl_player(string)
        player.stop()    