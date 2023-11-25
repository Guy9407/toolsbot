import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import random
import glob, os, os.path
import sys
import fileinput
import asyncio
import string
from itertools import cycle

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())  #defining our client
client.remove_command('help') # removes the basic help command

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('----------------------------')
    print(f'ID: {client.user.id}')
    print('----------------------------')
    print(f'Guilds: {len(client.guilds)}')
    print('----------------------------')
    print(f'Members: {len(set(client.get_all_members()))}')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('with NATI'))
    try:
        await client.tree.sync()
    except Exception as e:
        print(e)



@client.tree.command(name="say", description="say something as kipud")
async def say(ctx = discord.interactions,*, message: str):
    await ctx.response.send_message('k', ephemeral=True,delete_after=0.1)
    channel = ctx.channel
    await ctx.channel.send(message)



@client.event
async def on_guild_join(guild):
    open(f"./MuteRoles/{guild.id}-mute-role.txt", "x")
    channel = client.get_channel(697830313879011389)
    await channel.send(f'New guild: **{guild.name}** (ID: **{guild.id}**)')
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
        client.user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }
    channel = await guild.create_text_channel(name='welcome-tools', overwrites=overwrites)
    welcome_embed = discord.Embed(color=0xfd9fb9, title=':wave: Hey there!', description="Thanks for adding me to the server! \n \nOk, let's start with some basic information. I'd suggest setting up some stuff first. No worries, I'll help you.\n \nLet's start with setting up a log channel. You can simply do that, by typing the following command: \n**!setlog [channel]** \n \nGreat, let's move on. The next you can do, is setting up a welcome message and a welcome channel. There are some really useful parameters, that you can use for this. Let me show it to you: \n **!setmsg Hey {mention}! Welcome to {guild}, you're member number {members}!** \n \nLet's set up a channel for this messages: \n**!setwelcome [channel]** \n \nSweet! So, the last thing we should do, is tp set up a mute role. This is also very simple, just to the following: \n**!muterole [role]** \n \nRemember to **__not__** include the **[ ]** when you're executing the commands. \n \nAnyway, looks like we set up everything! If you still have any questions, feel free to msg the creator (guyod on discord).\n \nFeel free to delete this channel. You can see all my commands, by typing **!help** into a channel.")
    await channel.send(embed=welcome_embed)

@client.event
async def on_guild_remove(guild): # when the bot gets removed from a guild 
    channel = client.get_channel(697830245725896705)
    await channel.send(f'Removed from guild: **{guild.name}** (ID: **{guild.id}**)')

@client.command()
@commands.has_permissions(administrator=True)
async def biscuit(ctx):
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/biskut-biscuits-snacks-gif-12926857")

@client.command()
@commands.has_permissions(manage_messages=True)
async def ping(ctx):
    bot_latency= round(client.latency * 1000)
    await ctx.send(f"Pong! {bot_latency} ms.")

@client.command()
async def corn(ctx):
    welcome_embed = discord.Embed(color=0xfd9fb9, title='<a:Wave:723567545927335957> Hey there!', description="Thanks for adding me to the server! <a:Dance:723567543096311892> \n \nOk, let's start with some basic information. I'd suggest setting up some stuff first. No worries, I'll help you.\n \nLet's start with setting up a log channel. You can simply do that, by typing the following command: \n**!setlog [channel]** \n \nGreat, let's move on. The next you can do, is setting up a welcome message and a welcome channel. There are some really useful parameters, that you can use for this. Let me show it to you: \n **!setmsg Hey {mention}! Welcome to {guild}, you're member number {members}!** \n \nLet's set up a channel for this messages: \n**!setwelcome [channel]** \n \nSweet! So, the last thing we should do, is tp set up a mute role. This is also very simple, just to the following: \n**!muterole [role]** \n \nRemember to **__not__** include the **[ ]** when you're executing the commands. \n \nAnyway, looks like we set up everything! If you still have any questions, feel free to dm the creator. guyod on discord. \n \nFeel free to delete this channel. You can see all my commands, by typing **!help dm** into a channel.")
    await ctx.send(embed=welcome_embed)

