import discord
from discord.ext import commands
import requests
import xml.etree.ElementTree as ET 
import csv
from datetime import datetime
import os

intents = discord.Intents.default()
intents.message_content = True
BOT_TOKEN = 'MTE1MzAxMzU2MDQ5MDg1NjU2OA.G_M2I3.LCN9zZ5ONXhmRx3G2f1EU6b5-WOYD8_xV0vqBw'

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged as {bot.user.name}')


@bot.command(name='livescore')
async def get_live_score(ctx):
    url = 'http://static.cricinfo.com/rss/livescores.xml'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            root = ET.fromstring(response.text)
            items = root.findall('.//item')

            if not items:
                await ctx.send('No live scores available.')
                return

            
            first_match = items[0]
            match_title = first_match.find('title').text
            match_description = first_match.find('description').text
    
            team_names_scores = match_title.split(' v ')
            team1_name_score = team_names_scores[0]
            team2_name_score = team_names_scores[1]
            
            summary = ""
            if '*' in team1_name_score:
                summary = "Team 1 chose to bat"
            elif '*' in team2_name_score:
                summary = "Team 2 chose to bat"
            else:
                summary="Not yet decided"
    
    
            
            await ctx.send(
                f'Team 1: {team1_name_score} \n'
                f'Team 2: {team2_name_score} \n'
                f'Summary: {summary}'
            )
            csv_file = 'cricket_scores.csv'
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Team 1', 'Team 2'])
                writer.writerow([team1_name_score, team2_name_score])

        except Exception as e:
            await ctx.send('Failed to fetch live scores. Error: ' + str(e))
    else:
        await ctx.send('Failed to fetch live scores. Status code not 200.')


@bot.command(name='generate')
async def generate_csv(ctx):
    csv_file = 'cricket_scores.csv'
    if os.path.isfile(csv_file):
        await ctx.send(file=discord.File(csv_file))
    else:
        await ctx.send('CSV file not found. Run the /livescore command to create it.')

@bot.command(name='help')
async def bot_help(ctx):
    help_message = '''
    **Commands:**
    `/livescore` - Get the live cricket score.
    `/generate` - Generate a CSV file with live scores.
    `/help` - Show this help message.
    '''
    await ctx.send(help_message)

bot.run(BOT_TOKEN)
