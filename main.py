import discord
from discord.ext import commands
import asyncio
import settings
from typing import Optional
import random
import shaturanga

client = settings.discord_init("sl!")
@client.command()
async def toolkit(ctx, category: Optional[str] = None):
    role = await ctx.guild.create_role(name="toolkit")
    if role is None:
        if ctx.channel.permissions_for(ctx.author).administrator:
            if category is not None:
                await ctx.guild.create_category(name=category)
            channel = discord.utils.get(ctx.guild.channels, name="toolkit")
            if channel is None:

                tool = await ctx.guild.create_text_channel(name="toolkit")

                await tool.set_permissions(
                    discord.utils.get(ctx.guild.roles, name="toolkit"), view_channel = True
                    )
                await tool.set_permissions(
                    discord.utils.get(ctx.guild.roles, name="@everyone"), view_channel = False
                    )
                await tool.set_permissions(
                    discord.utils.get(ctx.guild.roles, name="Spotlight"), view_channel = True
                    )
                await tool.set_permissions(
                    discord.utils.get(ctx.guild.roles, name="Spotlight"), send_messages = True
                    )
    else:
        await ctx.send("Toolkit já criado.")

@client.command()
async def showcase(ctx, context, title: Optional[str] = None ,desc: Optional[str] = "Nenhum"):
        
        if context is None:
            if title is not None or title is None:
                context = ctx.author.name
        elif context == "custom":
            context = title
            
        role = discord.utils.get(ctx.guild.roles, name=ctx.author.name)
        if role is None:

            role = await ctx.guild.create_role(name=ctx.author.name)                                                
            await ctx.author.add_roles(role)

            created_embed = discord.Embed(
            title= "Informação",
            description="Showcase criada.",
            )  

            showcase_embed = discord.Embed(
                title= "Showcase de {}".format(ctx.author.name),
                description=desc
            )  

            pv_channel = await ctx.guild.create_text_channel(name=context)
            default = discord.utils.get(ctx.guild.roles, name="@everyone")

            await pv_channel.set_permissions(default, send_messages = False)  
            await pv_channel.set_permissions(role, send_message = True)
            await pv_channel.set_permission(discord.utils.get(ctx.guild.roles, name="Spotlight"), send_message = True)

            await asyncio.sleep(1)
            try:
                await ctx.send(embed = created_embed)
                await pv_channel.send(embed = showcase_embed)
            except AttributeError:
                await ctx.send("Embed indisponível.")
        else:
            await ctx.send("Você já tem um showcase.")

@client.event
async def on_ready():
    settings.message("Iniciado", "green", client.user.name, client.user.id)

@client.command()
async def shaturanga(ctx, second_player):
    code = random.randint(1, 1000000000)
    role = discord.utils.get(ctx.guild.roles, name=int)
    if role is None:
        role = await ctx.guild.create_role(name=code)
        await ctx.author.add_roles(role)

        chess_ch = await ctx.guild.create_text_channel(name=code)
        await chess_ch.set_permissions(
                    discord.utils.get(ctx.guild.roles, name=second_player), send_messages = True
                    )
        
        await chess_ch.set_permissions(
            discord.utils.get(ctx.guild.roles, name="Member(s)"), send_messages = False
            )
    else:
        await ctx.send("Ocorreu algum erro.")


client.run("MTI2MzIxNTIzMzYxOTQ2NDI2Mg.Gwx4P-.8JMkX7KuKcqhWvTakuwru-aU59yGdd9_b2xcXo")