@client.command()
async def rulesetx(ctx):
    welcome_embed = discord.Embed(color=0xfd9fb9, title='RULES', description='**חוקי השרת**\n 1. נא לשמור על כבוד. מותר לצחוק, ומותר לדבר בכל צורה שבה כל הצדדים בשיחה מסכימים לה.\n מצד שני, אינטרקציות אשר יתפסו כפוגעניות מספיק כלפי אחד הצדדים, או כלפי קבוצה ברורה אשר אינה נוכחת, יוענשו בהתאם, על פי שיקול דעת של הצד הנפגע (אם ישנו), ושל איש צוות.\n \n 2. לתוכן אשר מוגדר "לא ראוי" (NSFW, תוכן מיני או מזוויע ועוד), אין מקום בשרת\n ניתן לפנות לאדמין מחובר באישורו כדי לבדוק במקרה ספציפי שאינו חד וחלק, אם הדבר חשוב מספיק בשביל להצדיק את זה. ניצול מופרז או לא ראוי של סעיף זה יחשב עבירה על החוקים.\n 3. ספאם אשר יוגדר מופרז, יחשב כעבירה על החוקים, לשיקול דעתו של איש צוות.\n (לדוגמה - שליחת אותה הודעה שוב ושוב או הרבה הודעות ברצף ללא סיבה מוצדקת ואישור של איש צוות)\n\n4. מותר לקיים דיונים בשרת זה, כל עוד חבר צוות לא קובע שהדיון יוצא משליטה.\nבמידה וחבר צוות יגדיר את הנושא כיוצא משליטה, הדיון בתוך גבולות השרת יופסק מיידית.\nהפרה סדרתית של כלל זה, או אי ציות לבקשת חבר צוות בנושא תחשב כהפרת חוקי השרת.\n\n5. אין לפרסם בשרת זה.\nחל איסור על כל סוג פרסום בתוך גבולות השרת, וגם לאנשים מהשרת בפרטי.\n\n6. שרת זה הוא שרת דובר עברית ואנגלית בעיקר.\nדיבור מופרז בשפה אחרת ללא תרגום מדוייק מספיק מוצמד יחשב כספאם במידה ואין לו הצדקה ישירה.\nחל איסור להשתמש בתוכנות אשר משנות קול מכל סוג כלשהו.\n\n7. נא להימנע מתיוגים מיותרים של חברי השרת.\nכלל זה יאכף על פי תלונות של חברי השרת המתוייגים במידה ויעלו.\n\n8. פנייה לחברי שרת בפרטי ללא אישור קודם או סיבה מוצדקת תחשב כעבירה על חוקי השרת.\n\n9. לצוות השרת יש סמכות מלאה לאכוף את החוקים לפי שיקול דעתם.\nאם לדעתכם חלה טעות חמורה מספיק, ניתן לפנות לצוות הרלוונטי ולדבר על זה באופן פרטי.\nאין ליצור ויכוח ושיח פומבי לגבי ענייני אכיפה וענישה של אנשים אחרים. ענייני אכיפה הם דבר אישי, ואין שום הצדקה לגרור לתוכם אנשים אחרים.\nחל איסור על אלטים בשרת. אין לעקוף ענישה באמצעותם.\n\n10. שרת זה כפוף לכל תנאי השירות של דיסקורד.\nמי שמעוניין יכול לקרוא אותם כאן: <https://discord.com/terms>\n\n**אי ציות לחוקים יהווה ענישה על ידי צוות השרת בהתאם לחומרת העברה**\nאם יש לכם שאלות, אתם תמיד מוזמנים לפנות לצוות השרת')
    await ctx.send(embed=welcome_embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def help(ctx): #The help command
    help_embed=discord.Embed(color=0xfdfb9, title='Hey there', description="**Warn System** \nWARNING-If the user gets their 5th warn, they will automatically get banned** \n!warn `[mention or id]` `[reason]` **|** Warns the user \n!warnings `[mention or id]` **|** Shows the warnings of the user \n!clearwarns `[mention or id]` **|** Clears all warnings of the user\n \n**User Commands** \n!nickname `[ID or mention]` `[nickname]` **|** Changes the nickname of the member \n!hug `[mention or id]` **|** Hugs the user \n!fight `[mention or id]` **|** Fights the user\n \n**Mod Commands** \n!setlog `[ID or mention]` **|** Sets a log channel \n!softban `[ID or mention]` `[reason]`**|** Softbans a member \n!ban `[ID or mention]` `[reason]` **|** Bans a user \n!kick `[ID or mention]` `[reason]` **|** Kicks the user \n !clear `[amount]` **|** Clears a specific amount of messages \n!muterole `[role ID, mention or name]` **|** Sets a mute role \n!mute `[mention or ID]` `[time in minutes]` `[reason]` **|** Mutes a member for a specific amount of time \n!slowmode `[mention or ID]` `[time in seconds]` **|** Sets the channel slowmode \n!guildinfo **|** Shows info about the guild\n \n**Welcome System**- \n!setwelcome `[ID or mention]` **|** Sets a welcome channel \n!setmsg `[text]` **|** Sets a welcome message")
    await ctx.send(embed=help_embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def av(ctx, member: discord.Member = None): # shows the avatar
    if member == None:
        member = ctx.message.author
    elif member == member.id:
        member = member
    e = discord.Embed(color=0xfd9fb9)
    e.set_author(name=f"{member}'s avatar")
    e.set_image(url=member.avatar_url)
    e.set_footer(text=f'Invoked by {ctx.message.author}')
    await ctx.send(embed=e)

@client.command()
@commands.has_permissions(ban_members=True)
async def sm(ctx, channel: discord.TextChannel = None, *, time: int = None): # changes the slowmode
    if channel == None:
        e2 = discord.Embed(color=0xfd9fb9, description='Please mention a valid channel or enter a valid channel id!')
        e2.set_author(name='Error: Invalid channel', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e2)
        return
    if time == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please enter a valid time!')
        e3.set_author(name='Error: Invalid time', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if channel == channel.id:
        channel = channel
    await channel.edit(slowmode_delay=time)
    e4 = discord.Embed(color=0xfd9fb9, description=f'Succesfully changed the slowmode for {channel.mention} to **{time}** seconds!')
    e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)



@client.command()
@commands.has_permissions(manage_messages=True)
async def nickname(ctx, member: discord.Member = None, *, name = None): # changes the nickname 
    if name == None:
        e2 = discord.Embed(color=0xfd9fb9, description='Please mention a valid name!')
        e2.set_author(name='Error: Invalid name', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e2)
        return
    if member == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/img/4622')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    await member.edit(nick=name)
    e4 = discord.Embed(color=0xfd9fb9, description=f'Succesfully changed the nickname of {member.mention} to **{name}** seconds!')
    e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)



@client.command()
@commands.has_permissions(manage_messages=True)
async def info(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.message.author
    elif member == member.id:
        member = member
    roles = [role for role in member.roles]
    e4 = discord.Embed(color=0xfd9fb9, timestamp=ctx.message.created_at, description=f'[Avatar]({member.avatar_url})')
    e4.set_author(name=f'{member}', icon_url=member.avatar_url)
    e4.add_field(name=f'Roles ({len(roles)}):', value=f' '.join([role.mention for role in roles]), inline=False)
    e4.add_field(name='Created at:', value=f"{member.created_at.strftime('%a, %m/%e/%Y, %H:%M')}", inline=False)
    e4.add_field(name='Joined at:', value=f"{member.joined_at.strftime('%a, %m/%e/%Y, %H:%M')}", inline=False)
    e4.set_footer(text=f'User ID: {member.id}')
    await ctx.send(embed=e4)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = None):
    if amount == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please enter a valid amount of messages between 1 and 50')
        e3.set_author(name='Error: Invalid amount', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if amount > 50:
        e7 = discord.Embed(color=0xfd9fb9, description='Sorry, but I can only delete 50 messages at one time!')
        e7.set_author(name='Error: Too many messages', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e7)
        return
    await ctx.message.channel.purge(limit=amount)
    e4 = discord.Embed(color=0xfd9fb9, description=f'Successfully deleted **{amount}** messages in {ctx.message.channel.mention}!')
    e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)
    


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, reason = None):
    if member == ctx.message.author:
        e7 = discord.Embed(color=0xfd9fb9, description="Sorry, but you can't kick yourself!")
        e7.set_author(name='Error: Author', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e7)
        return
    if member == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    if reason == None:
        reason = 'No reason provided'
    e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
    e.set_author(name='User kicked')
    await member.kick(reason=reason)
    e4 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully kicked {member.mention} for **{reason}**!')
    e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)
    guild = ctx.message.guild
    f = open(f"{guild.id}-log.txt", "r")
    channel_id = f.read()
    log_channel = await client.fetch_channel(channel_id)
    await log_channel.send(embed=e)




