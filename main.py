import discord
import asyncio
from discord.ext import commands
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

export POKEMONTCG_IO_API_KEY='5be6b7cb-0bdc-4053-9db7-080758b8d6de'

# Discord Bot Status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pcg info"))