import discord
from discord.ext import commands
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.members = True

TOKEN = 'BotToken' #봇 토큰 넣기

date = 20 #추방 조건

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name}에 로그인')

@bot.event
async def on_member_join(member):
    account_age = datetime.utcnow() - member.created_at
    if account_age.days < date:
        dm_embed = discord.Embed(
            title="할말",
            description="할말",
            color=discord.Color.gold()
        )
        dm_embed.add_field(name="할말", value=member.created_at.strftime("%Y년 %m월 %d일"))
        dm_embed.add_field(name="할말", value="할말")
        dm_embed.set_footer(text="할말")

        try:
            await member.send(embed=dm_embed)
        except discord.HTTPException:
            pass

        await member.kick(reason="계정 생성일이" f"{date}일 미만입니다.")

bot.run(TOKEN)