@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, reason = None): # ban command
    if member == ctx.message.author:
        e7 = discord.Embed(color=0xfd9fb9, description="Sorry, but you can't ban yourself!")
        e7.set_author(name='Error: Author', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e7)
        return
    if member == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    if reason == None:
        reason = 'No reason provided'
    await member.ban(reason=reason)
    e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
    e.set_author(name='User banned')
    e4 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully banned {member.mention} for **{reason}**!')
    e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)
    guild = ctx.message.guild
    await client.send_message(member.id, 'yapp')
    f = open(f"{guild.id}-log.txt", "r")
    channel_id = f.read()
    log_channel = await client.fetch_channel(channel_id)
    await log_channel.send(embed=e)


@client.command()
@commands.has_permissions(ban_members=True)
async def bam(ctx, member: discord.Member = None, *, reason = None): # ban command
    if member == ctx.message.author:
        e7 = discord.Embed(color=0xfd9fb9, description="Sorry, but you can't bam yourself!")
        e7.set_author(name='Error: Author', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e7)
        return
    if member == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    if reason == None:
        reason = 'No reason provided'
    e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
    e.set_author(name='User bammed')
    e4 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully bammed {member.mention} for **{reason}**!')
    e4.set_author(name='BAMMED', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)
    guild = ctx.message.guild




