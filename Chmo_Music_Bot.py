
import discord
from discord.ext import commands, tasks
import youtube_dl
from youtube_dl import YoutubeDL
from discord.utils import get
from discord import FFmpegPCMAudio




DSCRD_TKN = ("THERE SHOULD BE YOUR DISCORD TOKEN")

opus = discord.opus.load_opus("/Users/macbookpro/Downloads/ffmpeg")
intents = discord.Intents().all()
clients = discord.Client (intents=intents)
bot = commands.Bot(command_prefix = "/", intents = intents)


ytdl = youtube_dl.YoutubeDL ()


class  YTDLSource(discord.PCMVolumeTransformer):


    def __init__ (self, source, *, data, volume = 0.5):
        super().__init__(source,volume)
        self.data=data
        self.title = data.get('title') 
        self.url = ""

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'False', 'simulate': True, 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


@bot.command(name='join')
async def join(ctx):
    await ctx.send ("Привет,Лошара. команды - /play /pause /resume /leave")
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command(name='leave')
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command(name='play')
async def play(ctx, url):
    vc = await ctx.message.author.voice.channel.connect()
    await ctx.send ("Привет,Лошара. команды - /play /pause /resume /leave")
    await ctx.send ("DANILA LOX POD ETU MUZIKU EGO EBAL")

    with YoutubeDL(YDL_OPTIONS) as ydl:
        if 'https://' in url:
            info: ydl.extract_info(url, download=False)
        else:
            info = ydl.extract_info(f"ytsearch:{url}", download=False)["entries"][0]
    
    
    link= info ['formats'][0]['url']

    vc.play(discord.FFmpegPCMAudio(executable="/Users/macbookpro/Downloads/ffmpeg",source=link, **FFMPEG_OPTIONS))
    

@bot.command(name='pause')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    await ctx.send ("МАМКУ СВОЮ ЗАПАУЗИ, ИСПОЛЬЗУЙ /resume, чтобы возобновить музон")
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is on pause.")
    
@bot.command(name='resume')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    await ctx.send ("Мама тобой гордится, слушай своего Моргена")
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("Resuming...")
 


bot.run(DSCRD_TKN)