@client.command()
@commands.has_permissions(administrator=True)
async def setlog(ctx, channel: discord.TextChannel = None): # sets a log channel
    if channel == None:
        e2 = discord.Embed(color=0xfd9fb9, description='Please mention a valid channel or enter a valid channel id!')
        e2.set_author(name='Error: Invalid channel', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e2)
        return
    guild = ctx.message.guild
    f = open(f"{guild.id}-log.txt", "w")
    f.write(f"{channel.id}")
    f.close()
    e4 = discord.Embed(color=0xfd9fb9, description=f'Successfully set the log channel to {channel.mention}!')
    e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)


@client.command()
@commands.has_permissions(ban_members=True)
async def removerole(ctx, member: discord.Member = None, *, role: discord.Role = None): # reoves a role
    if member == None:
        e2 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e2.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e2)
        return
    if role == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please enter a valid role name/id or mention a valid role!')
        e3.set_author(name='Error: Invalid role', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    if role == role.id:
        role = role
    await member.remove_roles(role)
    e4 = discord.Embed(color=0xfd9fb9, description=f'Successfully removed the role {role.mention} from {member.mention}!')
    e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)



@client.command()
@commands.has_permissions(ban_members=True)
async def addrole(ctx, member: discord.Member = None, *, role: discord.Role = None): # adds role
    if member == None:
        e2 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e2.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e2)
        return
    if role == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please enter a valid role name/id or mention a valid role!')
        e3.set_author(name='Error: Invalid role', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    if role == role.id:
        role = role
    await member.add_roles(role)
    e4 = discord.Embed(color=0xfd9fb9, description=f'Successfully added the role {role.mention} to {member.mention}!')
    e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)

@client.command()
@commands.has_permissions(kick_members=True)
async def warm(ctx, member: discord.Member = None, *, reason = None): # warms a member
    guild = ctx.message.guild
    if member == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == ctx.message.author:
        e7 = discord.Embed(color=0xfd9fb9, description="Sorry, but you can't warn yourself!")
        e7.set_author(name='Error: Author', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e7)
        return
    if member == member.id:
        member = member
    if reason == None:
        reason = 'No reason provided'
    e5 = discord.Embed(color=0xfd9fb9, description=f"{ctx.message.author.mention} successfully warmed {member.mention} for **{reason}**!")
    e5.set_author(name='WARMED', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e5)


@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member = None, *, reason = None): # warns a member
    guild = ctx.message.guild
    if member == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == ctx.message.author:
        e7 = discord.Embed(color=0xfd9fb9, description="Sorry, but you can't warn yourself!")
        e7.set_author(name='Error: Author', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e7)
        return
    if member == member.id:
        member = member
    if reason == None:
        reason = 'No reason provided'
    if not os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
        with open(f"{guild.id}-{member.id}-warns.txt", "w") as f10:
            f10.write("1")
            f10.close()
            e4 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully warned {member.mention} for **{reason}**!')
            e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e4)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'You have been warned by {ctx.message.author.mention} for **{reason}**. this is your 1st out 5 warnings.')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warned')
                await log_channel.send(embed=e)
                await member.send(embed=e010)
            else:
                pass
            return
    if os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
        f = open(f"{guild.id}-{member.id}-warns.txt", "r")
        global warns
        warns = f.read()
        if warns == '0':
            f2 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f2.write('1')
            f2.close()
            e5 = discord.Embed(color=0xfd9fb9, description=f"{ctx.message.author.mention} successfully warned {member.mention} for **{reason}**!")
            e5.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e5)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'You have been warned by {ctx.message.author.mention} for **{reason}**. this is your 1st out 5 warnings.')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warned')
                await log_channel.send(embed=e)
                await member.send(embed=e010)
            else:
                pass
            return
        if warns == '1':
            f3 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f3.write('2')
            f3.close()
            e6 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully warned {member.mention} for **{reason}**!')
            e6.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e6)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'You have been warned by {ctx.message.author.mention} for **{reason}**. this is your 2nd out 5 warnings.')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warned')
                await log_channel.send(embed=e)
                await member.send(embed=e010)
            else:
                pass
            return
        if warns == '2':
            f4 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f4.write('3')
            f4.close()
            e7 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully warned {member.mention} for **{reason}**!')
            e7.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e7)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'You have been warned by {ctx.message.author.mention} for **{reason}**. this is your 3rd out 5 warnings.')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warned')
                await log_channel.send(embed=e)
                await member.send(embed=e010)
            else:
                pass
            return
        if warns == '3':
            f5 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f5.write('4')
            f5.close()
            e8 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully warned {member.mention} for **{reason}**!')
            e8.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e8)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'You have been warned by {ctx.message.author.mention} for **{reason}**. this is your 4th and last warning out 5 warnings, you will be banned if you get one more warning')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warned')
                await log_channel.send(embed=e)
                await member.send(embed=e010)
            else:
                pass
            return
        if warns == '4':
            f6 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f6.write('0')
            f6.close()
            await member.ban(reason=reason)
            e9 = discord.Embed(color=0xfd9fb9, description=f"Looks like {member.mention} has been warned to often and now they're banned!")
            e9.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e9)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'You have been warned by {ctx.message.author.mention} for **{reason}**. this is your 5th warning and you have been banned.')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User banned (5 warns)')
                await log_channel.send(embed=e)
                await member.send(embed=e010)
        
@client.command()
@commands.has_permissions(kick_members=True)
async def warnremove(ctx, member: discord.Member = None, *, reason = None): # remove one warn off member
    guild = ctx.message.guild
    if member == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == ctx.message.author:
        e7 = discord.Embed(color=0xfd9fb9, description="Sorry, but you can't remove a warn  yourself!")
        e7.set_author(name='Error: Author', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e7)
        return
    if member == member.id:
        member = member
    if reason == None:
        reason = 'No reason provided'
    if not os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
            e4 = discord.Embed(color=0xfd9fb9, description=f'{member.mention} doesn`t have any warns to remove.')
            e4.set_author(name='No warns', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e4)
    else:
            pass
    if os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
        f = open(f"{guild.id}-{member.id}-warns.txt", "r")
        global warns
        warns = f.read()
        if warns == '0':
            e5 = discord.Embed(color=0xfd9fb9, description=f"{member.mention} doesn`t have any warns to remove.")
            e5.set_author(name='No warns', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e5)
        else:
            pass
        if warns == '1':
            f3 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f3.write('0')
            f3.close()
            e6 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully removed a warn from {member.mention} for **{reason}**!, they now have 0 warns.')
            e6.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e6)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'Your warn has been removed by {ctx.message.author.mention} for **{reason}**. you now have 0 warns.')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warn removed')
                await log_channel.send(embed=e)
                await member.send(embed=e010)
            else:
                pass
            return
        if warns == '2':
            f4 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f4.write('1')
            f4.close()
            e7 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully removed a warn from {member.mention} for **{reason}**!, they now have 1 warn.')
            e7.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e7)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'Your warn has been removed by {ctx.message.author.mention} for **{reason}**. you now have 1 warn.')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warn removed')
                await log_channel.send(embed=e)
                await member.send(embed=e010)
            else:
                pass
            return
        if warns == '3':
            f5 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f5.write('2')
            f5.close()
            e8 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully removed a warn from {member.mention} for **{reason}**!, they now have 2 warn.')
            e8.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e8)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'Your warn has been removed by {ctx.message.author.mention} for **{reason}**. you now have 2 warns.')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warn removed')
                await log_channel.send(embed=e)
                await member.send(embed=e010)
            else:
                pass
            return
        if warns == '4':
            f6 = open(f"{guild.id}-{member.id}-warns.txt", "w")
            f6.write('3')
            f6.close()
            e9 = discord.Embed(color=0xfd9fb9, description=f"{ctx.message.author.mention} successfully removed a warn from {member.mention} for **{reason}**!, they now have 2 warns.")
            e9.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
            await ctx.send(embed=e9)
            if os.path.exists(f"{guild.id}-log.txt"):
                e010 = discord.Embed(color=0x000000, description=f'Your warn has been removed by {ctx.message.author.mention} for **{reason}**. you now have 3 warns.')
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nReason: **{reason}**")
                e.set_author(name='User warn removed')
                await log_channel.send(embed=e)
                await member.send(embed=e010)


@client.command()
@commands.has_permissions(ban_members=True)
async def clearwarns(ctx, member: discord.Member = None): # clears the warnings of a member
    guild = ctx.message.guild
    if member == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    if os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
        f = open(f"{guild.id}-{member.id}-warns.txt", "w")
        f.write('0')
        e9 = discord.Embed(color=0xfd9fb9, description=f"Successfully cleard the warnings of {member.mention}!")
        e9.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
        await ctx.send(embed=e9)
        if os.path.exists(f"{guild.id}-log.txt"):
                f9 = open(f"{guild.id}-log.txt", "r")
                log_id = f9.read()
                log_channel = await client.fetch_channel(log_id)
                e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**)")
                e.set_author(name='Warns cleared')
                await log_channel.send(embed=e)
        else:
            pass
    else:
        await ctx.send('Looks like something went wrong...')




@client.command()
@commands.has_permissions(ban_members=True)
async def warnings(ctx, member: discord.Member = None): # shows the amount of warnings a member currently has
    guild = ctx.message.guild
    if member == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e3.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if member == member.id:
        member = member
    if os.path.exists(f"{guild.id}-{member.id}-warns.txt"):
        f = open(f"{guild.id}-{member.id}-warns.txt", "r")
        warns = f.read()
        e3 = discord.Embed(color=0xfd9fb9, description=f'{member.mention} currently has **{warns}** warning(s)!')
        await ctx.send(embed=e3)
    else:
        await ctx.send('Looks like something went wrong...')


@client.command()
@commands.has_permissions(ban_members=True)
async def guildinfo(ctx): # shows info about the guild
    g = ctx.guild
    e = discord.Embed(color=0xfd9fb9, title=f'__Guild info for {g.name}__', description=f'Name: **{g.name}** \nID: **{g.id}** \nOwner: {g.owner.mention} \nOwner ID: **{g.owner_id}** \n \nRoles: **{len(g.roles)}** \nEmojis: **{len(g.emojis)}** \n \nCategories: **{len(g.categories)}** \nVoice channels: **{len(g.voice_channels)}** \nText channels: **{len(g.text_channels)}** \n \nMax members: **{g.max_members}** \nMembers: **{len(g.members)}**')
    e.set_thumbnail(url=g.icon_url)
    e.set_footer(text=f'Invoked by {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=e)


@client.event
async def on_member_remove(member):
    guild = client.get_guild(712832986642645004)
    g = member.guild
    g2 = client.get_guild(701041308810084362)
    if g == guild:
        log = client.get_channel(713029013483946054)
        embed = discord.Embed(color=0x7289DA, description=f"**User has left the Server** \nUser Name: **{member}** \n \nUser ID: **{member.id}**")
        await log.send(embed=embed)
        return
    if g == g2:
        log2 = client.get_channel(701959960208343141)
        embed2 = discord.Embed(color=0x7289DA, description=f"**User has left the Server** \nUser Name: **{member}** \n \nUser ID: **{member.id}**")
        await log2.send(embed=embed2)
        return


@client.command()
@commands.has_permissions(administrator=True)
async def hug(ctx, member: discord.Member = None): # hug a member
    if member == None:
        await ctx.send('Who do you want to hug?')
        return
    if member == ctx.message.author:
        await ctx.send("Sorry, but you can't hug yourself.")
        return
    if member == member.id:
        member = member
    await ctx.send(f"{member.mention}, {ctx.message.author.name} just gave you a big big hug!")



@client.command()
@commands.has_permissions(administrator=True)
async def fight(ctx, member: discord.Member = None): # fight a member
    if member == None:
        await ctx.send('Who to you want to attack?')
        return
    if member == ctx.message.author:
        await ctx.send("Sorry, but you can't fight yourself.")
        return
    if member == member.id:
        member = member
    ans = [f"{ctx.message.author.name} is fighting {member.mention}, but hurt themselves in confusion!",
            f"{ctx.message.author.name} is fighting {member.mention}, but they stumbled over their shoelaces!",
            f"{ctx.message.author.name} is fighting {member.mention}, but they tripped over a rock and fell in the ocean!"
            f"{ctx.message.author.name} killed {member.mention}. R.I.P"]
    await ctx.send(random.choice(ans))







@client.command()
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member = None, *, reason = None):
    guild = ctx.message.guild
    if member == None:
        e2 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e2.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e2)
        return
    if member == ctx.message.author:
        e7 = discord.Embed(color=0xfd9fb9, description="Sorry, but you can't ban yourself!")
        e7.set_author(name='Error: Author', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e7)
        return
    if member == member.id:
        member = member
    if reason == None:
        reason = 'No reason provided'
    await guild.ban(user=member, reason=reason, delete_message_days=7)
    await guild.unban(user=member, reason='Softban')
    e4 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully softbanned {member.mention} for **{reason}**!')
    e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
    await ctx.send(embed=e4)
    e = discord.Embed(color=0xfd9fb9, description=f"**User:** {member} (ID: **{member.id}**) \n**Moderator:** {ctx.message.author} (ID: **{ctx.message.author.id}**) \n**Reason:** {reason}")
    e.set_author(name='User softbanned')
    f = open(f"{guild.id}-log.txt", "r")
    channel_id = f.read()
    channel = await client.fetch_channel(channel_id)
    await channel.send(embed=e)

@client.command()
@commands.has_permissions(ban_members=True)
async def muterole(ctx, role: discord.Role = None):
    guild = ctx.message.guild
    if muterole == None:
        e3 = discord.Embed(color=0xfd9fb9, description='Please enter a valid role name/id or mention a valid role!')
        e3.set_author(name='Error: Invalid role', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e3)
        return
    if not os.path.exists(f"./MuteRoles/{guild.id}-mute-role.txt"):
        e33 = discord.Embed(color=0xfd9fb9, description='File not found. This is a super rare error. Please contact `guyod` about this!')
        e33.set_author(name='Error: 404', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e33)
        return
    if os.path.exists(f"./MuteRoles/{guild.id}-mute-role.txt"):
        f = open(f"./MuteRoles/{guild.id}-mute-role.txt", "w")
        f.write(f"{role.id}")
        f.close()
        e99 = discord.Embed(color=0xfd9fb9, description=f'Successfully set the mute role to {role.mention}!')
        e99.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
        await ctx.send(embed=e99)
        return



@client.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member = None, time: int = None, *, reason = None):
    guild = ctx.message.guild
    max_time = 2880
    if member == None:
        e2 = discord.Embed(color=0xfd9fb9, description='Please mention a valid member or enter a valid member id!')
        e2.set_author(name='Error: Invalid member', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e2)
        return
    if time == None:
        e2 = discord.Embed(color=0xfd9fb9, description='Please enter a valid time!')
        e2.set_author(name='Error: Invalid time', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e2)
        return
    if time > max_time:
        e22 = discord.Embed(color=0xfd9fb9, description='Sorry, but the max mute time is 2 days (2880 minutes).')
        e22.set_author(name='Error: Max time', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e22)
        return
    if reason == None:
        reason = 'None'
    if not os.path.exists(f"./MuteRoles/{guild.id}-mute-role.txt"):
        e33 = discord.Embed(color=0xfd9fb9, description='File not found. This is a super rare error. Please contact `@guyod` about this!')
        e33.set_author(name='Error: 404', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e33)
        return
    if os.path.exists(f"./MuteRoles/{guild.id}-mute-role.txt"):
        if os.stat(f"./MuteRoles/{guild.id}-mute-role.txt").st_size == 0:
            e332 = discord.Embed(color=0xfd9fb9, description='Looks like no mute role has been set yet!')
            e332.set_author(name='Error: No mute role', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
            await ctx.send(embed=e332)
            return
        f = open(f"./MuteRoles/{guild.id}-mute-role.txt", "r")
        mute_role_id = f.read()
        mute_role = discord.utils.get(guild.roles, id=int(mute_role_id))
        await member.add_roles(mute_role, reason=reason)
        e4 = discord.Embed(color=0xfd9fb9, description=f'{ctx.message.author.mention} successfully muted {member.mention} for **{time}** minutes because of **{reason}**!')
        e4.set_author(name='Success', icon_url='https://cdn2.iconfinder.com/data/icons/greenline/512/check-512.png')
        await ctx.send(embed=e4)
        if os.path.exists(f"{guild.id}-log.txt"):
            f9 = open(f"{guild.id}-log.txt", "r")
            log_id = f9.read()
            log_channel = await client.fetch_channel(log_id)
            e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**) \nTime: **{time}** Minutes \nReason: **{reason}**")
            e.set_author(name='User Muted')
            await log_channel.send(embed=e)
        else:
            pass
        await asyncio.sleep(time * 60)
        await member.remove_roles(mute_role, reason=reason)
        if os.path.exists(f"{guild.id}-log.txt"):
            f9 = open(f"{guild.id}-log.txt", "r")
            log_id = f9.read()
            log_channel = await client.fetch_channel(log_id)
            e = discord.Embed(color=0xfd9fb9, description=f"User: **{member}** (ID: **{member.id}**) \nModerator: **{ctx.message.author}** (ID: **{ctx.message.author.id}**)")
            e.set_author(name='User Unmuted')
            await log_channel.send(embed=e)
        else:
            pass








@client.event
async def on_command_error(ctx, error): # error messages
    if isinstance(error, commands.BotMissingPermissions):
        e33 = discord.Embed(color=0xfd9fb9, description="I don't have proper permissions do to this action!")
        e33.set_author(name='Error: Missing bot permissions', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e33)
        return
    if isinstance(error, commands.MissingPermissions):
        e332 = discord.Embed(color=0xfd9fb9, description="Looks like you don't have proper permissions do to this action!")
        e332.set_author(name='Error: Missing user permissions', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e332)
        return
    if isinstance(error, commands.NotOwner):
        e333 = discord.Embed(color=0xfd9fb9, description="This commands can only be used by the bot's owner!")
        e333.set_author(name='Error: Owner only', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e333)
        return
    if isinstance(error, commands.BadArgument):
        e335 = discord.Embed(color=0xfd9fb9, description="Value error: One of the arguments has to be an int, not str!")
        e335.set_author(name='Error: Value error', icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=e335)
        return







client.run("MTE3MTgxNTA2NzA0NjY1NDA2Ng.GSxLar.GtPMK9pgXaUFzsSb6xuZWFYEfO6rpOW7rOuh9c")