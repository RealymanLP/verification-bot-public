import disnake as discord
from disnake.ext import commands
import asyncio
import random
import traceback
from sys import getsizeof
import sys
import aiohttp, json, subprocess

global add_lock
global v2
global code
global unverify_lock
global local_verification
global local_verify_message
global db_channel_obj
global ready
global db_channel_obj6
global banned_server
global banned_server_obj
global local_verified_roles
global local_verified_roles_obj
global local_not_verified_roles
global local_not_verified_roles_obj
global banned_users
global s_code
global neustarttimer
global savedata
global verify_role_cache
global everyone_cache
everyone_cache = {}
verify_role_cache = {}
savedata = {}
s_code = ""
banned_users = []
banned_server_obj = []
banned_server = []
ready = False
db_channel_obj = []
db_channel_obj6 = []
local_verification = []
local_verify_message = []
local_verified_roles = []
local_verified_roles_obj = []
local_not_verified_roles = []
local_not_verified_roles_obj = []
add_lock = []
unverify_lock = []
global sp
sp = []
global ssave
ssave = ""
code = {}
v2 = {}

membercache = discord.MemberCacheFlags.none()

intents = discord.Intents.default()
intents.members = True
all_intents = []
if intents.bans:
    all_intents.append("bans = True")
else:
    all_intents.append("bans = False")
if intents.dm_messages:
    all_intents.append("dm_messages = True")
else:
    all_intents.append("dm_messages = False")
if intents.dm_reactions:
    all_intents.append("dm_reactions = True")
else:
    all_intents.append("dm_reactions = False")
if intents.dm_typing:
    all_intents.append("dm_typing = True")
else:
    all_intents.append("dm_typing = False")
if intents.emojis:
    all_intents.append("emojis = True")
else:
    all_intents.append("emojis = False")
if intents.guild_messages:
    all_intents.append("guild_messages = True")
else:
    all_intents.append("guild_messages = False")
if intents.guild_reactions:
    all_intents.append("guild_reactions = True")
else:
    all_intents.append("guild_reactions = False")
if intents.guild_typing:
    all_intents.append("guild_typing = True")
else:
    all_intents.append("guild_typing = False")
if intents.guilds:
    all_intents.append("guilds = True")
else:
    all_intents.append("guilds = False")
if intents.integrations:
    all_intents.append("integrations = True")
else:
    all_intents.append("integrations = False")
if intents.invites:
    all_intents.append("invites = True")
else:
    all_intents.append("invites = False")
if intents.members:
    all_intents.append("members = True")
else:
    all_intents.append("members = False")
if intents.messages:
    all_intents.append("messages = True")
else:
    all_intents.append("messages = False")
if intents.presences:
    all_intents.append("presences = True")
else:
    all_intents.append("presences = False")
if intents.reactions:
    all_intents.append("reactions = True")
else:
    all_intents.append("reactions = False")
if intents.typing:
    all_intents.append("typing = True")
else:
    all_intents.append("typing = False")
if intents.value:
    all_intents.append("value = True")
else:
    all_intents.append("value = False")
if intents.voice_states:
    all_intents.append("voice_states = True")
else:
    all_intents.append("voice_states = False")
if intents.webhooks:
    all_intents.append("webhooks = True")
else:
    all_intents.append("webhooks = False")
print(f"Intents: {all_intents}\n")

client = commands.AutoShardedBot(command_prefix=discord.ext.commands.when_mentioned, intents=intents, chunk_guilds_at_startup=False, member_cache_flags=membercache, max_messages=5, test_guilds=[714819340788301934])

############################################

# Change variables here:

# Set the bot ADMINS; They have acess to special commands and are excluded from MAINTENANCE mode. They can also answer in DM-Support
ADMINS = [513071093976793099]

# When a support message contains one of these words, it will be marked as spam
CHAT_FILTER = ["idiot", "ideot", "lächerlich", "behindert", "toxic", "noob", "arsch", "ehrenlos", "skilllos", "scheiß", "fresse", "kak", "kack", "rumheulen",  "rip", "wichser", "wichsen", "arschloch", "sex", "bastard", "arschgesicht", "scheißkopf", "verpiss",  "anal", "anus", "arse", "assfuck", "asshole", "assfucker", "asshole", "assshole", "bastard", "bitch", "bloodyhell", "cockfucker", "cocksuck", "cocksucker", "coonnass", "douche", "erect", "erection", "erotic", "escort", "fuckoff", "fuckyou", "fuckass", "fuckhole", "goddamn", "homoerotic", "lesbian", "lesbians", "motherfucker", "motherfuck", "nigger", "penis", "penisfucker", "pissoff", "porn", "porno", "pornography", "pussy", "retard", "sadist", "sexy", "sonofabitch", "tits", "naked", "nackte", "nackt", "nackten", "schei0", "ar***", "scheiss", "kacke", "fick", "oasch", "drecksau", "saubeutel", "drecksack", "wixxe", "wichse", "sackgesicht", "spasst", "spast", "deimudda", "deinemudda", "deinemutter", "deimutter", "spasti", "spacko", "spakko", "hackfresse", "pansen", "natursekt", "naturkaviar", "klitoris", "vagina",  "titte", "pimmel", "puller", "schlampe", "fotze", "hure", "nutte", "beidl", "moese", "schwuchtel", "lesbe", "schwul", "schwuchtl", "schwuchtel", "lesbisch", "muschi", "stricher", "sperm", "homos", "hoden", "sex", "pedophil", "pedofil", "jihad", "dschihad", "gulag", "tschusch", "neger", "nigger", "bimbo", "kanake", "kanacke", "kannacke", "muselmann", "itacker", "itaka", "polack", "kkk", "kukluxklan", "itaker", "kuemmeltuerk", "chinafarmer", "reisfresser", "kokain", "koks", "xtasy", "ecstasy", "marihuana", "mariwana", "mariwanna", "hasch", "cannabis", "moepse", "moese", "moeppse", "kloeten", "kinderschaender", "scheiss", "arsch", "bumsen", "abortion", "analingus", "anus", "anuses", "arse", "arsehole", "arseraper", "arserapist", "aryan", "asscrack", "ass", "asses", "asspirate", "asswipe", "ballbuster", "ballbreaker", "ballsack", "bastard", "beaver", "bestiality", "beastiality", "beeyotch", "biatch", "bitch", "blowjob", "blueball", "bollock", "bollox", "boner", "boners", "booty", "bunghole", "butthole", "canabis", "cannabis", "chlamydia", "choad", "chode", "circle", "jerk", "cocaine", "colostomy", "constipat", "cottonpicker", "crackhead", "creaming", "cum", "cumbucket", "cumguzzler", "cumshot", "cunniling", "cunt", "darkie", "darky", "daterape", "deepthroat", "defecat", "deficat", "dildo", "dingleberr", "doggiestyle", "doggystyle", "donkeypunch", "dookie", "doosh", "douch", "doush", "ejaculat", "enema", "erectile", "erection", "fag", "fart", "farts", "fcuk", "fecal", "feces", "felch", "fellat", "fetus", "foetus", "fisting", "fook", "foreskin", "frontbum", "fudgepacker", "funbags", "furburger", "furryburger", "gangbang", "gangrape", "ganja", "genital", "gloryhole", "goatse", "goldenshower", "gonorhea", "gonorrhoea", "gonad", "handjob", "heroin", "hemorrhoid", "haemorrhoid", "herpes", "hoebag", "honkie", "honky", "hooker", "hooter", "hotcarl", "hymen", "jackoff", "jerkoff", "jigabo", "jihad", "jism", "jizz", "juggs", "klit", "lemonparty", "mangina", "manjuice", "marijuana", "masturbat", "maxipad", "milf", "molester", "molestor", "muffbomb", "muffdiv", "nads", "necroped", "necrophil", "negro", "negroes", "niglet", "nippl", "nobgoblin", "numbnut", "nutsack", "nutted", "orgasm", "paedophile", "pedofile", "pedophile", "penis", "pillowbiter", "piss", "pootang", "poontang", "porn", "pussy", "queef", "queer", "raghead", "rapist", "rapists", "reacharound", "rectal", "rectum", "reefer", "retard", "rimjob", "rugmunch", "rumprider", "schlong", "secks", "sex", "shemale", "shlong", "skinflute", "slanteyes", "slut", "sperm", "sphincter", "spliff", "joint", "strapon", "swampass", "sybian", "syphil", "taliban", "tampax", "tampon", "tarbaby", "teabag", "testic", "tightass", "tits", "tittie", "titty", "tosser", "towelhead", "tranny", "tubgirl", "twat", "urinat", "vagina", "vajina", "vajayjay", "vibrater", "vibrator", "whitie", "whore", "wrecktum", "zipperhead"]

# When !clean gets executed, the bot will stay on these servers, even when the bot is not in use there
ALLOWED_SERVERS = [ENTER SERVER-IDS HERE]

# Set to true to enable MAINTENANCE mode. Will set the bot's status to "MAINTENANCE" and users are no longer able to run commands
MAINTENANCE = True

# Set the DB Channel for banned users
BANNED_USERS_ID = ENTER CHANNEL-ID HERE

# Set the DB Channel for Verification-Channel and Server
VERIFY_CHANNEL_ID = ENTER CHANNEL-ID HERE

# Set the DB Channel for verify-message
MESSAGE_CHANNEL_ID = ENTER CHANNEL-ID HERE

# Set the DB Channel for banned servers
BANNS_CHANNEL_ID = ENTER CHANNEL-ID HERE

# Set the DB Channel for Verified roles
VERIFIED_ROLES_CHANNEL_ID = ENTER CHANNEL-ID HERE

# Log server joins/leaves
SERVER_JOIN_LEAVE_CHANNEL_ID = ENTER CHANNEL-ID HERE

# Log errors
ERROR_CHANNEL = ENTER CHANNEL-ID HERE

############################################

def sizeof_fmt(num, suffix='B'):
    ''' by Fred Cirera,  https://stackoverflow.com/a/1094933/1870254, modified'''
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

async def clear():
    while True:
        global v2
        global sp
        global ssave
        global code
        code = {}
        ssave = ""
        v2 = {}
        await asyncio.sleep(5000)

async def clearcache():
    while True:
        add_lock = []
        await asyncio.sleep(300)

async def autoneustart():
    await asyncio.sleep(43200)
    print("Auto Neustart")
    await client.close()
    sys.exit()

@client.slash_command(name="help", description="Shows all commands", dm_permission=False)
async def help(interaction):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    embed = discord.Embed(title='Verification-Help', description='https://realygirllp.jimdofree.com/discord/verification-bot/', color=3566847)
    embed.add_field(name="---", value="Admin-Commands", inline=False)
    embed.add_field(name=f"/add-verification", value="Add the verification to the channel, where you run the command (makes it a verify-channel)", inline=False)
    embed.add_field(name=f"/remove-channel", value="Remove the verification (verify-channel) from the channel, where you run the command. ", inline=False)
    embed.add_field(name=f"/check-verify-channel", value="Checks if the channel, where you run the command is a verify-channel", inline=False)
    embed.add_field(name=f"/check-verification", value="Checks whether errors occurred during the setup of the verification (or later) that could cause problems. You should run this command after !add-verification is finished. Note: Not every error is a problem!", inline=False)
    embed.add_field(name=f"/verify-message", value="Customize the message, when a new user types !verify. You can include the code with {code}. Example: \"!verify-message Welcome to the Server! Please verify yourself with the code {code}\" ", inline=False)
    embed.add_field(name=f"/mverify USER", value="Manually verify a user", inline=False)
    embed.add_field(name=f"/unverify USER", value="Manually unverify a user", inline=False)
    embed.add_field(name=f"---", value="User-Commands", inline=False)
    embed.add_field(name=f"/verify", value="Generates a verification code. Only runs in verify-channel. Message with code will be deleted in 5 minutes.", inline=False)
    embed.add_field(name=f"/verify [NUMBER]", value="Redeem a generated verification-code", inline=False)
    embed.add_field(name=f"/help", value="Shows this message", inline=False)
    try:
        await interaction.response.send_message(embed=embed, ephemeral=True)
    except:
        await interaction.response.send_message("This message is too long to send it as text. Please enable embeds on the server!", ehemeral=True)

class PermissionSelectEveryone(discord.ui.View):
    options = [
        discord.SelectOption(label="Don't change", description="Don't change permissions"),
        discord.SelectOption(label="None", description="No permissions"),
        discord.SelectOption(label='create_instant_invite', description='Add CREATE_INSTANT_INVITE permission'),
        discord.SelectOption(label='add_reactions', description='Add ADD_REACTIONS permission'),
        discord.SelectOption(label='view_channel', description='Add VIEW_CHANNEL permission'),
        discord.SelectOption(label='send_messages', description='Add SEND_MESSAGES permission'),
        discord.SelectOption(label='send_tts_messages', description='Add SEND_TTS_MESSAGES permission'),
        discord.SelectOption(label='embed_links', description='Add EMBED_LINKS permission'),
        discord.SelectOption(label='attach_files', description='Add ATTACH_FILES permission'),
        discord.SelectOption(label='read_message_history', description='Add READ_MESSAGE_HISTORY permission'),
        discord.SelectOption(label='mention_everyone', description='Add MENTION_EVERYONE permission'),
        discord.SelectOption(label='use_external_emojis', description='Add USE_EXTERNAL_EMOJIS permission'),
        discord.SelectOption(label='connect', description='Add CONNECT permission'),
        discord.SelectOption(label='speak', description='Add SPEAK permission'),
        discord.SelectOption(label='change_nickname', description='Add CHANGE_NICKNAME permission'),
        discord.SelectOption(label='create_public_threads', description='Add CREATE_PUBLIC_THREADS permission'),
        discord.SelectOption(label='create_private_threads', description='Add CREATE_PRIVATE_THREADS permission'),
        discord.SelectOption(label='use_external_stickers', description='Add USE_EXTERNAL_STICKERS permission'),
        discord.SelectOption(label='send_messages_in_threads', description='Add SEND_MESSAGES_IN_THREADS permission')
        
    ]
    
    @discord.ui.select(placeholder='Select permissions', min_values=1, max_values=len(options), options=options)
    async def sel(self, select: discord.ui.Select, interaction: discord.Interaction):
        global verify_role_cache
        global everyone_cache
        selected = interaction.data.values
        verified_role = verify_role_cache[str(interaction.guild.id)]
        everyone_role = everyone_cache[str(interaction.guild.id)]
        try:
            await interaction.message.delete()
            if "Don't change" in selected:
                pass
            else:
                permissions = 0
                if "create_instant_invite" in selected:
                    permissions += 1
                if "add_reactions" in selected:
                    permissions += 64
                if "view_channel" in selected:
                    permissions += 1024
                if "send_messages" in selected:
                    permissions += 2048
                if "send_tts_messages" in selected:
                    permissions += 4096
                if "embed_links" in selected:
                    permissions += 16384
                if "attach_files" in selected:
                    permissions += 32768
                if "read_message_history" in selected:
                    permissions += 65536
                if "mention_everyone" in selected:
                    permissions += 131072
                if "use_external_emojis" in selected:
                    permissions += 262144
                if "connect" in selected:
                    permissions += 1048576
                if "speak" in selected:
                    permissions += 2097152
                if "change_nickname" in selected:
                    permissions += 67108864
                if "create_public_threads" in selected:
                    permissions += 34359738368
                if "create_private_threads" in selected:
                    permissions += 68719476736
                if "use_external_stickers" in selected:
                    permissions += 137438953472
                if "send_messages_in_threads" in selected:
                    permissions += 274877906944

                permission_overwrite = discord.Permissions(permissions=permissions+2147483648)
                await everyone_role.edit(permissions=permission_overwrite)

            await interaction.channel.set_permissions(everyone_role, overwrite=discord.PermissionOverwrite(read_messages=True, read_message_history=True, send_messages=True, use_slash_commands=True))
            await interaction.channel.set_permissions(verified_role, overwrite=discord.PermissionOverwrite(read_messages=False, read_message_history=False, send_messages=False, use_slash_commands=True))

            embed = discord.Embed(title=f"Setup done sucessfully!", description="This message will be automatically deleted in 5 seconds.", color=3566847)
            await interaction.response.send_message(embed=embed, delete_after=5)

        except:
            embed = discord.Embed(title="I'm sorry, but I don't have permissions to change server/channel permissions.", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("I'm sorry, but I don't have permissions to change server/channel permissions.", ephemeral=True)


class PermissionSelectVerified(discord.ui.View):
    options = [
        discord.SelectOption(label="Don't change", description="Don't change permissions"),
        discord.SelectOption(label="None", description="No permissions"),
        discord.SelectOption(label='create_instant_invite', description='Add CREATE_INSTANT_INVITE permission'),
        discord.SelectOption(label='add_reactions', description='Add ADD_REACTIONS permission'),
        discord.SelectOption(label='view_channel', description='Add VIEW_CHANNEL permission'),
        discord.SelectOption(label='send_messages', description='Add SEND_MESSAGES permission'),
        discord.SelectOption(label='send_tts_messages', description='Add SEND_TTS_MESSAGES permission'),
        discord.SelectOption(label='embed_links', description='Add EMBED_LINKS permission'),
        discord.SelectOption(label='attach_files', description='Add ATTACH_FILES permission'),
        discord.SelectOption(label='read_message_history', description='Add READ_MESSAGE_HISTORY permission'),
        discord.SelectOption(label='mention_everyone', description='Add MENTION_EVERYONE permission'),
        discord.SelectOption(label='use_external_emojis', description='Add USE_EXTERNAL_EMOJIS permission'),
        discord.SelectOption(label='connect', description='Add CONNECT permission'),
        discord.SelectOption(label='speak', description='Add SPEAK permission'),
        discord.SelectOption(label='change_nickname', description='Add CHANGE_NICKNAME permission'),
        discord.SelectOption(label='create_public_threads', description='Add CREATE_PUBLIC_THREADS permission'),
        discord.SelectOption(label='create_private_threads', description='Add CREATE_PRIVATE_THREADS permission'),
        discord.SelectOption(label='use_external_stickers', description='Add USE_EXTERNAL_STICKERS permission'),
        discord.SelectOption(label='send_messages_in_threads', description='Add SEND_MESSAGES_IN_THREADS permission')
        
    ]
    
    @discord.ui.select(placeholder='Select permissions', min_values=1, max_values=len(options), options=options)
    async def sel(self, select: discord.ui.Select, interaction: discord.Interaction):
        global verify_role_cache
        global everyone_cache
        selected = interaction.data.values
        verified_role = verify_role_cache[str(interaction.guild.id)]
        everyone_role = everyone_cache[str(interaction.guild.id)]
        try:
            await interaction.message.delete()
            if "Don't change" in selected:
                pass
            else:
                permissions = 0
                if "create_instant_invite" in selected:
                    permissions += 1
                if "add_reactions" in selected:
                    permissions += 64
                if "view_channel" in selected:
                    permissions += 1024
                if "send_messages" in selected:
                    permissions += 2048
                if "send_tts_messages" in selected:
                    permissions += 4096
                if "embed_links" in selected:
                    permissions += 16384
                if "attach_files" in selected:
                    permissions += 32768
                if "read_message_history" in selected:
                    permissions += 65536
                if "mention_everyone" in selected:
                    permissions += 131072
                if "use_external_emojis" in selected:
                    permissions += 262144
                if "connect" in selected:
                    permissions += 1048576
                if "speak" in selected:
                    permissions += 2097152
                if "change_nickname" in selected:
                    permissions += 67108864
                if "create_public_threads" in selected:
                    permissions += 34359738368
                if "create_private_threads" in selected:
                    permissions += 68719476736
                if "use_external_stickers" in selected:
                    permissions += 137438953472
                if "send_messages_in_threads" in selected:
                    permissions += 274877906944

                permission_overwrite = discord.Permissions(permissions=permissions+2147483648)
                await verified_role.edit(permissions=permission_overwrite)

            embed = discord.Embed(title=f"Select default permissions for \"{everyone_role.name}\"", description=f"You can select your default permissions for \"{everyone_role.name}\".", color=3566847)
            await interaction.response.send_message(embed=embed, view=PermissionSelectEveryone())
        except:
            embed = discord.Embed(title="I'm sorry, but I don't have permissions to change server/channel permissions.", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("I'm sorry, but I don't have permissions to change server/channel permissions.", ephemeral=True)


@client.slash_command(name="setup", description="Setup for Verification-System", options=[discord.Option("verified_role", "Select your Verified-Role. Users will get it after they have verified.", discord.OptionType.role)], default_member_permissions=discord.Permissions(8), dm_permission=False)
async def setup(interaction, verified_role=None):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    global verify_role_cache
    global everyone_cache
    if not ready:
        embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
        return
    if MAINTENANCE and not interaction.author.id in ADMINS:
        embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_", ephemeral=True)
        return
    savedata[interaction.guild.id] = verified_role
    perm = []
    botperm = []
    for i in interaction.author.guild_permissions:
        perm.append(str(i))
    for i in interaction.channel.guild.me.guild_permissions:
        botperm.append(str(i))
    user = interaction.author
    if str("('administrator', True)") in perm or interaction.author.id in sp:
        if verified_role is None:
            try:
                verified_role = await interaction.guild.create_role(name="Verified")
            except:
                embed = discord.Embed(title='Failed to create "Verified"-Role! Please ensure, that I have the manage_roles permission and try again!', color=16711680)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message('Failed to create "Verified"-Role! Please ensure, that I have the manage_roles permission and try again!', ephemeral=True)
                return

        if True:
            noverify = False
            try:
                exclude = []
                excluded_channels = excluded_channels.replace(" ")
                excludex = excluded_channels.split(",")
                if not exclude is None:
                    for channel_id in excludex:
                        try:
                            c = client.get_channel(int(channel_id))
                            exclude.append(c)
                        except:
                            pass
            except:
                exclude = []
            
            if interaction.guild.id in add_lock:
                embed = discord.Embed(title='Please wait 5 minutes, until you run the command again.\n(Discord API restriction)', color=16711680)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message("Please wait 5 minutes, until you run the command again.\n(Discord API restriction)", ephemeral=True)
                return
            verify_role_cache[str(interaction.guild.id)] = verified_role
            everyone_cache[str(interaction.guild.id)] = interaction.guild.default_role
            if not str(interaction.guild.id) in local_verification:
                msg = await client.get_channel(VERIFY_CHANNEL_ID).send(interaction.guild.id)
                local_verification.append(str(interaction.guild.id))
                db_channel_obj.append(msg)
            if not str(interaction.channel.id) in local_verification:
                msg = await client.get_channel(VERIFY_CHANNEL_ID).send(interaction.channel.id)
                local_verification.append(str(interaction.channel.id))
                db_channel_obj.append(msg)
            if not str(verified_role.id) in local_verified_roles:
                msg = await client.get_channel(VERIFIED_ROLES_CHANNEL_ID).send(verified_role.id)
                local_verified_roles.append(str(verified_role.id))
                local_verified_roles_obj.append(msg)
            embed = discord.Embed(title=f"Select default permissions for \"{verified_role.name}\"", description=f"You can select your default permissions for \"{verified_role.name}\".", color=3566847)
            await interaction.response.send_message(embed=embed, view=PermissionSelectVerified())

            """
            guild = interaction.guild
            embed = discord.Embed(title='Setup is now running. This can take a few minutes...\n(Discord API restriction)', description='This message will be automatically deleted when finished.', color=3566847)
            
            try:
                await interaction.response.send_message(embed=embed)
            except:
                await interaction.response.send_message("Setup is now running. This can take a few minutes...\n(Discord API restriction)\nThis message will be automatically deleted when finished.")
            wait_msg = await interaction.original_message()
            await interaction.channel.trigger_typing()
            roles = []
            for i in guild.roles:
                roles.append(i.name)
            
            if not str(guild.id) in local_verification:
                msg = await client.get_channel(713392523502157946).send(guild.id)
                local_verification.append(str(guild.id))
                db_channel_obj.append(msg)
            if not str(interaction.channel.id) in local_verification:
                msg = await client.get_channel(713392523502157946).send(interaction.channel.id)
                local_verification.append(str(interaction.channel.id))
                db_channel_obj.append(msg)
            role2 = verified_role
            print(role2)
            role3 = discord.utils.get(interaction.guild.roles, name='@everyone')
            role4 = discord.utils.get(interaction.guild.roles, name='Verification')
            add_lock.append(guild.id)
            clocked = False
            try:
                failed_channels = []
                for i in guild.channels:
                    changed_roles = []
                    for role in i.changed_roles:
                        changed_roles.append(role.name)
                    if not i in exclude:
                        if not "Verified" in changed_roles:
                                try:
                                    await asyncio.sleep(3)
                                    await interaction.channel.trigger_typing()
                                    await i.set_permissions(role2, overwrite=discord.PermissionOverwrite(read_messages = True, send_messages=True))
                                    await i.set_permissions(role4, overwrite=discord.PermissionOverwrite(read_messages = True, send_messages=True))
                                except Exception as e:
                                    pass
                await asyncio.sleep(2)
                await interaction.channel.set_permissions(role2, overwrite=discord.PermissionOverwrite(read_messages = False, send_messages=False))
                await interaction.channel.set_permissions(role4, overwrite=discord.PermissionOverwrite(read_messages = True, send_messages=True))
            except:
                pass
            embed = discord.Embed(title='Verify-Channel set to the current channel!', color=3566847)
            
            try:
                await wait_msg.edit(embed=embed)
            except:
                await wait_msg.edit("Verify-Channel set to the current channel!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await wait_msg.delete()
            except:
                pass
            
            await asyncio.sleep(300)
            add_lock.remove(guild.id)

            """
        
        

    else:
        embed = discord.Embed(title="You don't have permission for this command!", color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.", ephemeral=True)


@client.slash_command(name="remove-channel", description="Removes verification-system from current channel", default_member_permissions=discord.Permissions(8), dm_permission=False)
async def removechannel(interaction):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if not ready:
        embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
        return
    if MAINTENANCE and not interaction.author.id in ADMINS:
        embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_", ephemeral=True)
        return
    if True:
        perm = []
        for i in interaction.author.guild_permissions:
            perm.append(str(i))
        if str("('administrator', True)") in perm or interaction.author.id in sp:
            if str(interaction.channel.id) in local_verification:
                try:
                    for i in interaction.guild.channels:
                        if str(i.id) in local_verification:
                            vchannel = str(i.id)
                except:
                    pass
                nachricht = discord.utils.get(db_channel_obj, content=vchannel)
                try:
                    await nachricht.delete()
                    local_verification.remove(vchannel)
                    embed = discord.Embed(title='This verify-channel got deleted!', color=3566847)
                    try:
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                    except:
                        await interaction.response.send_message("This verify-channel got deleted!", ephemeral=True)
                except:
                    embed = discord.Embed(title="This channel isn't a verify-channel!", color=16711680)
                    try:
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                    except:
                        await interaction.response.send_message("This channel isn't a verify-channel!", ephemeral=True)
            else:
                embed = discord.Embed(title="This channel isn't a verify-channel!", color=16711680)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message("This channel isn't a verify-channel!", ephemeral=True)
        else:
            embed = discord.Embed(title="You don't have permission for this command!", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("You don't have permission for this command!", ephemeral=True)

@client.slash_command(name="unverify", description="Unverify a user", options=[discord.Option("user", "User to unverify", discord.OptionType.user, required=True)], default_member_permissions=discord.Permissions(8), dm_permission=False)
async def unverify(interaction, user):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if not ready:
        embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
        return
    if MAINTENANCE and not interaction.author.id in ADMINS:
        embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_", ephemeral=True)
        return
    if True:
        perm = []
        for i in interaction.author.guild_permissions:
            perm.append(str(i))
        if str("('administrator', True)") in perm or interaction.author.id in sp:
            for role in interaction.guild.roles:
                if str(role.id) in local_verified_roles:
                    role1 = discord.utils.get(interaction.guild.roles, id=role.id)
                    break
                else:
                    role1 = discord.utils.get(interaction.guild.roles, name='Verified')
            try:
                await user.remove_roles(role1)
                embed = discord.Embed(title=f'{user} unverified successfully!', description='', color=3566847)
                    
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message(f"{user} unverified successfully!", ephemeral=True)
            except:
                embed = discord.Embed(title='This user can\'t get unverified!', description='', color=16711680)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message("This user can\'t get unverified!", ephemeral=True)
        else:
            embed = discord.Embed(title="You don't have permission for this command!", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("You don't have permission for this command!", ephemeral=True)

@client.slash_command(name="check-verify-channel", description="Checks if the current channel is defined as verify-channel", default_member_permissions=discord.Permissions(8), dm_permission=False)
async def checkverifychannel(interaction):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if not ready:
        embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
        return
    if MAINTENANCE and not interaction.author.id in ADMINS:
        embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_", ephemeral=True)
        return
    if True:
        perm = []
        for i in interaction.author.guild_permissions:
            perm.append(str(i))
        if str("('administrator', True)") in perm or interaction.author.id in sp:
            if str(interaction.channel.id) in local_verification:
                embed = discord.Embed(title='This is a verify-channel!', color=3566847)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message("This is a verify-channel!", ephemeral=True)
            else:
                embed = discord.Embed(title="This channel isn't a verify-channel!", color=16711680)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message("This channel isn't a verify-channel!", ephemeral=True)
        else:
            embed = discord.Embed(title="You don't have permission for this command!", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("You don't have permission for this command!", ephemeral=True)

@client.slash_command(name="check-verification", description="Checks setup status of verification-system on your server", default_member_permissions=discord.Permissions(8), dm_permission=False)
async def checkverification(interaction):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if not ready:
        embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
        return
    if MAINTENANCE and not interaction.author.id in ADMINS:
        embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_", ephemeral=True)
        return
    if True:
        perm = []
        botperm = []
        for i in interaction.author.guild_permissions:
            perm.append(str(i))
        for i in interaction.channel.guild.me.guild_permissions:
            botperm.append(str(i))
        if str("('administrator', True)") in perm or interaction.author.id in sp:
            await interaction.response.defer(ephemeral=True)
            original_message = await interaction.original_message()
            try:
                for i in interaction.guild.channels:
                    if str(i.id) in local_verification:
                        vchannel = int(i.id)
                        vchannel = client.get_channel(int(vchannel))
            except:
                pass
            channelperm = []
            try:
                for i in vchannel.permissions_for(interaction.channel.guild.me):
                    channelperm.append(str(i))
            except:
                pass
            if str("('manage_messages', True)") in botperm or str("('manage_messages', True)") in channelperm:
                manage_confirm = True
                manage_confirmx = True
            else:
                manage_confirm = False
                manage_confirmx = ('**' + str(False)) + '**'
            if str(interaction.guild.id) in local_verification:
                guild_confirm = True
                guild_confirmx = True
            else:
                guild_confirm = False
                guild_confirmx = ('**' + str(False)) + '**'
            roles = []
            for i in interaction.guild.roles:
                roles.append(i.name)
            for i in interaction.guild.roles:
                if str(i.id) in local_verified_roles:
                    verified_confirm = True
                    verified_confirmx = f"{i} ({i.id})"
                    try:
                        role2 = discord.utils.get(interaction.guild.roles, id=i.id)
                    except:
                        pass
                    break
                elif 'Verified' in roles:
                    role2 = discord.utils.get(interaction.guild.roles, name='Verified')
                    verified_confirm = True
                    verified_confirmx = f"{role2.name} ({role2.mention})\n{role2.id}"
                    break
                else:
                    verified_confirm = False
                    verified_confirmx = '**' + str(None) + '**'
                    role2 = None
            channels = []
            channel_confirm = ''
            for i in interaction.guild.channels:
                if str(i.id) in local_verification:
                    channel_confirm = str(i.id)
                    channel_confirmx = f"{i.name} ({i.mention})\n{i.id}"
            if channel_confirm == '':
                channel_confirm = None
                channel_confirmx = ('**' + str(None)) + '**'
            try:
                await interaction.channel.guild.me.add_roles(role2)
                await asyncio.sleep(2)
                await interaction.channel.guild.me.remove_roles(role2)
                verified_high = True
                verified_highx = True
            except:
                verified_high = False
                verified_highx = ('**' + str(False)) + '**'

            code22x = []
            for messagex in db_channel_obj6:
                code22x.append(messagex.content)
            try:
                ver_message = code22x.index(str(interaction.guild.id))
                ver_message = code22x[ver_message-1]
            except:
                ver_message = "Default"
                
            if guild_confirm == True and verified_confirm == True and not channel_confirm == None and verified_high == True and manage_confirm == True:
                check_status = '**Everything is fine!**'
                check_color = 3566847
            else:
                check_status = '**There are some errors! They are marked bold.**'
                check_color = 16711680
            embed = discord.Embed(title='Verification-Check', description=check_status, color=check_color)
            embed.add_field(name='Server registered?', value=guild_confirmx, inline=False)
            embed.add_field(name='Verify-Channel?', value=channel_confirmx, inline=False)
            embed.add_field(name='Verified-role?', value=verified_confirmx, inline=False)
            embed.add_field(name='Verified-role assignable?', value=verified_highx, inline=False)
            embed.add_field(name='Delete messages in verify-channel?', value=manage_confirmx, inline=False)
            embed.add_field(name='Verify-message?', value=ver_message, inline=False)
            if guild_confirm == True and verified_confirm == True and not channel_confirm == None and verified_high == True and manage_confirm == True:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/4sGPHCN/ixVTxxT.png')
                except:
                    pass
            else:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/8dQWnzY/cq2w57Y.png')
                except:
                    pass
            
            try:
                await original_message.edit(embed=embed)
            except:
                await original_message.edit(f"Verification-Check - {check_status}\nServer registered? - {guild_confirmx}\nVerify-Channel? - {channel_confirmx}\nVerified-role exist? - {verified_confirmx}\nVerified-role assignable? - {verified_highx}\nNot verified-role exist? - {not_verified_confirmx}\nNot verified-role assignable? - {not_verified_highx}\nDelete messages in verify-channel? - {manage_confirmx}")
        else:
            embed = discord.Embed(title="You don't have permission for this command!", color=16711680)
            
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("You don't have permission for this command!", ephemeral=True)

@client.slash_command(name="verify-message", description="Set the verify-message, a new user see after running /verify", options=[discord.Option("message", "The verify-message", discord.OptionType.string)], default_member_permissions=discord.Permissions(8), dm_permission=False)
async def verifymessage(interaction, message=None):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if not ready:
        embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
        return
    if MAINTENANCE and not interaction.author.id in ADMINS:
        embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_", ephemeral=True)
        return
    if True:
        perm = []
        for i in interaction.author.guild_permissions:
            perm.append(str(i))
        if str("('administrator', True)") in perm or interaction.author.id in sp:
            if message is None:
                if str(interaction.guild.id) in local_verify_message:
                    nachricht = discord.utils.get(db_channel_obj6, content=str(interaction.guild.id))
                    try:
                        await nachricht.delete()
                        try:
                            local_verify_message.remove(nachricht.content)
                        except:
                            pass
                        try:
                            db_channel_obj6.remove(nachricht)
                        except:
                            pass
                        embed = discord.Embed(title='Your custom verify-message got deleted!', color=3566847)
                        try:
                            await interaction.response.send_message(embed=embed, ephemeral=True)
                        except:
                            await interaction.response.send_message('Your custom verify-message got deleted!', ephemeral=True)
                        return
                    except:
                        embed = discord.Embed(title='Your custom verify-message got deleted!', color=3566847)
                        try:
                            await interaction.response.send_message(embed=embed, ephemeral=True)
                        except:
                            await interaction.response.send_message('Your custom verify-message got deleted!', ephemeral=True)
                        return
                else:
                    embed = discord.Embed(title='Your custom verify-message got deleted!', color=3566847)
                    try:
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                    except:
                        await interaction.response.send_message('Your custom verify-message got deleted!', ephemeral=True)
                    return
                    
                    
            elif not "{code}" in message:
                embed = discord.Embed(title='You have to include the code variable \{code\} (with the brackets) into your message!', color=16711680)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message("You have to include the code variable \{code\} (with the brackets) into your message!", ephemeral=True)
                return
            channel = client.get_channel(MESSAGE_CHANNEL_ID)
            try:
                if str(interaction.guild.id) in local_verify_message:
                    guild = interaction.guild
                nachricht1 = discord.utils.get(db_channel_obj6, content=str(interaction.guild.id))
                await nachricht1.delete()
            except:
                pass
            n1 = await channel.send(str(interaction.guild.id))
            n2 = await channel.send(message)
            local_verify_message.insert(0, str(interaction.guild.id))
            local_verify_message.insert(0, message)
            db_channel_obj6.insert(0, n1)
            db_channel_obj6.insert(0, n2)
            embed = discord.Embed(title=f'Verify-Message set to:\n{message}', color=3566847)
            try:
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message(f'Verify-Message set to:\n{message}', ephemeral=True)
            except:
                x = await interaction.original_message()
                try:
                    await x.edit(embed=embed)
                except:
                    await x.edit(f'Verify-Message set to:\n{nachricht}')

                
        else:
            embed = discord.Embed(title="You don't have permission for this command!", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("You don't have permission for this command!", ephemeral=True)

@client.slash_command(name="vote", description="Vote for our bot!", dm_permission=False)
async def vote(interaction):
    embed = discord.Embed(title="Vote!", description='Vote for our bot and support us!\nhttps://top.gg/bot/713387523757310042/vote\nhttps://botsfordiscord.com/bot/713387523757310042/vote', color=3566847)
    try:
        await interaction.response.send_message(embed=embed, ephemeral=True)
    except:
         await interaction.response.send_message("Vote!\nVote for our bot and support us!\nhttps://top.gg/bot/713387523757310042", ephemeral=True)

@client.slash_command(name="verify", description="Verify yourself on the server", options=[discord.Option("vcode", "Your verify-code (run first without this parameter)", discord.OptionType.integer)], dm_permission=False)
async def verify(interaction, vcode=None):
    global v2
    global code
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if not ready:
        embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
        return
    if MAINTENANCE and not interaction.author.id in ADMINS:
        embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_", ephemeral=True)
        return
    if vcode is None:
        if str(interaction.channel.id) in local_verification:
            code22x = []
            for messagex in db_channel_obj6:
                code22x.append(messagex.content)
            code[interaction.guild.id] = str(random.randint(10000, 99999))
            try:
                code23 = code22x.index(str(interaction.guild.id))
                code2 = code22x[code23-1].format(code=str("/verify vcode:" + code[interaction.guild.id]))
            except:
                code2 = (f'To confirm that you are not a bot, please enter:\n/verify vcode:') + str(code[interaction.guild.id])
            embed = discord.Embed(title=code2, description='', color=3566847)
            embed.set_footer(text=f"Code doesn't work? Use /verify again!")
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message(f"{code2}\n_Code doesn't work? Use /verify again!_", ephemeral=True)

        else:
            embed = discord.Embed(title="You can't run this command here!", description="If you think that this is a mistake, please contact the server administrator for help.", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("You can't run this command here!\nIf you think that this is a mistake, please contact the server administrator for help.", ephemeral=True)

    else:
        if str(interaction.channel.id) in local_verification:
            if str(vcode) == str(code[interaction.guild.id]):
                try:
                    role2 = role2
                except:
                    role2 = discord.utils.get(interaction.guild.roles, name='Verified')
                try:
                    await interaction.author.add_roles(role2)
                except:
                    embed = discord.Embed(title='Error in Verify-Process! Please contact the server administrator for help.', color=16711680)
                    try:
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                    except:
                        await interaction.response.send_message("Error in Verify-Process! Please contact the server administrator for help.", ephemeral=True)
                    embed = discord.Embed(title='Error!', description='An error occoured while trying to give the "Verified"-Role. Please ensure, that my role is higher than the "Not verified" and "Verified"-Role!', color=16711680)
                    try:
                        await guild.owner.send(embed=embed)
                    except:
                        pass
                    try:
                        del code[message.guild.id]
                    except:
                        pass
                    return
                try:
                    del code[message.guild.id]
                except:
                    pass
                embed = discord.Embed(title='Verify successfull!', color=3566847)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message("Verify successfull!", ephemeral=True)
                for i in interaction.guild.roles:
                    for j in local_verified_roles:
                        if str(i.id) == j:
                            role2 = i
                            break
                return
            else:
                embed = discord.Embed(title='This Verify-code is wrong! Please try again!', color=16711680)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message("This Verify-code is wrong! Please try again!", ephemeral=True)

@client.slash_command(name="mverify", description="Manually verify users", options=[discord.Option("user", "User to verify", discord.OptionType.user, required=True)], default_member_permissions=discord.Permissions(8), dm_permission=False)
async def mverify(interaction, user):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if not ready:
        embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
        return
    if MAINTENANCE and not interaction.author.id in ADMINS:
        embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', color=16711680)
        try:
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            await interaction.response.send_message("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_", ephemeral=True)
        return
    if True:
        perm = []
        for i in interaction.author.guild_permissions:
            perm.append(str(i))
        if str("('administrator', True)") in perm or interaction.author.id in sp:
            for role in interaction.guild.roles:
                if str(role.id) in local_verified_roles:
                    role1 = discord.utils.get(interaction.guild.roles, id=role.id)
                    break
                else:
                    role1 = discord.utils.get(interaction.guild.roles, name='Verified')
            try:
                await user.add_roles(role1)
                embed = discord.Embed(title=f'{user} verified successfully!', color=3566847)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message(f'{user} verified successfully!', ephemeral=True)
            except:
                embed = discord.Embed(title='This user can\'t get verified!', color=16711680)
                try:
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                except:
                    await interaction.response.send_message("This user can\'t get verified!", ephemeral=True)          
        else:
            embed = discord.Embed(title="You don't have permission for this command!", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("You don't have permission for this command!", ephemeral=True)

@client.slash_command(name="clean", description="Cleans the DB from unused data", guild_ids=[542773622469689375, 714819340788301934], dm_permission=False)
async def clean(interaction):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if True:
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
            return
        elif int(interaction.author.id) in ADMINS:
            await interaction.response.send_message("Cleaning up...")
            await interaction.channel.trigger_typing()
            pos = -1
            for i in db_channel_obj6:
                try:
                    pos+=1
                    try:
                        int(db_channel_obj6[pos+1].content)
                    except:
                        try:
                            int(db_channel_obj6[pos].content)
                        except:
                            await asyncio.sleep(3)
                            try:
                                await interaction.channel.trigger_typing()
                                await db_channel_obj6[pos].delete()
                                db_channel_obj6.remove(db_channel_obj6[pos])
                            except:
                                pass
                except:
                    pass
            
            for i in local_verification:
                try:
                    test = client.get_channel(int(i))
                    if test == None:
                        test = client.get_guild(int(i))
                        if test == None:
                            await interaction.channel.trigger_typing()
                            nachricht = discord.utils.get(db_channel_obj, content=str(i))
                            try:
                                local_verification.remove(str(i))
                                db_channel_obj.remove(nachricht)
                                await nachricht.delete()
                            except:
                                pass
                            await asyncio.sleep(3)
                except:
                    pass
            
            for i in local_verification:
                try:
                    test = client.get_guild(int(i))
                    if test == None:
                        test = client.get_channel(int(i))
                        if test == None:
                            await interaction.channel.trigger_typing()
                            nachricht = discord.utils.get(db_channel_obj, content=str(i))
                            try:
                                print(nachricht.content)
                            except:
                                pass
                            try:
                                local_verification.remove(str(i))
                                db_channel_obj.remove(nachricht)
                                await nachricht.delete()
                            except:
                                pass
                            await asyncio.sleep(3)
                except:
                    pass

            for i in local_verify_message:
                try:
                    test = client.get_guild(int(i))
                    if test == None:
                        if True:
                            await interaction.channel.trigger_typing()
                            nachricht = discord.utils.get(db_channel_obj6, content=str(i))
                            try:
                                print(nachricht.content)
                            except:
                                pass
                            try:
                                local_verification.remove(str(i))
                                db_channel_obj6.remove(nachricht)
                                await nachricht.delete()
                            except:
                                pass
                            await asyncio.sleep(3)
                except:
                    pass
                

            try:
                pos = -1
                for i in db_channel_obj6:
                    pos+=1
                    try:
                        int(db_channel_obj6[pos+1].content)
                    except:
                        try:
                            int(db_channel_obj6[pos].content)
                        except:
                            await asyncio.sleep(3)
                            try:
                                await interaction.channel.trigger_typing()
                                await db_channel_obj6[pos].delete()
                                db_channel_obj6.remove(db_channel_obj6[pos])
                            except:
                                pass
            except:
                pass

            await interaction.channel.trigger_typing()
            all_roles = []
            for guild in client.guilds:
                for role in guild.roles:
                    all_roles.append(str(role.id))
            await asyncio.sleep(3)
            for i in local_verified_roles:
                try:
                    if not i in all_roles:
                        await interaction.channel.trigger_typing()
                        nachricht = discord.utils.get(local_verified_roles_obj, content=str(i))
                        try:
                            print(nachricht.content)
                        except:
                             pass
                        try:
                            local_verified_roles.remove(str(i))
                            local_verified_roles_obj.remove(nachricht)
                            await nachricht.delete()
                        except:
                            pass
                        await asyncio.sleep(3)
                except:
                    pass
            for i in local_not_verified_roles:
                try:
                    if not i in all_roles:
                        await interaction.channel.trigger_typing()
                        nachricht = discord.utils.get(local_not_verified_roles_obj, content=str(i))
                        try:
                            print(nachricht.content)
                        except:
                             pass
                        try:
                            local_not_verified_roles.remove(str(i))
                            local_not_verified_roles_obj.remove(nachricht)
                            await nachricht.delete()
                        except:
                            pass
                        await asyncio.sleep(3)
                except:
                    pass
                
            await interaction.edit_original_message("Finished!")
        return

@client.slash_command(name="channelinfo", description="Shows information about the channel", options=[discord.Option(name="channel", description="The channel to check", required=True, type=discord.OptionType.channel)], guild_ids=[542773622469689375, 714819340788301934], dm_permission=False)
async def channelinfo(interaction, channel):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if True:
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
            return
        elif int(interaction.author.id) in ADMINS:
            embed = discord.Embed(title=channel.name, description='', color=3566847)
            embed.add_field(name='ID:', value=str(channel.id), inline=False)
            embed.add_field(name='Erstellt am:', value=str(channel.created_at), inline=False)
            
            await interaction.response.send_message(embed=embed)

@client.slash_command(name="svrclear", description="The bot leaves all servers, where it isn't in use", guild_ids=[542773622469689375, 714819340788301934], dm_permission=False)
async def svrclear(interaction):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if True:
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
            return
        elif int(interaction.author.id) in ADMINS:
            await interaction.response.send_message("Leaving unused servers...")
            for guild in client.guilds:
                if not str(guild.id) in local_verification:
                    if not int(guild.id) in ALLOWED_SERVERS:
                        await interaction.channel.trigger_typing()
                        try:
                            await guild.leave()
                            print(f"Left: {guild.id}")
                        except:
                            print(f"Can't leave: {guild.id}")
                        await asyncio.sleep(3)
            await interaction.edit_original_message("Finished!")

@client.slash_command(name="serverperm", description="Shows the bot's permissions on the server", options=[discord.Option(name="server", description="The server to check", type=discord.OptionType.string, required=True)], guild_ids=[542773622469689375, 714819340788301934], dm_permission=False)
async def serverperm(interaction, server):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if True:
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
            return
        if int(interaction.author.id) in ADMINS:
            server = client.get_guild(int(server))
            permissions = []
            if server.me.guild_permissions.kick_members:
                permissions.append("kick_members")
            if server.me.guild_permissions.ban_members:
                permissions.append("ban_members")
            if server.me.guild_permissions.administrator:
                permissions.append("administrator")
            if server.me.guild_permissions.manage_channels:
                permissions.append("manage_channels")
            if server.me.guild_permissions.manage_guild:
                permissions.append("manage_guild")
            if server.me.guild_permissions.add_reactions:
                permissions.append("add_reactions")
            if server.me.guild_permissions.view_audit_log:
                permissions.append("view_audit_log")
            if server.me.guild_permissions.priority_speaker:
                permissions.append("priority_speaker")
            if server.me.guild_permissions.stream:
                permissions.append("stream")
            if server.me.guild_permissions.read_messages:
                permissions.append("read_messages")
            if server.me.guild_permissions.view_channel:
                permissions.append("view_channel")
            if server.me.guild_permissions.send_messages:
                permissions.append("send_messages")
            if server.me.guild_permissions.send_tts_messages:
                permissions.append("send_tts_messages")
            if server.me.guild_permissions.manage_messages:
                permissions.append("manage_messages")
            if server.me.guild_permissions.embed_links:
                permissions.append("embed_links")
            if server.me.guild_permissions.attach_files:
                permissions.append("attach_files")
            if server.me.guild_permissions.read_message_history:
                permissions.append("read_message_history")
            if server.me.guild_permissions.mention_everyone:
                permissions.append("mention_everyone")
            if server.me.guild_permissions.external_emojis:
                permissions.append("external_emojis")
            if server.me.guild_permissions.use_external_emojis:
                permissions.append("use_external_emojis")
            if server.me.guild_permissions.view_guild_insights:
                permissions.append("view_guild_insights")
            if server.me.guild_permissions.connect:
                permissions.append("connect")
            if server.me.guild_permissions.speak:
                permissions.append("speak")
            if server.me.guild_permissions.mute_members:
                permissions.append("mute_members")
            if server.me.guild_permissions.deafen_members:
                permissions.append("deafen_members")
            if server.me.guild_permissions.move_members:
                permissions.append("move_members")
            if server.me.guild_permissions.use_voice_activation:
                permissions.append("use_voice_activation")
            if server.me.guild_permissions.change_nickname:
                permissions.append("change_nickname")
            if server.me.guild_permissions.manage_nicknames:
                permissions.append("manage_nicknames")
            if server.me.guild_permissions.manage_roles:
                permissions.append("manage_roles")
            if server.me.guild_permissions.manage_permissions:
                permissions.append("manage_permissions")
            if server.me.guild_permissions.manage_webhooks:
                permissions.append("manage_webhooks")
            if server.me.guild_permissions.manage_emojis:
                permissions.append("manage_emojis")
            await interaction.response.send_message(permissions)

@client.slash_command(name="owner2server", description="Shows the server from the given owner-id", options=[discord.Option(name="ownerid", description="The owner to check", required=True, type=discord.OptionType.string)], guild_ids=[542773622469689375, 714819340788301934], dm_permission=False)
async def owner2server(interaction, ownerid):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if True:
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
            return
        elif int(interaction.author.id) in ADMINS:
            guilds = []
            for guild in client.guilds:
                if guild.owner_id == int(ownerid):
                    guilds.append(guild.id)
            await interaction.response.send_message(str(guilds))

@client.slash_command(name="vban", description="Bans a server from the bot's service", options=[discord.Option(name="serverid", description="The server to ban", required=True, type=discord.OptionType.string),discord.Option(name="reason", description="The reason for the ban", required=True, type=discord.OptionType.string)], guild_ids=[542773622469689375, 714819340788301934], dm_permission=False)
async def vban(interaction, serverid, reason):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if True:
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
            return
        elif int(interaction.author.id) in ADMINS:
            if True:
                try:
                    serverid = int(serverid)
                except:
                    await interaction.response.send_message("Bitte gebe eine gültige ID ein!")
                    return
            guild = client.get_guild(serverid)
            embed = discord.Embed(title='You are banned from this service!', description=f'Reason: {reason}\nIf you think that this is a mistake, please contact us [here](https://discord.gg/4EKzNBN)', color=16711680)
            
            try:
                usr = await client.fetch_user(guild.owner_id)
                await usr.send(embed=embed)
            except Exception as e:
                print(e)
            embed = discord.Embed(title=f'Server {guild.name} ({serverid}) banned!', color=3566847)
            
            n1 = await client.get_channel(BANNS_CHANNEL_ID).send(serverid)
            await client.get_channel(BANNS_CHANNEL_ID).send(reason)
            banned_server.append(int(serverid))
            banned_server_obj.append(n1)
            try:
                await guild.leave()
            except:
                pass
            await interaction.response.send_message(embed=embed)

@client.slash_command(name="vunban", description="Unbans a server from the bot's service", options=[discord.Option(name="serverid", description="The server to unban", required=True, type=discord.OptionType.string)], guild_ids=[542773622469689375, 714819340788301934], dm_permission=False)
async def vunban(interaction, serverid):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if True:
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
            return
        channel = client.get_channel(BANNS_CHANNEL_ID)
        if int(interaction.author.id) in ADMINS:
            nachrichtx = discord.utils.get(banned_server_obj, content=str(serverid))
            await nachrichtx.delete()
            embed = discord.Embed(title=f'Server {str(serverid)} unbanned!', color=3566847)
            
            await interaction.response.send_message(embed=embed)
            banned_server.remove(int(serverid))
            banned_server_obj.remove(nachrichtx)

@client.slash_command(name="sban", description="Bans a user from the bot-support", options=[discord.Option(name="userid", description="The user to ban", required=True, type=discord.OptionType.string),discord.Option(name="reason", description="The reason for the ban", required=True, type=discord.OptionType.string)], guild_ids=[542773622469689375, 714819340788301934], dm_permission=False)
async def sban(interaction, userid, reason):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if True:
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
            return
        elif int(interaction.author.id) in ADMINS:
            if True:
                try:
                    userid = int(userid)
                except:
                    await interaction.response.send_message("Bitte gebe eine gültige ID ein!")
                    return
            user = await client.fetch_user(userid)
            embed = discord.Embed(title=f'User {user} ({userid}) banned!', color=3566847)
            
            n1 = await client.get_channel(BANNED_USERS_ID).send(userid)
            await client.get_channel(BANNED_USERS_ID).send(reason)
            banned_users.append(int(userid))
            local_banned_users_obj.append(n1)
            await interaction.response.send_message(embed=embed)

@client.slash_command(name="sunban", description="Unbans a server from the bot's service", options=[discord.Option(name="userid", description="The user to unban", required=True, type=discord.OptionType.string)], guild_ids=[542773622469689375, 714819340788301934], dm_permission=False)
async def sunban(interaction, userid):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global savedata
    if True:
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", color=16711680)
            try:
                await interaction.response.send_message(embed=embed, ephemeral=True)
            except:
                await interaction.response.send_message("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", ephemeral=True)
            return
        channel = client.get_channel(BANNED_USERS_ID)
        if int(interaction.author.id) in ADMINS:
            nachrichtx = discord.utils.get(local_banned_users_obj, content=str(userid))
            await nachrichtx.delete()
            embed = discord.Embed(title=f'User {str(userid)} unbanned!', color=3566847)
            
            await interaction.response.send_message(embed=embed)
            banned_users.remove(int(userid))
            local_banned_users_obj.remove(nachrichtx)

@client.event
async def on_ready():
    global banned_users
    global local_verification
    global db_channel_obj
    global db_channel_obj2
    global db_channel_obj6
    global local_verify_message
    global ready
    global banned_server
    global banned_server_obj
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    global local_banned_users_obj
    votes_channel = client.get_channel(742398800664068206)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    if not MAINTENANCE:
        await client.change_presence(activity=discord.Game(name="Starting..."))
    if MAINTENANCE:
        await client.change_presence(activity=discord.Game(name="MAINTENANCE | Starting..."))
    db_channel = []
    db_channel_id = client.get_channel(VERIFY_CHANNEL_ID) # verifizierung
    db_channel_id3 = client.get_channel(MESSAGE_CHANNEL_ID) # message
    banned_users_channel = client.get_channel(BANNED_USERS_ID) # banned users
    banned_channel = client.get_channel(BANNS_CHANNEL_ID) # banns
    verified_roles_channel = client.get_channel(VERIFIED_ROLES_CHANNEL_ID) # verified roles

    async for i in banned_users_channel.history(limit=None):
        try:
            banned_users.append(int(i.content))
        except:
            pass
    await asyncio.sleep(2)
    print("Local banned users loaded!")
    
    async for i in db_channel_id.history(limit=None):
        local_verification.append(i.content)
    await asyncio.sleep(2)
    print("Local verify-message loaded!")
    
    local_banned_users_obj = await banned_users_channel.history(limit=None).flatten()
    await asyncio.sleep(2)
    print("Local banned users obj loaded!")
    
    await asyncio.sleep(2)
    print("Local verification loaded!")
    
    async for i in db_channel_id3.history(limit=None):
        local_verify_message.append(i.content)
    await asyncio.sleep(2)
    print("Local verify-message loaded!")
    
    db_channel_obj = await db_channel_id.history(limit=None).flatten()
    await asyncio.sleep(2)
    print("Local verification obj loaded!")
    
    async for i in db_channel_id3.history(limit=None):
        db_channel_obj6.append(i)
    await asyncio.sleep(2)
    print("Local verify-message obj loaded!")
    async for i in banned_channel.history(limit=None):
        try:
            banned_server.append(int(i.content))
        except:
            pass
    await asyncio.sleep(2)
    print("Local banned servers loaded!")
    banned_server_obj = await banned_channel.history(limit=None).flatten()
    await asyncio.sleep(2)
    print("Local banned servers obj loaded!")
    
    async for i in verified_roles_channel.history(limit=None):
        local_verified_roles.append(i.content)
    await asyncio.sleep(2)
    print("Local verified roles loaded!")
    local_verified_roles_obj = await verified_roles_channel.history(limit=None).flatten()
    await asyncio.sleep(2)
    print("Local verified roles obj loaded!")
    
    ready = True
    print("ready")

    while True:
        if not MAINTENANCE:
            await client.change_presence(activity=discord.Game(name=f'''Problems? DM me for support! | {len(client.guilds)} servers!'''))
        if MAINTENANCE:
            await client.change_presence(activity=discord.Game(name=f"MAINTENANCE | {len(client.guilds)} servers!"))
        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://api.discordextremelist.xyz/v2/bot/{client.user.id}/stats',
                headers={'Authorization': 'DELAPI_09ff823ab349da1f96f41b9a0ab3f4b5-713387523757310042',
                "Content-Type": 'application/json'},
                data=json.dumps({'guildCount': len(client.guilds)
                })) as r:
                    js = await r.json()
                    if js['error'] == True:
                        print(f'Failed to post to discordextremelist.xyz\n{js}')
        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://botsfordiscord.com/api/bot/{client.user.id}',
                headers={'Authorization': '77013a47715ce2ee8b3327af3bc1fcf2fa29d6a0599264e8616f7b8b2b0197ecdcfbfffafb99473c4bbe8777e130abf374307a266fab3ea8ae1658cc59814cdf',
                "Content-Type": 'application/json'},
                data=json.dumps({'server_count': len(client.guilds)
                })) as r:
                    js = await r.json()
        await asyncio.sleep(600)

@client.event
async def on_member_join(member):
    if not member.guild.chunked:
        await member.guild.chunk(cache=True)
    if member.bot:
        return
    global ready
    while True:
        if ready:
            break
        else:
            await asyncio.sleep(5)
#    await client.wait_until_ready()
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    if member.guild.id == 542773622469689375:
        if not str(member.id) in ADMINS:
            await member.kick()
            return
    try:
        if member.guild.id == 541922290095357962:
            owners = []
            for server in client.guilds:
                if not server.id == 541922290095357962:
                    owners.append(server.owner_id)
            if member.id in owners:
                #verification_user_role = discord.utils.get(member.guild.roles, id=741324470379085864)
                #await member.add_roles(verification_user_role)
                general_channel = client.get_channel(741326677245820938)
                announcements_channel = client.get_channel(741326625882374162)
                support_channel = client.get_channel(741326700733923408)
                embed = discord.Embed(title='Welcome to the support-server!', description=f'I automtatically gave you the role to access the bot-related channels.\nYou can talk general in {general_channel.mention}, get support in {support_channel.mention} and see the newest information and updates in {announcements_channel.mention}.  \n\n---\n**I AM A BOT AND THIS MESSAGE WAS AUTOMATED.**\n*Replying to this message will direct your message to the bot support!*', color=3566847)
                
                try:
                    await member.send(embed=embed)
                except:
                    pass
    except:
        pass

@client.event
async def on_guild_join(guild):
    global banned_server
    global ready
    while True:
        if ready:
            break
        else:
            await asyncio.sleep(5)
    await client.wait_until_ready()
    server_owner = await client.fetch_user(guild.owner_id)
    if int(guild.id) in banned_server:
        embed = discord.Embed(title='You are banned from this service!', description='If you think that this is a mistake, please contact us [here](https://discord.gg/4EKzNBN).', color=16711680)
        
        try:
            await server_owner.send(embed=embed)
        except:
            pass
        await guild.leave()
        return
    realygirllp = await client.fetch_user(513071093976793099)
    embed = discord.Embed(title='Welcome!', description='Hey, thank you for adding me to your server!\nPlease read the instructions [here](https://realygirllp.jimdofree.com/discord/verification-bot/) for setup.\n\nWe recommend to join our [Server](https://discord.gg/A9us3fv) to get all updates and important information. After joining, you will automatically get the permissions to access the bot-related channels. If not, please type !add-verify in commands. Don\'t forget to verify yourself!\n\n---\n**I AM A BOT AND THIS MESSAGE WAS AUTOMATED.**\n*Replying to this message will direct your message to the bot support!*', color=3566847)
    
    try:
        await server_owner.send(embed=embed)
        dms = True
    except:
        dms = False
    features = []
    for feature in guild.features:
        features.append(feature)
    members = []
    bots = []
    for member in guild.members:
        if member.bot:
            bots.append(member)
        else:
            members.append(member)
    embed = discord.Embed(title='Neuer Server', color=0x3eff00)
    embed.add_field(name="Servername", value=guild.name, inline=True)
    embed.add_field(name="Server-ID", value=guild.id, inline=True)
    try:
        embed.add_field(name="Besitzer", value=f"{server_owner} ({server_owner.id})", inline=True)
    except:
        try:
            embed.add_field(name="Besitzer", value=f"{client.get_user(guild.owner_id).name} ({guild.owner_id})", inline=True)
        except Exception as e:
            print(e)
    embed.add_field(name="Besitzer DMs aktiv", value=f"{dms}", inline=True)
    embed.add_field(name="Erstellt", value=guild.created_at, inline=True)
    embed.add_field(name="Features", value=features, inline=True)
    try:
        embed.set_thumbnail(url=str(guild.icon.url))
    except:
        pass

    await client.get_channel(SERVER_JOIN_LEAVE_CHANNEL_ID).send(embed=embed)

@client.event
async def on_guild_remove(guild):
    global ready
    while True:
        if ready:
            break
        else:
            await asyncio.sleep(5)
    await client.wait_until_ready()
    realygirllp = await client.fetch_user(513071093976793099)
    try:
        server_owner = await client.fetch_user(guild.owner_id)
    except:
        server_owner = None
    features = []
    for feature in guild.features:
        features.append(feature)
    members = []
    bots = []
    for member in guild.members:
        if member.bot:
            bots.append(member)
        else:
            members.append(member)
    embed = discord.Embed(title='Ein Server weniger', color=0xFF0000)
    embed.add_field(name="Servername", value=guild.name, inline=True)
    embed.add_field(name="Server-ID", value=guild.id, inline=True)
    try:
        embed.add_field(name="Besitzer", value=f"{server_owner} ({server_owner.id})", inline=True)
    except:
        try:
            embed.add_field(name="Besitzer", value=f"{client.get_user(guild.owner_id).name} ({guild.owner_id})", inline=True)
        except:
            pass
    embed.add_field(name="Erstellt", value=guild.created_at, inline=True)
    embed.add_field(name="Features", value=features, inline=True)
    
    try:
        embed.set_thumbnail(url=str(guild.icon.url))
    except:
        pass
    try:
        await client.get_channel(SERVER_JOIN_LEAVE_CHANNEL_ID).send(embed=embed)
    except:
        pass
    try:
        if str(guild.id) in local_verify_message:
            nachricht = discord.utils.get(db_channel_obj6, content=str(guild.id))
            await nachricht.delete()
            db_channel_obj6.remove(nachricht)
            local_verify_message.remove(str(guild.id))
    except:
        pass
    try:
        if str(guild.id) in local_verification:
            nachricht = discord.utils.get(db_channel_obj, content=str(guild.id))
            await nachricht.delete()
            db_channel_obj.remove(nachricht)
            local_verification.remove(str(guild.id))
    except:
        pass
    try:
        for channel in guild.channels:
            if str(channel.id) in local_verification:
                nachricht = discord.utils.get(db_channel_obj, content=str(channel.id))
                await nachricht.delete()
    except:
        pass

    try:
        for role in guild.roles:
            if str(role.id) in local_verified_roles:
                nachricht = discord.utils.get(local_verified_roles_obj, content=str(role.id))
                await nachricht.delete()
            if str(role.id) in local_not_verified_roles:
                nachricht = discord.utils.get(local_not_verified_roles_obj, content=str(role.id))
                await nachricht.delete()
    except:
        pass


@client.event
async def on_message(message):
    global s_code
    global banned_users
    global local_banned_users_obj
    global banned_server
    global banned_server_obj
    global local_verify_message
    global db_channel_obj6
    global ready
    await client.wait_until_ready()
    global db_channel_obj
    global ssave
    global sp
    global add_lock
    global local_verification
    global local_verified_roles
    global local_verified_roles_obj
    global local_not_verified_roles
    global local_not_verified_roles_obj
    if message.author == client.user:
        return
    if message.author.bot:
        return
    if type(message.channel) == discord.DMChannel :
        if message.content.startswith(f'!reply') and message.author.id in ADMINS:
            name = message.content
            name = name.replace('!reply ', '')
            namel = name.split()
            name4 = namel[0]
            name5 = namel[1]
            name = name.replace(name4, "")
            name = name.replace(name5, "")
            name4 = int(name4)
            name2 = await client.fetch_user(name4)
            name5 = await name2.fetch_message(name5)
            name3 = name
            name3 = name3.lstrip()
            name3 = f"Hey {name2.name}, thank you for contacting our support.\n\n{name3}\n\nFeel free to contact us again or join our [Server](https://discord.gg/ayNqnDg) if you have more questions or problems.\nThe Verification-Team"
            await message.author.send((((('Die Nachricht wurde an ' + str(name2)) + ' (') + str(name2.id)) + ') ') + ' verschickt!')
            mmangehängt = message.attachments
            try:
                try:
                    bild1 = mmangehängt[0]
                    bild1 = bild1.url
                    embed = discord.Embed(title='**You got a message from the bot-support:**', description=(name3 + '\n') + bild1, color=3566847)
                except:
                    embed = discord.Embed(title='**You got a message from the bot-support:**', description=name3, color=3566847)
                await name5.reply(embed=embed)
            except:
                await message.author.send('Die Nachricht konnte nicht zugestellt werden.\nMöglicherweise sind keine DMs aktiv.')
            return
        if message.content.startswith(f'!re'):
            return
        try:
            int(message.content)
            return
        except:
            pass
        content = message.content.lower()
        
        if int(message.author.id) in banned_users:
            embed = discord.Embed(title='You are currently banned from the support!', description='If you think this is a mistake, please contact us [here](https://discord.gg/4EKzNBN)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if len(message.content) < 30:
            embed = discord.Embed(title='Your support question is too short! Please include more useful information about your problem/question with the bot. (At least 30 characters)', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        wortliste = content.split()
        if len(wortliste) < 8:
            embed = discord.Embed(title='Your support question is too short! Please include more useful information about your problem/question with the bot. (At least 8 words)', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        wwwww = message.content.lower()
        wwwww = wwwww.replace(" ", "")
        for word in CHAT_FILTER:
            if word in wwwww:
                embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
                
                try:
                    await message.reply(embed=embed)
                    return
                except:
                    return
                
        if "aaaa" in content or "bbbb" in content or "cccc" in content or "dddd" in content or "eeee" in content or "ffff" in content or "gggg" in content or "hhhh" in content or "iiii" in content or "jjjj" in content or "kkkk" in content or "llll" in content or "mmmm" in content or "nnnn" in content or "oooo" in content or "pppp" in content or "qqqq" in content or "vvvv" in content or "wwww" in content or "xxxx" in content or "yyyy" in content or "zzzz" in content or "ääää" in content or "öööö" in content or "üüüü" in content or "...." in content or ",,,," in content or "----" in content or "!!!!" in content or "????" in content or "0000" in content or "1111" in content or "2222" in content or "3333" in content or "4444" in content or "5555" in content or "6666" in content or "7777" in content or "8888" in content or "9999" in content:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if message.content == ssave:
            embed = discord.Embed(title='You already sent this question! Please be patient until bot support answers you.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if content[0] == content[5] and content[0] == content[3] and content[0] == content[10]:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if content[0] == content[3] and content[0] == content[6] and content[0] == content[9]:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if content[0] == content[1] and content[0] == content[2] and content[0] == content[3]:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if content[1] == content[2] and content[1] == content[3] and content[1] == content[4]:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if wortliste[0] == wortliste[5] and wortliste[0] == wortliste[3] and wortliste[0] == wortliste[10]:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if wortliste[0] == wortliste[3] and wortliste[0] == wortliste[6] and wortliste[0] == wortliste[9]:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if wortliste[0] == wortliste[1] and wortliste[0] == wortliste[2] and wortliste[0] == wortliste[3]:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        if wortliste[1] == wortliste[2] and wortliste[1] == wortliste[3] and wortliste[1] == wortliste[4]:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return
        lettercount = 0
        if "a" in content:
            lettercount += 1
        if "b" in content:
            lettercount += 1
        if "c" in content:
            lettercount += 1
        if "d" in content:
            lettercount += 1
        if "e" in content:
            lettercount += 1
        if "f" in content:
            lettercount += 1
        if "g" in content:
            lettercount += 1
        if "h" in content:
            lettercount += 1
        if "i" in content:
            lettercount += 1
        if "j" in content:
            lettercount += 1
        if "k" in content:
            lettercount += 1
        if "l" in content:
            lettercount += 1
        if "m" in content:
            lettercount += 1
        if "n" in content:
            lettercount += 1
        if "o" in content:
            lettercount += 1
        if "p" in content:
            lettercount += 1
        if "q" in content:
            lettercount += 1
        if "r" in content:
            lettercount += 1
        if "s" in content:
            lettercount += 1
        if "t" in content:
            lettercount += 1
        if "u" in content:
            lettercount += 1
        if "v" in content:
            lettercount += 1
        if "w" in content:
            lettercount += 1
        if "x" in content:
            lettercount += 1
        if "y" in content:
            lettercount += 1
        if "z" in content:
            lettercount += 1
        if "ä" in content:
            lettercount += 1
        if "ö" in content:
            lettercount += 1
        if "ü" in content:
            lettercount += 1
        if "ß" in content:
            lettercount += 1
        if "!" in content:
            lettercount += 1
        if "\"" in content:
            lettercount += 1
        if "§" in content:
            lettercount += 1
        if "$" in content:
            lettercount += 1
        if "%" in content:
            lettercount += 1
        if "&" in content:
            lettercount += 1
        if "/" in content:
            lettercount += 1
        if "(" in content:
            lettercount += 1
        if ")" in content:
            lettercount += 1
        if "=" in content:
            lettercount += 1
        if "?" in content:
            lettercount += 1
        if "\\" in content:
            lettercount += 1
        if "{" in content:
            lettercount += 1
        if "}" in content:
            lettercount += 1
        if "0" in content:
            lettercount += 1
        if "1" in content:
            lettercount += 1
        if "2" in content:
            lettercount += 1
        if "3" in content:
            lettercount += 1
        if "4" in content:
            lettercount += 1
        if "5" in content:
            lettercount += 1
        if "6" in content:
            lettercount += 1
        if "7" in content:
            lettercount += 1
        if "8" in content:
            lettercount += 1
        if "9" in content:
            lettercount += 1
        if "." in content:
            lettercount += 1
        if ":" in content:
            lettercount += 1
        if "-" in content:
            lettercount += 1
        if "_" in content:
            lettercount += 1
        if "," in content:
            lettercount += 1
        if "." in content:
            lettercount += 1
        if lettercount < 5:
            embed = discord.Embed(title='Your support question looks like spam! Please include more useful information about your problem/question with the bot.', description='If you think this is a mistake, please ask on our [support-server](https://discord.gg/A9us3fv)', color=16711680)
            
            try:
                await message.reply(embed=embed)
                return
            except:
                return

        if True:
            s_code = random.randint(100000, 999999)
            embed = discord.Embed(title='Confirm Support-Request', description=f'You want to send\n```{message.content}```\nto the bot-support.\nAre you sure, you want to do that?\n\n*Notes:\n-Before you send your request, please read [setup instructions and the other things](https://realygirllp.jimdofree.com/discord/verification-bot/).\n-Support-Answers can take up to **48 hours**. **Don\'t** send the same request again until the 48 hours are up.\n- Support is currently only available in **English and German**. Support-requests in other languages will get answered in English.\n- We **can\'t** help with permission problems on 3rd servers if you are not the owner. Please contact a server admin/owner instead!\n- This is only the support for **this** bot. We can\'t help you with Discord-problems, server-problems or other bots. Please contact [Discord-support](http://dis.gd/support) or support for the other bot/server instead!\n- We will **not** answer, when your request is **spam, not understandable** or **doesn\'t match the points above**!\n**- Support-abuse will result in a ban!***\n\nConfirm with code: **{s_code}**\n*By sending the support request, you confirm that you have read and understood the points above.*', color=0xff9300)
            embed.set_footer(text="Code doesn't work? Send your support-request again!")
            cmsg = await message.reply(embed=embed)
            while True:
                msg2 = await client.wait_for('message')
                if type(msg2.channel) == discord.DMChannel:
                    if msg2.content == str(s_code):
                        await cmsg.delete()
                        break
                    try:
                        int(msg2.content)
                    except:
                        await cmsg.delete()
                        return
        
        embed = discord.Embed(title='Thank you for your message! We will give you a reply, as fast as possible.', description='Please make sure that DMs are active and the bot is on your server, so that we can reach you.', color=3566847)
        
        try:
            await message.channel.send(embed=embed)
        except:
            return
        author = message.author
        mmangehängt = message.attachments
        ssave = message.content
        try:
            bild1 = mmangehängt[0]
            bild1 = bild1.url
            mod1 = await client.fetch_user(513071093976793099)
            embed = discord.Embed(title="New Support request", description=f"{message.content}\n{bild1}", color=3566847)
            embed.add_field(name=f"by {message.author} ({message.author.id})", value=f"!reply {message.author.id} {message.id}")
            await mod1.send(embed=embed)
        except:
            mod1 = await client.fetch_user(513071093976793099)
            embed = discord.Embed(title="New Support request", description=f"{message.content}", color=3566847)
            embed.add_field(name=f"by {message.author} ({message.author.id})", value=f"!reply {message.author.id} {message.id}")
            await mod1.send(embed=embed)
            return

    if str(message.channel.id) in local_verification:
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        if not str("('administrator', True)") in perm or message.author.id in sp:
            await message.delete()

    """
    #if message.guild.id == 714819340788301934:
    if True:
        code29x = []
        for messagex in db_channel_obj2:
            code29x.append(messagex.content)
        try:
            code30 = code29x.index(str(message.guild.id))
            prefix = code29x[code30-1]
        except:
            prefix = "!"
            
    if message.content.startswith(f'{prefix}help') or message.content.startswith(f'{prefix}commands'):
        embed = discord.Embed(title='Verification-Help', description='https://realygirllp.jimdofree.com/discord/verification-bot/', color=3566847)
        embed.add_field(name="---", value="Admin-Commands", inline=False)
        embed.add_field(name=f"{prefix}add-verification", value="Add the verification to the channel, where you run the command (makes it a verify-channel)", inline=False)
        embed.add_field(name=f"{prefix}remove-verification", value="Remove the verification (verify-channel) from the channel, where you run the command. ", inline=False)
        embed.add_field(name=f"{prefix}check-verify-channel", value="Checks if the channel, where you run the command is a verify-channel", inline=False)
        embed.add_field(name=f"{prefix}check-verification", value="Checks whether errors occurred during the setup of the verification (or later) that could cause problems. You should run this command after !add-verification is finished. Note: Not every error is a problem!", inline=False)
        embed.add_field(name=f"{prefix}verify-message", value="Customize the message, when a new user types !verify. You can include the code with {code}. Example: \"!verify-message Welcome to the Server! Please verify yourself with the code {code}\" ", inline=False)
        embed.add_field(name=f"{prefix}prefix", value="Customize the bots prefix for commands. Default is \"!\".", inline=False)
        embed.add_field(name=f"{prefix}mverify USERID", value="Manually verify a user", inline=False)
        embed.add_field(name=f"{prefix}unverify USERID", value="Manually unverify a user", inline=False)
        embed.add_field(name=f"{prefix}update", value="Updates your \"Verified\" and \"Not verified\"-roles to renameable roles. You only have to run this command, when you already used the bot before the 2.0 update.", inline=False)
        embed.add_field(name=f"---", value="User-Commands", inline=False)
        embed.add_field(name=f"{prefix}verify", value="Generates a verification code. Only runs in verify-channel. Message with code will be deleted in 5 minutes.", inline=False)
        embed.add_field(name=f"{prefix}verify [NUMBER]", value="Redeem a generated verification-code", inline=False)
        embed.add_field(name=f"{prefix}verification-help", value="Shows a link to this website", inline=False)
        
        try:
            await message.reply(embed=embed)
        except:
            await message.reply("This message is too long to send it as text. Please enable embeds on your server!")
    
    if message.channel.id == 785544074199433266:
        try:
            banned_users.append(int(message.content))
        except:
            pass

    if message.content.startswith("<@!713387523757310042>"):
        embed = discord.Embed(title=f'The bot\'s current prefix is: {prefix}', color=3566847)
        try:
            msg = await message.reply(embed=embed)
        except:
            msg = await message.reply(f'The bot\'s current prefix is: {prefix}')

    if message.content.startswith(f'{prefix}verification-help'):
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        user = message.author
        #if str("('administrator', True)") in perm or message.author.id in sp:
        if True:
            embed = discord.Embed(title='Verify your users on your Discord-Server', description='[How to use and commands](https://realygirllp.jimdofree.com/discord/verification-bot/)', color=3566847)
            
            try:
                await message.reply(embed=embed)
            except:
                await message.reply("Verify your users on your Discord-Server\nhttps://realygirllp.jimdofree.com/discord/verification-bot/")
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
    if message.content.startswith(f'{prefix}add-verification'):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.channel.send(embed=embed)
            except:
                failmsg = await message.channel.send("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.channel.send(embed=embed)
            except:
                failmsg = await message.channel.send("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_\nThis message will be automatically deleted in 10 seconds.")
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        perm = []
        botperm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        for i in message.channel.guild.me.guild_permissions:
            botperm.append(str(i))
        user = message.author
        if str("('administrator', True)") in perm or message.author.id in sp:
            embed = discord.Embed(title="Subcommands", description="**-exclude #channel1 #channel2** | Excludes text-channels from being changed by the bot\n\n**-seteveryone** | Uses @everyone-role instead of Not verified role\n\n**-useverified role-id** | Uses this role as Verified-role\n\n**-usenotverified role-id** | Uses this role as Not verified-role\n\n**-skipmm** | Skips check of **manage_messages**-permission in the Verify-channel (not recommended)\n\n**-start** | Starts BANNED_USERS_ID, color=3566847)
            infomsg = await message.channel.send(embed=embed)
            #return
            noverify = False
            if not "-skipmm" in message.content:
                try:
                    await message.delete()
                except:
                    embed = discord.Embed(title=f'Failed to delete messages! Please ensure, that I have the **manage_messages** permission and try again.\nType "{prefix}add-verification -skipmm" to continue without this permission (not recommended!)', description='This message will be automatically deleted in 10 seconds.', color=16711680)
                    
                    try:
                        failmsg = await message.channel.send(embed=embed)
                    except:
                        failmsg = await message.channel.send(f"Failed to delete messages! Please ensure, that I have the **manage_messages** permission and try again.\nType \"{prefix}add-verification -skipmm\" to continue without this permission (not recommended!)\nThis message will be automatically deleted in 10 seconds.")
                    await asyncio.sleep(5)
                    try:
                        await failmsg.delete()
                    except:
                        pass
                    return
            seteveryone = False
            if "-seteveryone" in message.content:
                seteveryone = True
            useverified = False
            if "-useverified" in message.content:
                useverified = True
                msgc = message.content.split()
                c = -1
                for i in msgc:
                    c+=1
                    if i == "-useverified":
                        try:
                            role2 = discord.utils.get(message.guild.roles, id=int(msgc[c+1]))
                            if role2 == None:
                                embed = discord.Embed(title=f'Role with ID {msgc[c+1]} not found!', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                                
                                try:
                                    failmsg = await message.channel.send(embed=embed)
                                except:
                                    failmsg = await message.channel.send(f"f'Role with ID {msgc[c+1]} not found!\nThis message will be automatically deleted in 5 seconds.")
                                await asyncio.sleep(5)
                                try:
                                    await failmsg.delete()
                                except:
                                    pass
                                return
                        except:
                            embed = discord.Embed(title=f'Role with ID {msgc[c+1]} not found!', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                            
                            try:
                                failmsg = await message.channel.send(embed=embed)
                            except:
                                failmsg = await message.channel.send(f"f'Role with ID {msgc[c+1]} not found!\nThis message will be automatically deleted in 5 seconds.")
                            await asyncio.sleep(5)
                            try:
                                await failmsg.delete()
                            except:
                                pass
                            return
            usenotverified = False
            if "-usenotverified" in message.content:
                usenotverified = True
                msgc = message.content.split()
                c = -1
                for i in msgc:
                    c+=1
                    if i == "-usenotverified":
                        try:
                            role1 = discord.utils.get(message.guild.roles, id=int(msgc[c+1]))
                            if role1 == None:
                                embed = discord.Embed(title=f'Role with ID {msgc[c+1]} not found!', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                                
                                try:
                                    failmsg = await message.channel.send(embed=embed)
                                except:
                                    failmsg = await message.channel.send(f"f'Role with ID {msgc[c+1]} not found!\nThis message will be automatically deleted in 5 seconds.")
                                await asyncio.sleep(5)
                                try:
                                    await failmsg.delete()
                                except:
                                    pass
                                return
                        except:
                            embed = discord.Embed(title=f'Role with ID {msgc[c+1]} not found!', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                            
                            try:
                                failmsg = await message.channel.send(embed=embed)
                            except:
                                failmsg = await message.channel.send(f"f'Role with ID {msgc[c+1]} not found!\nThis message will be automatically deleted in 5 seconds.")
                            await asyncio.sleep(5)
                            try:
                                await failmsg.delete()
                            except:
                                pass
                            return
            if "-skipmm" in message.content:
                embed = discord.Embed(title='WARNING: You are currently skipping the check for the **manage_messages** permission.\nThis could cause unwanted problems. Type "yes" to continue anyway.', description='This message will be automatically deleted when finished.', color=0xff9300)
                
                try:
                    try:
                        norole_msg = await message.channel.send(embed=embed)
                    except:
                        norole_msg = await message.channel.send("WARNING: You are currently skipping the check for the **manage_messages** permission.\nThis could cause unwanted problems. Type \"yes\" to continue anyway.\nThis message will be automatically deleted when finished.")
                    msg2 = await client.wait_for('message')
                    if msg2.content == "yes":
                        pass
                    else:
                        await norole_msg.delete()
                        return
                    
                except:
                    embed = discord.Embed(title='An unknown error has occurred. Please contact us with the Error Code 1 via the bot as DM and we will help you.', description='This message will be automatically deleted in 10 seconds.', color=16711680)
                    
                    try:
                        failmsg = await message.channel.send(embed=embed)
                    except:
                        failmsg = await message.channel.send("An unknown error has occurred. Please contact us with the Error Code 1 via the bot as DM and we will help you.\nThis message will be automatically deleted in 10 seconds.")
                    await asyncio.sleep(10)
                    try:
                        await failmsg.delete()
                    except:
                        pass
                    try:
                        await message.delete()
                    except:
                        pass
                    
            if "-noverify" in message.content:
                noverify = True

            exclude = []
            if "-exclude" in message.content:
                for channel in message.channel_mentions:
                    exclude.append(channel)
            
            if message.guild.id in add_lock:
                embed = discord.Embed(title='Please wait 5 minutes, until you run the command again.\n(Discord API restriction)', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                
                try:
                    failmsg = await message.channel.send(embed=embed)
                except:
                    failmsg = await message.channel.send("Please wait 5 minutes, until you run the command again.\n(Discord API restriction)\nThis message will be automatically deleted in 5 seconds.")
                await asyncio.sleep(5)
                try:
                    await failmsg.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
                return
            guild = message.guild
            embed = discord.Embed(title='Setup is now running. This can take a few minutes...\n(Discord API restriction)', description='This message will be automatically deleted when finished.', color=3566847)
            
            try:
                wait_msg = await message.channel.send(embed=embed)
            except:
                wait_msg = await message.channel.send("Setup is now running. This can take a few minutes...\n(Discord API restriction)\nThis message will be automatically deleted when finished.")
            await message.channel.trigger_typing()
            roles = []
            for i in guild.roles:
                roles.append(i.name)
            if not 'Verified' in roles and not useverified:
                try:
                    r = await guild.create_role(name='Verified')
                    if not str(r.id) in local_verified_roles:
                        r2 = await client.get_channel(VERIFIED_ROLES_CHANNEL_ID).send(r.id)
                        local_verified_roles.append(r2.content)
                        local_verified_roles_obj.append(r2)
                except:
                    embed = discord.Embed(title='Failed to create "Verified"-Role! Please ensure, that I have the **manage_roles** permission and try again!', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                    
                    try:
                        failmsg = await message.channel.send(embed=embed)
                    except:
                        failmsg = await message.channel.send("Failed to create \"Verified\"-Role! Please ensure, that I have the **manage_roles** permission and try again!\nThis message will be automatically deleted in 5 seconds.")
                    await asyncio.sleep(5)
                    try:
                        await failmsg.delete()
                    except:
                        pass
                    try:
                        await wait_msg.delete()
                    except:
                        pass
                    try:
                        await norole_msg.delete()
                    except:
                        pass
                    return

            await asyncio.sleep(2)
            if not 'Not verified' in roles and not usenotverified and not seteveryone:
                try:
                    r = await guild.create_role(name='Not verified')
                    if not str(r.id) in local_verified_roles:
                        r2 = await client.get_channel(769855532885344306).send(r.id)
                        local_not_verified_roles.append(r2.content)
                        local_not_verified_roles_obj.append(r2)
                except:
                    embed = discord.Embed(title='Failed to create "Not Verified"-Role! Please ensure, that I have the **manage_roles** permission and try again!', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                    
                    try:
                        failmsg = await message.channel.send(embed=embed)
                    except:
                        failmsg = await message.channel.send("Failed to create \"Not Verified\"-Role! Please ensure, that I have the **manage_roles** permission and try again!\nThis message will be automatically deleted in 5 seconds.")
                    await asyncio.sleep(5)
                    try:
                        await failmsg.delete()
                    except:
                        pass
                    try:
                        await wait_msg.delete()
                    except:
                        pass
                    try:
                        await norole_msg.delete()
                    except:
                        pass
                    return
            if not str(guild.id) in local_verification:
                msg = await client.get_channel(713392523502157946).send(guild.id)
                local_verification.append(str(guild.id))
                db_channel_obj.append(msg)
            if not str(message.channel.id) in local_verification:
                msg = await client.get_channel(713392523502157946).send(message.channel.id)
                local_verification.append(str(message.channel.id))
                db_channel_obj.append(msg)
            try:
                role1 = role1
            except:
                role1 = discord.utils.get(message.guild.roles, name='Not verified')
            try:
                role2 = role2
            except:
                role2 = discord.utils.get(message.guild.roles, name='Verified')
            print(role1)
            print(role2)
            role3 = discord.utils.get(message.guild.roles, name='@everyone')
            role4 = discord.utils.get(message.guild.roles, name='Verification')
            add_lock.append(guild.id)
            clocked = False
            try:
                failed_channels = []
                for i in guild.channels:
                    changed_roles = []
                    for role in i.changed_roles:
                        changed_roles.append(role.name)
                    if not i in exclude:
                        if not "Verified" in changed_roles or not "Not verified" in changed_roles:
                                try:
                                    await asyncio.sleep(3)
                                    await message.channel.trigger_typing()
                                    if not "-usenotverified" in message.content and not seteveryone:
                                        await i.set_permissions(role1, overwrite=discord.PermissionOverwrite(read_messages = False, send_messages=False))
                                    await asyncio.sleep(3)
                                    if not "-useverified" in message.content:
                                        await i.set_permissions(role2, overwrite=discord.PermissionOverwrite(read_messages = True, send_messages=True))
                                    await i.set_permissions(role4, overwrite=discord.PermissionOverwrite(read_messages = True, send_messages=True))
                                    if seteveryone:
                                        await asyncio.sleep(3)
                                        await i.set_permissions(role3, overwrite=discord.PermissionOverwrite(read_messages = False, send_messages=False))
                                except Exception as e:
                                    print(e)
                                    if not clocked:
                                        if not len(failed_channels) >= 10:
                                            if not i.name in failed_channels:
                                                failed_channels.append(str(i.name))
                                                clocked = True
                if not seteveryone:
                    await message.channel.set_permissions(role1, overwrite=discord.PermissionOverwrite(read_messages = True, send_messages=True))
                await message.channel.set_permissions(role2, overwrite=discord.PermissionOverwrite(read_messages = False, send_messages=False))
                await message.channel.set_permissions(role4, overwrite=discord.PermissionOverwrite(read_messages = True, send_messages=True))
                if seteveryone:
                    await message.channel.set_permissions(role3, overwrite=discord.PermissionOverwrite(read_messages = True, send_messages=True))
            except:
                pass
            if not failed_channels == []:
                embed = discord.Embed(title=f'Failed to set the permissions for some channels!\nPlease check the channel permissions and use {prefix}check-verification to check again.', description='This message will be automatically deleted in 10 seconds.', color=16711680)
                
                try:
                    failmsg = await message.channel.send(embed=embed)
                except:
                    failmsg = await message.channel.send(f"Failed to set the permissions for some channels!\nPlease check the channel permissions and use {prefix}check-verification to check again.\nThis message will be automatically deleted in 10 seconds.")
                await asyncio.sleep(10)
                try:
                    await failmsg.delete()
                except:
                    pass
            mlocked = True
            try:
                failed_members = []
                for member in guild.members:
                    if not member.bot:
                        memberroles = []
                        for role in member.roles:
                            memberroles.append(role.name)
                        verified_role = discord.utils.get(member.guild.roles, name='Verified')
                        if not seteveryone:
                            not_verified_role = discord.utils.get(member.guild.roles, name='Not verified')
                        if not "Verified" in memberroles and not "Not verified" in memberroles:
                            try:
                                await asyncio.sleep(3)
                                await message.channel.trigger_typing()
                                await asyncio.sleep(3)
                                if not noverify:
                                    await member.add_roles(verified_role)
                                if noverify and not seteveryone:
                                    await member.add_roles(not_verified_role)
                            except:
                                if not mlocked:
                                    if not len(failed_members) >= 10:
                                        if not member.name in failed_members:
                                            failed_members.append(str(member.name))
                                            mlocked = True
            except:
                pass
            if not failed_members == []:
                embed = discord.Embed(title=f'Failed to set the permissions for some members!\nPlease check the member roles and use {prefix}check-verification to check again.', description='This message will be automatically deleted in 10 seconds.', color=16711680)
                
                try:
                    failmsg = await message.channel.send(embed=embed)
                except:
                    failmsg = await message.channel.send(f"Failed to set the permissions for some members!\nPlease check the member roles and use {prefix}check-verification to check again.\nThis message will be automatically deleted in 10 seconds.")
                await asyncio.sleep(10)
                try:
                    await failmsg.delete()
                except:
                    pass
            embed = discord.Embed(title='Verify-Channel set to the current channel!', description='This message will be automatically deleted in 5 seconds.', color=3566847)
            
            try:
                msg = await message.channel.send(embed=embed)
            except:
                msg = await message.channel.send("Verify-Channel set to the current channel!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await norole_msg.delete()
            except:
                pass
            try:
                await wait_msg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            try:
                await msg.delete()
            except:
                pass
            
            await asyncio.sleep(300)
            add_lock.remove(guild.id)
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.channel.send(embed=embed)
            except:
                failmsg = await message.channel.send("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            
    if message.content.startswith(f'{prefix}remove-verification'):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_\nThis message will be automatically deleted in 10 seconds.")
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        user = message.author
        if str("('administrator', True)") in perm or message.author.id in sp:
            if str(message.channel.id) in local_verification:
                guild = message.guild
                try:
                    for i in guild.channels:
                        if str(i.id) in local_verification:
                            vchannel = str(i.id)
                except:
                    pass
                nachricht = discord.utils.get(db_channel_obj, content=vchannel)
                try:
                    await nachricht.delete()
                    local_verification.remove(vchannel)
                    embed = discord.Embed(title='This verify-channel got deleted!', description='This message will be automatically deleted in 5 seconds.', color=3566847)
                    
                    try:
                        sucmsg = await message.reply(embed=embed)
                    except:
                        sucmsg = await message.reply("This verify-channel got deleted!\nThis message will be automatically deleted in 5 seconds.")
                    await asyncio.sleep(5)
                    try:
                        await sucmsg.delete()
                    except:
                        pass
                    try:
                        await failmsg.delete()
                    except:
                        pass
                    try:
                        await message.delete()
                    except:
                        pass
                except:
                    embed = discord.Embed(title="This channel isn't a verify-channel!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
                    
                    try:
                        failmsg = await message.reply(embed=embed)
                    except:
                        failmsg = await message.reply("This channel isn't a verify-channel!\nThis message will be automatically deleted in 5 seconds.")
                    await asyncio.sleep(5)
                    try:
                        await failmsg.delete()
                    except:
                        pass
                    try:
                        await sucmsg.delete()
                    except:
                        pass
                    try:
                        await message.delete()
                    except:
                        pass
            else:
                embed = discord.Embed(title="This channel isn't a verify-channel!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
                
                try:
                    failmsg = await message.reply(embed=embed)
                except:
                    failmsg = await message.reply("This channel isn't a verify-channel!\nThis message will be automatically deleted in 5 seconds.")
                await asyncio.sleep(5)
                try:
                    await failmsg.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass

    if message.content.startswith(f"{prefix}prefix"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_\nThis message will be automatically deleted in 10 seconds.")
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        user = message.author
        if str("('administrator', True)") in perm or message.author.id in sp:
            nachricht = message.content.replace(f"{prefix}prefix ", "")
            nachricht = message.content.replace(f"{prefix}prefix", "")
            try:
                int(nachricht)
                embed = discord.Embed(title="You can't use just numbers as prefix!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
                
                try:
                    failmsg = await message.reply(embed=embed)
                except:
                    failmsg = await message.reply("You can't use just numbers as prefix!\nThis message will be automatically deleted in 5 seconds.")
                await asyncio.sleep(5)
                try:
                    await failmsg.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
                return
            except:
                pass
            if nachricht == "" or nachricht == " ":
                embed = discord.Embed(title="You have to include a prefix!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
                
                try:
                    failmsg = await message.reply(embed=embed)
                except:
                    failmsg = await message.reply("You have to include a prefix!\nThis message will be automatically deleted in 5 seconds.")
                await asyncio.sleep(5)
                try:
                    await failmsg.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
                return
            channel = client.get_channel(PREFIX_CHANNEL_ID)
            try:
                if str(message.guild.id) in local_prefix:
                    guild = message.guild
                nachricht1 = discord.utils.get(db_channel_obj2, content=str(message.guild.id))
                await nachricht1.delete()
            except:
                pass
            n1 = await channel.send(str(message.guild.id))
            n2 = await channel.send(nachricht)
            local_prefix.insert(0, str(message.guild.id))
            local_prefix.insert(0,nachricht)
            db_channel_obj2.insert(0, n1)
            db_channel_obj2.insert(0, n2)
            embed = discord.Embed(title=f'Prefix set to:\n{nachricht}', color=3566847)
            
            try:
                await message.reply(embed=embed)
            except:
                await message.reply(f"Prefix set to:\n{nachricht}")
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass

    if message.content.startswith(f"{prefix}unverify") and not message.content == f"{prefix}unverify-all":
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_\nThis message will be automatically deleted in 10 seconds.")
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        if str("('administrator', True)") in perm or message.author.id in sp:
            erwähnungen = message.mentions
            if erwähnungen == []:
                try:
                    name1 = message.content
                    name1 = name1.replace(f'{prefix}unverify ', '')
                    try:
                        name1 = int(name1)
                    except:
                        embed = discord.Embed(title=f'Please enter a valid User-ID or @mention!', description='', color=16711680)
                        try:
                            await message.reply(embed=embed)
                        except:
                            await message.reply("Please enter a valid User-ID or @mention!")
                    member = await message.guild.fetch_member(name1)
                    for role in message.guild.roles:
                        if str(role.id) in local_verified_roles:
                            role1 = discord.utils.get(member.guild.roles, id=role.id)
                            break
                        else:
                            role1 = discord.utils.get(member.guild.roles, name='Verified')
                    for role in message.guild.roles:
                        if str(role.id) in local_not_verified_roles:
                            role2 = discord.utils.get(member.guild.roles, id=role.id)
                            break
                        else:
                            role2 = discord.utils.get(member.guild.roles, name='Not verified')
                    await member.remove_roles(role1)
                    await asyncio.sleep(1)
                    await member.add_roles(role2)
                    embed = discord.Embed(title=f'{member} unverified successfully!', description='', color=3566847)
                    
                    try:
                        await message.reply(embed=embed)
                    except:
                        await message.reply(f"{member} unverified successfully!")
                except:
                    embed = discord.Embed(title='This user can\'t get unverified!', description='', color=16711680)
                    
                    try:
                        await message.reply(embed=embed)
                    except:
                        await message.reply("This user can\'t get unverified!")
                return
            if len(erwähnungen) > 1:
                embed = discord.Embed(title="Please only mention one user!", color=3566847)
                
                try:
                    await message.reply(embed=embed)
                except:
                     message.reply("Please only mention one user!")
                return
            for name in erwähnungen:
                mbr = name
            if True:
                try:
                    role1 = discord.utils.get(message.guild.roles, name="Verified")
                    await mbr.remove_roles(role1)
                    await asyncio.sleep(1)
                    role2 = discord.utils.get(message.guild.roles, name="Not verified")
                    await mbr.add_roles(role2)
                    embed = discord.Embed(title=f'{mbr} unverified successfully!', description='', color=3566847)
                    
                    try:
                        await message.reply(embed=embed)
                    except:
                        await message.reply(f"{mbr} unverified successfully!")
                except:
                    embed = discord.Embed(title='This user can\'t get unverified!', description='', color=16711680)
                    
                    try:
                        await message.reply(embed=embed)
                    except:
                        await message.reply("This user can\'t get unverified!")
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
    
    if message.content.startswith(f'{prefix}check-verify-channel'):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_\nThis message will be automatically deleted in 10 seconds.")
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        user = message.author
        if str("('administrator', True)") in perm or message.author.id in sp:
            if str(message.channel.id) in local_verification:
                embed = discord.Embed(title='This is a verify-channel!', description='This message will be automatically deleted in 5 seconds.', color=3566847)
                
                try:
                    sucmsg = await message.reply(embed=embed)
                except:
                    sucmsg = await message.reply("This is a verify-channel!\nThis message will be automatically deleted in 5 seconds.")
                await asyncio.sleep(5)
                try:
                    await sucmsg.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
            else:
                embed = discord.Embed(title="This channel isn't a verify-channel!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
                
                try:
                    failmsg = await message.reply(embed=embed)
                except:
                    failmsg = await message.reply("This channel isn't a verify-channel!\nThis message will be automatically deleted in 5 seconds.")
                await asyncio.sleep(5)
                try:
                    await failmsg.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
    if message.content == f'{prefix}check-verification':
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_\nThis message will be automatically deleted in 10 seconds.")
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        perm = []
        botperm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        for i in message.channel.guild.me.guild_permissions:
            botperm.append(str(i))
        user = message.author
        if str("('administrator', True)") in perm or message.author.id in sp:
            guild = message.guild
            await message.channel.trigger_typing()
            try:
                for i in guild.channels:
                    if str(i.id) in local_verification:
                        vchannel = int(i.id)
                        vchannel = client.get_channel(int(vchannel))
            except:
                pass
            channelperm = []
            try:
                for i in vchannel.permissions_for(message.channel.guild.me):
                    channelperm.append(str(i))
            except:
                pass
            if str("('manage_messages', True)") in botperm or str("('manage_messages', True)") in channelperm:
                manage_confirm = True
                manage_confirmx = True
            else:
                manage_confirm = False
                manage_confirmx = ('**' + str(False)) + '**'
            if str(guild.id) in local_verification:
                guild_confirm = True
                guild_confirmx = True
            else:
                guild_confirm = False
                guild_confirmx = ('**' + str(False)) + '**'
            roles = []
            for i in guild.roles:
                roles.append(i.name)
            for i in guild.roles:
                if str(i.id) in local_verified_roles:
                    verified_confirm = True
                    verified_confirmx = True
                    try:
                        role2 = discord.utils.get(message.guild.roles, id=i.id)
                    except:
                        pass
                    break
                elif 'Verified' in roles:
                    role2 = discord.utils.get(message.guild.roles, name='Verified')
                    verified_confirm = True
                    verified_confirmx = True
                    break
                else:
                    verified_confirm = False
                    verified_confirmx = '**' + str(False) + '**'
                    role2 = None
            for i in guild.roles:
                if str(i.id) in local_not_verified_roles:
                    not_verified_confirm = True
                    not_verified_confirmx = True
                    try:
                        role1 = discord.utils.get(message.guild.roles, id=i.id)
                    except:
                        pass
                    break
                elif 'Not verified' in roles:
                    role1 = discord.utils.get(message.guild.roles, name='Not verified')
                    not_verified_confirm = True
                    not_verified_confirmx = True
                    break
                else:
                    not_verified_confirm = False
                    not_verified_confirmx = '**' + str(False) + '**'
                    role1 = None
            print(role1)
            print(role2)
            channels = []
            channel_confirm = ''
            for i in guild.channels:
                if str(i.id) in local_verification:
                    channel_confirm = str(i.id)
                    channel_confirmx = str(i.id)
            if channel_confirm == '':
                channel_confirm = None
                channel_confirmx = ('**' + str(None)) + '**'
            await message.channel.trigger_typing()
            fail_channels = []
            channelrollen = []
            channelrollenid = []
            for i in guild.channels:
                channelrollen = []
                for role in i.changed_roles:
                    channelrollen.append(role.name)
                for role in i.changed_roles:
                    channelrollenid.append(str(role.id))
                if not 'Verified' in channelrollen:
                    if not i.name in fail_channels:
                        fail_channels.append(i.name)
                if not 'Not verified' in channelrollen:
                    if not i.name in fail_channels:
                        fail_channels.append(i.name)
            if fail_channels == []:
                fail_channels = None
            await message.channel.trigger_typing()
            try:
                await message.channel.guild.me.add_roles(role1)
                await asyncio.sleep(2)
                await message.channel.guild.me.remove_roles(role1)
                not_verified_high = True
                not_verified_highx = True
            except:
                not_verified_high = False
                not_verified_highx = ('**' + str(False)) + '**'
            await message.channel.trigger_typing()
            try:
                await message.channel.guild.me.add_roles(role2)
                await asyncio.sleep(2)
                await message.channel.guild.me.remove_roles(role2)
                verified_high = True
                verified_highx = True
            except Exception as e:
                print(e)
                verified_high = False
                verified_highx = ('**' + str(False)) + '**'
            try:
                member_roles_conf = []
                member_roles_conf2 = []
                for member in guild.members:
                    if not member.bot:
                        member_roles = []
                        for role in member.roles:
                            if role.name == 'Not verified':
                                member_roles.append(role.name)
                            if role.name == 'Verified':
                                member_roles.append(role.name)
                        if not 'Not verified' in member_roles and not 'Verified' in member_roles:
                            member_roles_conf.append(((member.name + ' (') + str(member.id)) + ')')
                            member_roles_conf2.append(((member.name + ' (') + str(member.id)) + ')')
                if member_roles_conf == []:
                    member_roles_conf = None
                    member_roles_conf2 = None
            except:
                embed = discord.Embed(title='An unknown error has occurred. Please contact us with the Error Code 8 via the bot as DM and we will help you.', description='This message will be automatically deleted in 10 seconds.', color=16711680)
                
                try:
                    failmsg = await message.reply(embed=embed)
                except:
                    failmsg = await message.reply("An unknown error has occurred. Please contact us with the Error Code 8 via the bot as DM and we will help you.\nThis message will be automatically deleted in 10 seconds.")
                await asyncio.sleep(10)
                try:
                    await failmsg.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
                
            if guild_confirm == True and verified_confirm == True and not_verified_confirm == True and not channel_confirm == None and not_verified_high == True and verified_high == True and manage_confirm == True:
                check_status = '**Everything is fine!**'
                check_color = 3566847
            else:
                check_status = '**There are some errors! They are marked bold.**'
                check_color = 16711680
            embed = discord.Embed(title='Verification-Check', description=check_status, color=check_color)
            embed.add_field(name='Server registered?', value=guild_confirmx, inline=False)
            embed.add_field(name='Verify-Channel?', value=channel_confirmx, inline=False)
            embed.add_field(name='Verified-role exist?', value=verified_confirmx, inline=False)
            embed.add_field(name='Verified-role assignable?', value=verified_highx, inline=False)
            embed.add_field(name='Not verified-role exist?', value=not_verified_confirmx, inline=False)
            embed.add_field(name='Not verified-role assignable?', value=not_verified_highx, inline=False)
            embed.add_field(name='Delete messages in verify-channel?', value=manage_confirmx, inline=False)
            if guild_confirm == True and verified_confirm == True and not_verified_confirm == True and not channel_confirm == None and not_verified_high == True and verified_high == True and manage_confirm == True:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/4sGPHCN/ixVTxxT.png')
                except:
                    pass
            else:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/8dQWnzY/cq2w57Y.png')
                except:
                    pass
            
            try:
                sucmsg = await message.reply(embed=embed)
            except:
                sucmsg = await message.reply(f"Verification-Check - {check_status}\nServer registered? - {guild_confirmx}\nVerify-Channel? - {channel_confirmx}\nVerified-role exist? - {verified_confirmx}\nVerified-role assignable? - {verified_highx}\nNot verified-role exist? - {not_verified_confirmx}\nNot verified-role assignable? - {not_verified_highx}\nDelete messages in verify-channel? - {manage_confirmx}")
            await message.channel.trigger_typing()
            await asyncio.sleep(3)
            fail_channels1 = []
            fail_channels2 = []
            fail_channels3 = []
            fail_channels4 = []
            fail_channels5 = []
            fail_channels6 = []
            fail_channels7 = []
            fail_channels8 = []
            fail_channels9 = []
            fail_channels10 = []
            if fail_channels != None:
                channel_status = "**There are some errors in channels!**\n*Not every error channel must be a problem.*"
                channel_color = 16711680
                for i in fail_channels:
                    if len(str(fail_channels1)) < 900:
                        fail_channels1.append(i)
                        continue
                    if len(str(fail_channels2)) < 900:
                        fail_channels2.append(i)
                        continue
                    if len(str(fail_channels3)) < 900:
                        fail_channels3.append(i)
                        continue
                    if len(str(fail_channels4)) < 900:
                        fail_channels4.append(i)
                        continue
                    if len(str(fail_channels5)) < 900:
                        fail_channels5.append(i)
                        continue
                    if len(str(fail_channels6)) < 900:
                        fail_channels6.append(i)
                        continue
                    if len(str(fail_channels7)) < 900:
                        fail_channels7.append(i)
                        continue
                    if len(str(fail_channels8)) < 900:
                        fail_channels8.append(i)
                        continue
                    if len(str(fail_channels9)) < 900:
                        fail_channels9.append(i)
                        continue
                    if len(str(fail_channels10)) < 900:
                        fail_channels10.append(i)
                        continue
                fail_channels1 = f"**{fail_channels1}**"
                fail_channels2 = f"**{fail_channels2}**"
                fail_channels3 = f"**{fail_channels3}**"
                fail_channels4 = f"**{fail_channels4}**"
                fail_channels5 = f"**{fail_channels5}**"
                fail_channels6 = f"**{fail_channels6}**"
                fail_channels7 = f"**{fail_channels7}**"
                fail_channels8 = f"**{fail_channels8}**"
                fail_channels9 = f"**{fail_channels9}**"
                fail_channels10 = f"**{fail_channels10}**"
            else:
                channel_status = '**Everything is fine!**'
                channel_color = 3566847
                fail_channels1 = None
            if not fail_channels2 == "**[]**" and not fail_channels2 == []:
                fail_channels1 = fail_channels1 + " \n\n**__+ MORE__**"
            embed = discord.Embed(title='Verification-Check', description=channel_status, color=channel_color)
            embed.add_field(name='Wrong channel-permissions?', value=fail_channels1, inline=False)
            
            if fail_channels == None:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/4sGPHCN/ixVTxxT.png')
                except:
                    pass
            else:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/8dQWnzY/cq2w57Y.png')
                except:
                    pass
            try:
                sucmsg_chl1 = await message.reply(embed=embed)
            except:
                sucmsg_chl1 = await message.reply(f"Verification-Check - {channel_status}\nWrong channel-permissions? - {fail_channels1}")
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass

    if message.content.startswith(f'{prefix}check-verification '):
        if not int(message.author.id) in ADMINS:
            return
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                await message.reply("Failed to send embed! Please ensure, that I have the **embed_messages** permission and try again!")
                return
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                await message.reply("Failed to send embed! Please ensure, that I have the **embed_messages** permission and try again!")
                return
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        nachricht = message.content.replace(f"{prefix}check-verification ", "")
        try:
            nachricht = int(nachricht)
        except:
            embed = discord.Embed(title='Unknown Server!', description='', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            return
        guild = client.get_guild(nachricht)
        botperm = []
        for i in guild.me.guild_permissions:
            botperm.append(str(i))
        user = message.author
        if True:
            await message.channel.trigger_typing()
            try:
                for i in guild.channels:
                    if str(i.id) in local_verification:
                        vchannel = int(i.id)
                        vchannel = client.get_channel(int(vchannel))
            except:
                pass
            channelperm = []
            try:
                for i in vchannel.permissions_for(guild.me):
                    channelperm.append(str(i))
            except:
                pass
            if str("('manage_messages', True)") in botperm or str("('manage_messages', True)") in channelperm:
                manage_confirm = True
                manage_confirmx = True
            else:
                manage_confirm = False
                manage_confirmx = ('**' + str(False)) + '**'
            if str(guild.id) in local_verification:
                guild_confirm = True
                guild_confirmx = True
            else:
                guild_confirm = False
                guild_confirmx = ('**' + str(False)) + '**'
            roles = []
            for i in guild.roles:
                roles.append(i.name)
            if 'Verified' in roles:
                verified_confirm = True
                verified_confirmx = True
            else:
                verified_confirm = False
                verified_confirmx = ('**' + str(False)) + '**'
            if 'Not verified' in roles:
                not_verified_confirm = True
                not_verified_confirmx = True
            else:
                not_verified_confirm = False
                not_verified_confirmx = ('**' + str(False)) + '**'
            channels = []
            channel_confirm = ''
            for i in guild.channels:
                if str(i.id) in local_verification:
                    channel_confirm = str(i.id)
                    channel_confirmx = str(i.id)
            if channel_confirm == '':
                channel_confirm = None
                channel_confirmx = ('**' + str(None)) + '**'
            await message.channel.trigger_typing()
            role1 = discord.utils.get(guild.roles, name='Not verified')
            role2 = discord.utils.get(guild.roles, name='Verified')
            fail_channels = []
            channelrollen = []
            for i in guild.channels:
                channelrollen = []
                for role in i.changed_roles:
                    channelrollen.append(role.name)
                if not 'Verified' in channelrollen:
                    if not i.name in fail_channels:
                        fail_channels.append(i.name)
                if not 'Not verified' in channelrollen:
                    if not i.name in fail_channels:
                        fail_channels.append(i.name)
            if fail_channels == []:
                fail_channels = None
            await message.channel.trigger_typing()
            try:
                await guild.me.add_roles(role1)
                await asyncio.sleep(2)
                await guild.me.remove_roles(role1)
                not_verified_high = True
                not_verified_highx = True
            except:
                not_verified_high = False
                not_verified_highx = ('**' + str(False)) + '**'
            await message.channel.trigger_typing()
            try:
                await guild.me.add_roles(role2)
                await asyncio.sleep(2)
                await guild.me.remove_roles(role2)
                verified_high = True
                verified_highx = True
            except:
                verified_high = False
                verified_highx = ('**' + str(False)) + '**'
            try:
                member_roles_conf = []
                member_roles_conf2 = []
                for member in guild.members:
                    if not member.bot:
                        member_roles = []
                        for role in member.roles:
                            if role.name == 'Not verified':
                                member_roles.append(role.name)
                            if role.name == 'Verified':
                                member_roles.append(role.name)
                        if not 'Not verified' in member_roles and not 'Verified' in member_roles:
                            member_roles_conf.append(((member.name + ' (') + str(member.id)) + ')')
                            member_roles_conf2.append(((member.name + ' (') + str(member.id)) + ')')
                if member_roles_conf == []:
                    member_roles_conf = None
                    member_roles_conf2 = None
            except:
                embed = discord.Embed(title='An unknown error has occurred. Please contact us with the Error Code 8 via the bot as DM and we will help you.', description='This message will be automatically deleted in 10 seconds.', color=16711680)
                
                try:
                    failmsg = await message.reply(embed=embed)
                except:
                    await message.reply("Failed to send embed! Please ensure, that I have the **embed_messages** permission and try again!")
                    return
                await asyncio.sleep(10)
                try:
                    await failmsg.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
                
            if guild_confirm == True and verified_confirm == True and not_verified_confirm == True and not channel_confirm == None and not_verified_high == True and verified_high == True and manage_confirm == True:
                check_status = '**Everything is fine!**'
                check_color = 3566847
            else:
                check_status = '**There are some errors! They are marked bold.**'
                check_color = 16711680
            embed = discord.Embed(title='Verification-Check', description=check_status, color=check_color)
            embed.add_field(name='Server registered?', value=guild_confirmx, inline=False)
            embed.add_field(name='Verify-Channel?', value=channel_confirmx, inline=False)
            embed.add_field(name='Verified-role exist?', value=verified_confirmx, inline=False)
            embed.add_field(name='Verified-role assignable?', value=verified_highx, inline=False)
            embed.add_field(name='Not verified-role exist?', value=not_verified_confirmx, inline=False)
            embed.add_field(name='Not verified-role assignable?', value=not_verified_highx, inline=False)
            embed.add_field(name='Delete messages in verify-channel?', value=manage_confirmx, inline=False)
            if guild_confirm == True and verified_confirm == True and not_verified_confirm == True and not channel_confirm == None and not_verified_high == True and verified_high == True and manage_confirm == True:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/4sGPHCN/ixVTxxT.png')
                except:
                    pass
            else:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/8dQWnzY/cq2w57Y.png')
                except:
                    pass
            
            try:
                sucmsg = await message.reply(embed=embed)
            except:
                await message.reply("Failed to send embed! Please ensure, that I have the **embed_messages** permission and try again!")
                return
            await message.channel.trigger_typing()
            await asyncio.sleep(3)
            fail_channels1 = []
            fail_channels2 = []
            fail_channels3 = []
            fail_channels4 = []
            fail_channels5 = []
            fail_channels6 = []
            fail_channels7 = []
            fail_channels8 = []
            fail_channels9 = []
            fail_channels10 = []
            if fail_channels != None:
                channel_status = "**There are some errors in channels!**\n*Not every error channel must be a problem.*"
                channel_color = 16711680
                for i in fail_channels:
                    if len(str(fail_channels1)) < 900:
                        fail_channels1.append(i)
                        continue
                    if len(str(fail_channels2)) < 900:
                        fail_channels2.append(i)
                        continue
                    if len(str(fail_channels3)) < 900:
                        fail_channels3.append(i)
                        continue
                    if len(str(fail_channels4)) < 900:
                        fail_channels4.append(i)
                        continue
                    if len(str(fail_channels5)) < 900:
                        fail_channels5.append(i)
                        continue
                    if len(str(fail_channels6)) < 900:
                        fail_channels6.append(i)
                        continue
                    if len(str(fail_channels7)) < 900:
                        fail_channels7.append(i)
                        continue
                    if len(str(fail_channels8)) < 900:
                        fail_channels8.append(i)
                        continue
                    if len(str(fail_channels9)) < 900:
                        fail_channels9.append(i)
                        continue
                    if len(str(fail_channels10)) < 900:
                        fail_channels10.append(i)
                        continue
                fail_channels1 = f"**{fail_channels1}**"
                fail_channels2 = f"**{fail_channels2}**"
                fail_channels3 = f"**{fail_channels3}**"
                fail_channels4 = f"**{fail_channels4}**"
                fail_channels5 = f"**{fail_channels5}**"
                fail_channels6 = f"**{fail_channels6}**"
                fail_channels7 = f"**{fail_channels7}**"
                fail_channels8 = f"**{fail_channels8}**"
                fail_channels9 = f"**{fail_channels9}**"
                fail_channels10 = f"**{fail_channels10}**"
            else:
                channel_status = '**Everything is fine!**'
                channel_color = 3566847
                fail_channels1 = None
            if not fail_channels2 == "**[]**" and not fail_channels2 == []:
                fail_channels1 = fail_channels1 + " \n\n**__+ MORE__**"
            embed = discord.Embed(title='Verification-Check', description=channel_status, color=channel_color)
            embed.add_field(name='Wrong channel-permissions?', value=fail_channels1, inline=False)
            
            if fail_channels == None:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/4sGPHCN/ixVTxxT.png')
                except:
                    pass
            else:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/8dQWnzY/cq2w57Y.png')
                except:
                    pass
            try:
                sucmsg_chl1 = await message.reply(embed=embed)
            except:
                await message.reply("Failed to send embed! Please ensure, that I have the **embed_messages** permission and try again!")
                return
            await message.channel.trigger_typing()
            await asyncio.sleep(3)
            await message.channel.trigger_typing()
            fail_members1 = []
            fail_members2 = []
            fail_members3 = []
            fail_members4 = []
            fail_members5 = []
            fail_members6 = []
            fail_members7 = []
            fail_members8 = []
            fail_members9 = []
            fail_members10 = []
            if member_roles_conf2 != None:
                members_status = "**Some members don't have the (not) verified - role**"
                members_color = 16711680
                for i in member_roles_conf2:
                    if len(str(fail_members1)) < 900:
                        fail_members1.append(i)
                        continue
                    if len(str(fail_members2)) < 900:
                        fail_members2.append(i)
                        continue
                    if len(str(fail_members3)) < 900:
                        fail_members3.append(i)
                        continue
                    if len(str(fail_members4)) < 900:
                        fail_members4.append(i)
                        continue
                    if len(str(fail_members5)) < 900:
                        fail_members5.append(i)
                        continue
                    if len(str(fail_members6)) < 900:
                        fail_members6.append(i)
                        continue
                    if len(str(fail_members7)) < 900:
                        fail_members7.append(i)
                        continue
                    if len(str(fail_members8)) < 900:
                        fail_members8.append(i)
                        continue
                    if len(str(fail_members9)) < 900:
                        fail_members9.append(i)
                        continue
                    if len(str(fail_members10)) < 900:
                        fail_members10.append(i)
                        continue
                fail_members1 = f"**{fail_members1}**"
                fail_members2 = f"**{fail_members2}**"
                fail_members3 = f"**{fail_members3}**"
                fail_members4 = f"**{fail_members4}**"
                fail_members5 = f"**{fail_members5}**"
                fail_members6 = f"**{fail_members6}**"
                fail_members7 = f"**{fail_members7}**"
                fail_members8 = f"**{fail_members8}**"
                fail_members9 = f"**{fail_members9}**"
                fail_members10 = f"**{fail_members10}**"
            else:
                members_status = '**Everything is fine!**'
                members_color = 3566847
                fail_members1 = None
            if not fail_members2 == "**[]**" and not fail_members2 == []:
                fail_members1 = fail_members1 + " \n\n**__+ MORE__**"
            embed = discord.Embed(title='Verification-Check', description=members_status, color=members_color)
            embed.add_field(name='Wrong members-permissions?', value=fail_members1, inline=False)
            
            if member_roles_conf == None:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/4sGPHCN/ixVTxxT.png')
                except:
                    pass
            else:
                try:
                    embed.set_thumbnail(url='https://i.ibb.co/8dQWnzY/cq2w57Y.png')
                except:
                    pass
            try:
                sucmsg_chl1 = await message.reply(embed=embed)
            except:
                await message.reply("Failed to send embed! Please ensure, that I have the **embed_messages** permission and try again!")
                return
            #embed.add_field(name='Missing member roles?', value=member_roles_conf2, inline=False)
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                await message.reply("Failed to send embed! Please ensure, that I have the **embed_messages** permission and try again!")
                return
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass

    if message.content.startswith(f"{prefix}verify-message"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_\nThis message will be automatically deleted in 10 seconds.")
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        user = message.author
        if str("('administrator', True)") in perm or message.author.id in sp:
            nachricht = message.content.replace(f"{prefix}verify-message ", "")
            nachricht = message.content.replace(f"{prefix}verify-message", "")
            if nachricht == "" or nachricht == " ":
                if str(message.guild.id) in local_verify_message:
                    guild = message.guild
                    nachricht = discord.utils.get(db_channel_obj6, content=str(message.guild.id))
                    try:
                        await nachricht.delete()
                        embed = discord.Embed(title='Your custom verify-message got deleted!', description='This message will be automatically deleted in 5 seconds.', color=3566847)
                        
                        try:
                            sucmsg = await message.reply(embed=embed)
                        except:
                            sucmsg = await message.reply('Your custom verify-message got deleted!\nThis message will be automatically deleted in 5 seconds.')
                        await asyncio.sleep(5)
                        try:
                            await sucmsg.delete()
                        except:
                            pass
                        try:
                            await message.delete()
                        except:
                            pass
                        return
                    except:
                        embed = discord.Embed(title="You have to include a verify-message!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
                        
                        try:
                            failmsg = await message.reply(embed=embed)
                        except:
                            failmsg = await message.reply("You have to include a verify-message!\nThis message will be automatically deleted in 5 seconds.")
                        await asyncio.sleep(5)
                        try:
                            await failmsg.delete()
                        except:
                            pass
                        try:
                            await message.delete()
                        except:
                            pass
                        return
                    
            if not "{code}" in nachricht:
                embed = discord.Embed(title='You have to include the code variable \{code\} (with the brackets) into your message!', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                
                try:
                    del1 = await message.reply(embed=embed)
                except:
                    del1 = await message.reply("You have to include the code variable \{code\} (with the brackets) into your message!\nThis message will be automatically deleted in 5 seconds.")
                await asyncio.sleep(5)
                try:
                    await del1.delete()
                except:
                    pass
                return
            channel = client.get_channel(MESSAGE_CHANNEL_ID)
            try:
                if str(message.guild.id) in local_verify_message:
                    guild = message.guild
                nachricht1 = discord.utils.get(db_channel_obj6, content=str(message.guild.id))
                await nachricht1.delete()
            except:
                pass
            n1 = await channel.send(str(message.guild.id))
            n2 = await channel.send(nachricht)
            local_verify_message.insert(0, str(message.guild.id))
            local_verify_message.insert(0, nachricht)
            db_channel_obj6.insert(0, n1)
            db_channel_obj6.insert(0, n2)
            embed = discord.Embed(title=f'Verify-Message set to:\n{nachricht}', color=3566847)
            
            try:
                await message.reply(embed=embed)
            except:
                await message.reply(f'Verify-Message set to:\n{nachricht}')
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
        
    if message.content == f"!vote":
        embed = discord.Embed(title="Vote!", description='Vote for our bot and support us!\nhttps://top.gg/bot/713387523757310042/vote\nhttps://botsfordiscord.com/bot/713387523757310042/vote', color=3566847)
        
        try:
            await message.reply(embed=embed)
        except:
            await message.reply("Vote!\nVote for our bot and support us!\nhttps://top.gg/bot/713387523757310042")

    if message.content == f'{prefix}verify':
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_\nThis message will be automatically deleted in 10 seconds.")
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        global v2
        try:
            await v2[message.guild.id].delete()
        except:
            pass
        if str(message.channel.id) in local_verification:
            code22x = []
            for messagex in db_channel_obj6:
                code22x.append(messagex.content)
            global code
            code[message.guild.id] = str(random.randint(10000, 99999))
            try:
                code23 = code22x.index(str(message.guild.id))
                code2 = code22x[code23-1].format(code=str(code[message.guild.id]))
            except:
                code2 = ((f'Um zu bestätigen, dass du keine Maschine bist, gebe bitte folgendes ein:\n{prefix}verify ' + str(code[message.guild.id])) + f'\n\n-----\n\nTo confirm that you are not a bot, please enter:\n{prefix}verify ') + str(code[message.guild.id])
            embed = discord.Embed(title=code2, description='', color=3566847)
            embed.set_footer(text=f"Code doesn't work? Use {prefix}verify again!")
            try:
                v2[message.guild.id] = await message.reply(embed=embed)
            except:
                v2[message.guild.id] = await message.reply(f"{code2}\n_Code doesn't work? Use {prefix}verify again!_")
            await asyncio.sleep(3)
            try:
                await message.delete()
            except:
                pass
            await asyncio.sleep(60)
            try:
                await v2[message.guild.id].delete()
            except:
                pass
            return
    if message.content.startswith(f'{prefix}verify') and not message.content == f'{prefix}verify' and not message.content.startswith(f"{prefix}verify-message"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        if MAINTENANCE and not message.author.id in ADMINS:
            embed = discord.Embed(title='This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_', description='This message will be automatically deleted in 10 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("This command is currently blocked due to MAINTENANCE work! Please try again later. _(Tip: As soon as my MAINTENANCE status is gone, you can try again)_\nThis message will be automatically deleted in 10 seconds.")
            await asyncio.sleep(10)
            try:
                await failmsg.delete()
            except:
                pass
            return
        guild = message.guild
        if str(message.channel.id) in local_verification:
            if str(message.content) == (f'{prefix}verify ' + str(code[message.guild.id])):
                embed = discord.Embed(title='Verify successfull!', description='', color=3566847)
                
                try:
                    v1 = await message.reply(embed=embed)
                except:
                    v1 = await message.reply("Verify successfull!")
                for i in message.guild.roles:
                    for j in local_not_verified_roles:
                        if str(i.id) == j:
                            role1 = i
                            break
                try:
                    role1 = role1
                except:
                    role1 = discord.utils.get(message.guild.roles, name='Not verified')
                try:
                    await message.author.remove_roles(role1)
                except:
                    pass
                await asyncio.sleep(1)
                for i in message.guild.roles:
                    for j in local_verified_roles:
                        if str(i.id) == j:
                            role2 = i
                            break
                try:
                    role2 = role2
                except:
                    role2 = discord.utils.get(message.guild.roles, name='Verified')
                try:
                    await message.author.add_roles(role2)
                except:
                    embed = discord.Embed(title='Error in Verify-Process! Please contact the server administrator for help.', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                    
                    try:
                        failmsg = await message.reply(embed=embed)
                    except:
                        failmsg = await message.reply("Error in Verify-Process! Please contact the server administrator for help.\nThis message will be automatically deleted in 5 seconds.")
                    embed = discord.Embed(title='Error!', description='An error occoured while trying to give the "Verified"-Role. Please ensure, that my role is higher than the "Not verified" and "Verified"-Role!', color=16711680)
                    
                    try:
                        await guild.owner.send(embed=embed)
                    except:
                        pass
                    try:
                        await message.delete()
                    except:
                        pass
                    try:
                        await v1.delete()
                    except:
                        pass
                    try:
                        await v2[message.guild.id].delete()
                    except:
                        pass
                    try:
                        del code[message.guild.id]
                    except Exception as e:
                        print(e)
                    await asyncio.sleep(5)
                    try:
                        await failmsg.delete()
                    except:
                        pass
                    return
                try:
                    await message.delete()
                except:
                    pass
                try:
                    await v1.delete()
                except:
                    pass
                try:
                    await v2[message.guild.id].delete()
                except:
                    pass
                try:
                    del code[message.guild.id]
                except Exception as e:
                    print(e)
                return
            else:
                embed = discord.Embed(title='This Verify-code is wrong! Please try again!', description='', color=16711680)
                
                try:
                    stopx = await message.reply(embed=embed)
                except:
                    stopx = await message.reply("This Verify-code is wrong! Please try again!")
                await asyncio.sleep(5)
                try:
                    await stopx.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
                return
    try:
        code[message.guild.id] = code[message.guild.id]
    except:
        code[message.guild.id] = "oaipfapjhfieaphedfphesafpsehpiuhu"
    if str(message.content) == str(code[message.guild.id]):
        guild = message.guild
        if str(message.channel.id) in local_verification:
            if str(message.content) == str(code[message.guild.id]):
                embed = discord.Embed(title='Verify successfull!', description='', color=3566847)
                
                try:
                    v1 = await message.reply(embed=embed)
                except:
                    v1 = await message.reply("Verify successfull!")
                for i in message.guild.roles:
                    for j in local_not_verified_roles:
                        if str(i.id) == j:
                            role1 = i
                            break
                try:
                    role1 = role1
                except:
                    role1 = discord.utils.get(message.guild.roles, name='Not verified')
                try:
                    await message.author.remove_roles(role1)
                except:
                    pass
                await asyncio.sleep(1)
                for i in message.guild.roles:
                    for j in local_verified_roles:
                        if str(i.id) == j:
                            role2 = i
                            break
                try:
                    role2 = role2
                except:
                    role2 = discord.utils.get(message.guild.roles, name='Verified')
                try:
                    await message.author.add_roles(role2)
                except:
                    embed = discord.Embed(title='Error in Verify-Process! Please contact the server administrator for help.', description='This message will be automatically deleted in 5 seconds.', color=16711680)
                    
                    try:
                        failmsg = await message.reply(embed=embed)
                    except:
                        failmsg = await message.reply("Error in Verify-Process! Please contact the server administrator for help.\nThis message will be automatically deleted in 5 seconds.")
                    embed = discord.Embed(title='Error!', description='An error occoured while trying to give the "Verified"-Role. Please ensure, that my role is higher than the "Not verified" and "Verified"-Role!', color=16711680)
                    
                    try:
                        await guild.owner.send(embed=embed)
                    except:
                        pass
                    try:
                        await message.delete()
                    except:
                        pass
                    try:
                        await v1.delete()
                    except:
                        pass
                    try:
                        await v2[message.guild.id].delete()
                    except:
                        pass
                    try:
                        del code[message.guild.id]
                    except Exception as e:
                        print(e)
                    await asyncio.sleep(5)
                    try:
                        await failmsg.delete()
                    except:
                        pass
                    return
                try:
                    await message.delete()
                except:
                    pass
                try:
                    await v1.delete()
                except:
                    pass
                try:
                    await v2[message.guild.id].delete()
                except:
                    pass
                try:
                    del code[message.guild.id]
                except Exception as e:
                    print(e)
                return
            else:
                embed = discord.Embed(title='This Verify-code is wrong! Please try again!', description='', color=16711680)
                
                try:
                    stopx = await message.reply(embed=embed)
                except:
                    stopx = await message.reply("This Verify-code is wrong! Please try again!")
                await asyncio.sleep(5)
                try:
                    await stopx.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
                return

    try:
        if not str(message.content) == str(code[message.guild.id]):
            int(message.content)
            guild = message.guild
            if str(message.channel.id) in local_verification:
                embed = discord.Embed(title='This Verify-code is wrong! Please try again!', description='', color=16711680)
                
                try:
                    stopx = await message.reply(embed=embed)
                except:
                    stopx = await message.reply("This Verify-code is wrong! Please try again!")
                await asyncio.sleep(5)
                try:
                    await stopx.delete()
                except:
                    pass
                try:
                    await message.delete()
                except:
                    pass
                return
    except:
        pass
    
    if not message.content.startswith(f'{prefix}verify') and not message.content == f'{prefix}verify':
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        user = message.author
        if not str("('administrator', True)") in perm:
            if str(message.channel.id) in local_verification:
                try:
                    await message.delete()
                except:
                    pass

    if message.content.startswith(f'{prefix}mverify') and not message.content == f"{prefix}mverify-all":
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("Failed to send embed! Please ensure, that I have the **embed_messages** permission and try again!")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
            return
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        if str("('administrator', True)") in perm or message.author.id in sp:
            erwähnungen = message.mentions
            if erwähnungen == []:
                try:
                    name1 = message.content
                    name1 = name1.replace(f'{prefix}mverify ', '')
                    try:
                        name1 = int(name1)
                    except:
                        embed = discord.Embed(title=f'Please enter a valid User-ID or @mention!', description='', color=16711680)
                        try:
                            await message.reply(embed=embed)
                        except:
                            await message.reply("Please enter a valid User-ID or @mention!")
                    member = await message.guild.fetch_member(name1)
                    for role in message.guild.roles:
                        if str(role.id) in local_verified_roles:
                            role1 = discord.utils.get(member.guild.roles, id=role.id)
                            break
                        else:
                            role1 = discord.utils.get(member.guild.roles, name='Verified')
                    for role in message.guild.roles:
                        if str(role.id) in local_not_verified_roles:
                            role2 = discord.utils.get(member.guild.roles, id=role.id)
                            break
                        else:
                            role2 = discord.utils.get(member.guild.roles, name='Not verified')
                    await member.remove_roles(role2)
                    await asyncio.sleep(1)
                    await member.add_roles(role1)
                    embed = discord.Embed(title=f'{member} verified successfully!', description='', color=3566847)
                    
                    try:
                        await message.reply(embed=embed)
                    except:
                        await message.reply(f'{mbr} verified successfully!')
                except:
                    embed = discord.Embed(title='This user can\'t get verified!', description='', color=16711680)
                    
                    try:
                        await message.reply(embed=embed)
                    except:
                        await message.reply("This user can\'t get verified!")
                return
            if len(erwähnungen) > 1:
                embed = discord.Embed(title="Please only mention one user!", color=16711680)
                
                try:
                    await message.reply(embed=embed)
                except:
                    await message.reply("Please only mention one user!")
                return
            for name in erwähnungen:
                mbr = name
            try:
                role1 = discord.utils.get(message.guild.roles, name="Not verified")
                await mbr.remove_roles(role1)
                await asyncio.sleep(1)
                role2 = discord.utils.get(message.guild.roles, name="Verified")
                await mbr.add_roles(role2)
                embed = discord.Embed(title=f'{mbr} verified successfully!', description='', color=3566847)
                
                try:
                    await message.reply(embed=embed)
                except:
                    await message.reply(f'{mbr} verified successfully!')
            except:
                embed = discord.Embed(title='This user can\'t get verified!', description='', color=16711680)
                
                try:
                    await message.reply(embed=embed)
                except:
                    await message.reply("This user can\'t get verified!")
            
        else:
            embed = discord.Embed(title="You don't have permission for this command!", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            try:
                failmsg = await message.reply(embed=embed)
            except:
                failmsg = await message.reply("You don't have permission for this command!\nThis message will be automatically deleted in 5 seconds.")
            await asyncio.sleep(5)
            try:
                await failmsg.delete()
            except:
                pass
            try:
                await message.delete()
            except:
                pass
    
    if message.content.startswith(f'{prefix}servers'):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        if int(message.author.id) in ADMINS:
            guilds1 = []
            guilds2 = []
            guilds3 = []
            guilds4 = []
            guilds5 = []
            guilds6 = []
            guilds7 = []
            guilds8 = []
            guilds9 = []
            guilds10 = []
            for i in client.guilds:
                i = ((str(i) + ' (') + str(i.id)) + ') '
                if len(str(guilds1)) < 1500:
                    guilds1.append(i)
                elif len(str(guilds2)) < 1500:
                    guilds2.append(i)
                elif len(str(guilds3)) < 1500:
                    guilds3.append(i)
                elif len(str(guilds4)) < 1500:
                    guilds4.append(i)
                elif len(str(guilds5)) < 1500:
                    guilds5.append(i)
                elif len(str(guilds6)) < 1500:
                    guilds6.append(i)
                elif len(str(guilds7)) < 1500:
                    guilds7.append(i)
                elif len(str(guilds8)) < 1500:
                    guilds8.append(i)
                elif len(str(guilds9)) < 1500:
                    guilds9.append(i)
                elif len(str(guilds10)) < 1500:
                    guilds10.append(i)
            guilds1 = str(guilds1)
            guilds1 = guilds1.replace('[', '')
            guilds1 = guilds1.replace(']', '')
            guilds2 = str(guilds2)
            guilds2 = guilds2.replace('[', '')
            guilds2 = guilds2.replace(']', '')
            guilds3 = str(guilds3)
            guilds3 = guilds3.replace('[', '')
            guilds3 = guilds3.replace(']', '')
            guilds4 = str(guilds4)
            guilds4 = guilds4.replace('[', '')
            guilds4 = guilds4.replace(']', '')
            guilds5 = str(guilds5)
            guilds5 = guilds5.replace('[', '')
            guilds5 = guilds5.replace(']', '')
            guilds6 = str(guilds6)
            guilds6 = guilds6.replace('[', '')
            guilds6 = guilds6.replace(']', '')
            guilds7 = str(guilds7)
            guilds7 = guilds7.replace('[', '')
            guilds7 = guilds7.replace(']', '')
            guilds8 = str(guilds8)
            guilds8 = guilds8.replace('[', '')
            guilds8 = guilds8.replace(']', '')
            guilds9 = str(guilds9)
            guilds9 = guilds9.replace('[', '')
            guilds9 = guilds9.replace(']', '')
            guilds10 = str(guilds10)
            guilds10 = guilds10.replace('[', '')
            guilds10 = guilds10.replace(']', '')
            if len(guilds1) > 0:
                await message.reply(guilds1)
            if len(guilds2) > 0:
                await message.reply(guilds2)
            if len(guilds3) > 0:
                await message.reply(guilds3)
            if len(guilds4) > 0:
                await message.reply(guilds4)
            if len(guilds5) > 0:
                await message.reply(guilds5)
            if len(guilds6) > 0:
                await message.reply(guilds6)
            if len(guilds7) > 0:
                await message.reply(guilds7)
            if len(guilds8) > 0:
                await message.reply(guilds8)
            if len(guilds9) > 0:
                await message.reply(guilds9)
            if len(guilds10) > 0:
                await message.reply(guilds10)
    if message.content.startswith(f'{prefix}serverinfo'):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        if int(message.author.id) in ADMINS:
            if message.content == f'{prefix}serverinfo':
                guild = message.guild
            else:
                name1 = message.content
                name1 = name1.replace(f'{prefix}serverinfo ', '')
                try:
                    guild = client.get_guild(int(name1))
                    server_owner = await client.fetch_user(guild.owner_id)
                except:
                    embed = discord.Embed(title='Dieser Server wurde nicht gefunden!', description='', color=16711680)
                    
                    await message.reply(embed=embed)
                    return
            await message.channel.trigger_typing()
            await asyncio.sleep(0.05)
            members = []
            bots = []
            for member in guild.members:
                if member.bot:
                    bots.append(member)
                else:
                    members.append(member)
            embed = discord.Embed(title=guild.name, description='', color=3566847)
            embed.add_field(name='ID:', value=str(guild.id), inline=False)
            valval = ''
            for i in guild.emojis:
                valval = (valval + i.name) + ', '
            if (not (valval == '')):
                embed.add_field(name='Emojis:', value=valval, inline=False)
            else:
                embed.add_field(name='Emojis:', value='---', inline=False)
            embed.add_field(name='AFK-Timeout:', value=str(guild.afk_timeout), inline=False)
            embed.add_field(name='AFK_Channel:', value=str(guild.afk_channel), inline=False)
            embed.add_field(name='Besitzer:', value=f"{str(server_owner)}", inline=False)
            embed.add_field(name='Anzahl Mitglieder:', value=len(members), inline=False)
            embed.add_field(name='Anzahl Bots:', value=len(bots), inline=False)
            embed.add_field(name='2FA:', value=str(guild.mfa_level), inline=False)
            valval = ''
            for i in guild.features:
                valval = (valval + i) + ', '
            if (not (valval == '')):
                embed.add_field(name='Features:', value=valval, inline=False)
            else:
                embed.add_field(name='Features:', value='---', inline=False)
            embed.add_field(name='Splash:', value=str(guild.splash), inline=False)
            embed.add_field(name='Erstellt am:', value=str(guild.created_at), inline=False)
            embed.set_thumbnail(url=str(guild.icon.url))
            
            await message.reply(embed=embed)
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            embed = discord.Embed(title='', description='', color=3566847)
            valval = ''
            for i in guild.channels:
                valval = (valval + i.name) + ', '
            embed.add_field(name='Kanäle:', value=valval, inline=False)
            
            await message.reply(embed=embed)
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            embed = discord.Embed(title='', description='', color=3566847)
            valval = ''
            for i in guild.roles:
                valval = (valval + i.name) + ', '
            embed.add_field(name='Ränge:', value=valval, inline=False)
            
            await message.reply(embed=embed)
            await message.channel.trigger_typing()
            await asyncio.sleep(2)
            valval = ''
            for i in guild.members:
                try:
                    valval = (valval + i.name) + ', '
                except:
                    pass
                if len(valval) > 1000:
                    embed = discord.Embed(title='', description='', color=3566847)
                    embed.add_field(name='Mitglieder:', value=valval, inline=False)
                    
                    await message.reply(embed=embed)
                    valval = ''
            embed = discord.Embed(title='', description='', color=3566847)
            embed.add_field(name='Mitglieder:', value=valval, inline=False)
            
            await message.reply(embed=embed)

    if message.guild.id == 714819340788301934:
        if message.content.startswith(f"{prefix}admin"):
            member_roles = []
            for i in message.author.roles:
                member_roles.append(i.name)
            if "Admin" in member_roles:
                role1 = discord.utils.get(message.guild.roles, name='Admin')
                await message.author.remove_roles(role1)
                embed = discord.Embed(title='You are no longer an Admin!', description='This message will be automatically deleted in 5 seconds!', color=3566847)
                
                del1 = await message.reply(embed=embed)
                await asyncio.sleep(5)
                await del1.delete()
                try:
                    await message.delete()
                except:
                    pass
            else:
                role1 = discord.utils.get(message.guild.roles, name='Admin')
                await message.author.add_roles(role1)
                embed = discord.Embed(title='You are now an Admin!', description='This message will be automatically deleted in 5 seconds!', color=3566847)
                
                del1 = await message.reply(embed=embed)
                await asyncio.sleep(5)
                await del1.delete()
                try:
                    await message.delete()
                except:
                    pass

    if message.content.startswith(f"!support") and message.channel.id == 741326700733923408 and not message.content.startswith(f"!supportde"):
        general_channel = client.get_channel(741326677245820938)
        bot_self = client.get_user(713387523757310042)
        if int(message.author.id) in ADMINS:
            msg = ""
            for mention in message.mentions:
                msg = msg + mention.mention
            embed = discord.Embed(title='Support', description=f'This channel is for support of {bot_self.mention}. Please use {general_channel.mention} for discussions!', color=3566847)
            
            del1 = await message.channel.send(msg, embed=embed)

    if message.content.startswith(f"!supportde") and message.channel.id == 741326700733923408:
        general_channel = client.get_channel(741326677245820938)
        bot_self = client.get_user(713387523757310042)
        if int(message.author.id) in ADMINS:
            msg = ""
            for mention in message.mentions:
                msg = msg + mention.mention
            embed = discord.Embed(title='Support', description=f'Dieser Kanal ist für Support für {bot_self.mention}. Bitte nutze {general_channel.mention} für Diskussionen!', color=3566847)
            
            del1 = await message.channel.send(msg, embed=embed)

    if message.content.startswith(f"!atmods") and message.channel.id == 741326700733923408 and not message.content.startswith(f"!atmodsde"):
        general_channel = client.get_channel(741326677245820938)
        bot_self = client.get_user(713387523757310042)
        if int(message.author.id) in ADMINS:
            msg = ""
            for mention in message.mentions:
                msg = msg + mention.mention
            embed = discord.Embed(title='@Moderator-mention', description=f'Please do not mention (ping) the Moderator-role for help, unless there is an emergency.\n\nHere are some examples of emergencies:\n- Raids / Multiple members mass spamming.\n- Severe disruption of Discord\'s ToS (NSFW content, etc)', color=3566847)
            
            del1 = await message.channel.send(msg, embed=embed)

    if message.content.startswith(f"!atmodsde") and message.channel.id == 741326700733923408:
        general_channel = client.get_channel(741326677245820938)
        bot_self = client.get_user(713387523757310042)
        if int(message.author.id) in ADMINS:
            msg = ""
            for mention in message.mentions:
                msg = msg + mention.mention
            embed = discord.Embed(title='@Moderator-mention', description=f'Bitte erwähne (pinge) nicht den Moderator-Rang, wenn es kein Notfall ist.\n\nHier sind einige Beispiele für Notfälle:\n- Raids / Mehrere User spammen in Massen.\n- Schwerwiegende Verstöße gegen die Discord-ToS (NSFW Inhalte, etc)', color=3566847)
            
            del1 = await message.channel.send(msg, embed=embed)

    if message.content.startswith(f"!ask2ask") and message.channel.id == 741326700733923408 and not message.content.startswith(f"!ask2askde"):
        if int(message.author.id) in ADMINS:
            msg = ""
            for mention in message.mentions:
                msg = msg + mention.mention
            embed = discord.Embed(title='Ask2Ask', description=f"Please don't ask to ask, just ask! You don't have to say: \"I need help!\" or \"Someone there?\". Just say, what you want to say and we will help you!\nPlease read https://dontasktoask.com/ for an explanation on why this is an issue.", color=3566847)
            
            del1 = await message.channel.send(msg, embed=embed)

    if message.content.startswith(f"!ask2askde") and message.channel.id == 741326700733923408:
        if int(message.author.id) in ADMINS:
            msg = ""
            for mention in message.mentions:
                msg = msg + mention.mention
            embed = discord.Embed(title='Ask2Ask', description=f"Bitte frage nicht, ob du was fragen darfst, frag einfach! Du musst nicht sagen: \"Ich brauche Hilfe!\" oder \"Jemand da?\". Sag einfach, was du sagen willst und du bekommst Hilfe!\nBitte lese https://dontasktoask.com/ für eine Erklärung, warum das ein Fehler ist.", color=3566847)
            
            del1 = await message.channel.send(msg, embed=embed)

    if message.content.startswith(f"{prefix}getowners"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.channel.send(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        if int(message.author.id) in ADMINS:
            owners = []
            for server in client.guilds:
                owners.append(f"{server.name} ({server.id}): {server.owner_id}")
            await message.channel.send(str(owners))

    if message.content.startswith(f"{prefix}v-ban"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        if int(message.author.id) in ADMINS:
            if True:
                name = message.content
                name = name.replace(f'{prefix}v-ban ', '')
                name4 = name.replace('a', '')
                name4 = name4.replace('b', '')
                name4 = name4.replace('c', '')
                name4 = name4.replace('d', '')
                name4 = name4.replace('e', '')
                name4 = name4.replace('f', '')
                name4 = name4.replace('g', '')
                name4 = name4.replace('h', '')
                name4 = name4.replace('i', '')
                name4 = name4.replace('j', '')
                name4 = name4.replace('k', '')
                name4 = name4.replace('l', '')
                name4 = name4.replace('m', '')
                name4 = name4.replace('n', '')
                name4 = name4.replace('o', '')
                name4 = name4.replace('p', '')
                name4 = name4.replace('q', '')
                name4 = name4.replace('r', '')
                name4 = name4.replace('s', '')
                name4 = name4.replace('t', '')
                name4 = name4.replace('u', '')
                name4 = name4.replace('v', '')
                name4 = name4.replace('w', '')
                name4 = name4.replace('x', '')
                name4 = name4.replace('y', '')
                name4 = name4.replace('z', '')
                name4 = name4.replace('ä', '')
                name4 = name4.replace('ö', '')
                name4 = name4.replace('ü', '')
                name4 = name4.replace('A', '')
                name4 = name4.replace('B', '')
                name4 = name4.replace('C', '')
                name4 = name4.replace('D', '')
                name4 = name4.replace('E', '')
                name4 = name4.replace('F', '')
                name4 = name4.replace('G', '')
                name4 = name4.replace('H', '')
                name4 = name4.replace('I', '')
                name4 = name4.replace('J', '')
                name4 = name4.replace('K', '')
                name4 = name4.replace('L', '')
                name4 = name4.replace('M', '')
                name4 = name4.replace('N', '')
                name4 = name4.replace('O', '')
                name4 = name4.replace('P', '')
                name4 = name4.replace('Q', '')
                name4 = name4.replace('R', '')
                name4 = name4.replace('S', '')
                name4 = name4.replace('T', '')
                name4 = name4.replace('U', '')
                name4 = name4.replace('V', '')
                name4 = name4.replace('W', '')
                name4 = name4.replace('X', '')
                name4 = name4.replace('Y', '')
                name4 = name4.replace('Z', '')
                name4 = name4.replace('Ä', '')
                name4 = name4.replace('Ö', '')
                name4 = name4.replace('Ü', '')
                name4 = name4.replace('#', '')
                name4 = name4.replace("'", '')
                name4 = name4.replace('*', '')
                name4 = name4.replace('~', '')
                name4 = name4.replace('-', '')
                name4 = name4.replace('_', '')
                name4 = name4.replace('>', '')
                name4 = name4.replace('<', '')
                name4 = name4.replace('|', '')
                name4 = name4.replace('!', '')
                name4 = name4.replace('"', '')
                name4 = name4.replace('§', '')
                name4 = name4.replace('$', '')
                name4 = name4.replace('%', '')
                name4 = name4.replace('&', '')
                name4 = name4.replace('/', '')
                name4 = name4.replace('(', '')
                name4 = name4.replace(')', '')
                name4 = name4.replace('=', '')
                name4 = name4.replace('?', '')
                name4 = name4.replace('.', '')
                name4 = name4.replace(',', '')
                name4 = name4.replace('´', '')
                name4 = name4.replace('`', '')
                name4 = name4.replace('^', '')
                name4 = name4.replace('°', '')
                name4 = name4.replace('ß', '')
                name4 = name4.replace('{', '')
                name4 = name4.replace('}', '')
                name4 = name4.replace('[', '')
                name4 = name4.replace(']', '')
                name4 = name4.replace('²', '')
                name4 = name4.replace('³', '')
                name4 = name4.replace('+', '')
                try:
                    name4 = int(name4)
                except:
                    await message.reply("Bitte gebe eine gültige ID ein!")
                    return
                name3 = 'xxx'
                name3 = str(name).replace('0', '')
                name3 = str(name3).replace('1', '')
                name3 = str(name3).replace('2', '')
                name3 = str(name3).replace('3', '')
                name3 = str(name3).replace('4', '')
                name3 = str(name3).replace('5', '')
                name3 = str(name3).replace('6', '')
                name3 = str(name3).replace('7', '')
                name3 = str(name3).replace('8', '')
                name3 = str(name3).replace('9', '')
                name3 = name3.lstrip()
            guild = client.get_guild(name4)
            embed = discord.Embed(title='You are banned from this service!', description=f'Reason: {name3}\nIf you think that this is a mistake, please contact us [here](https://discord.gg/4EKzNBN)', color=16711680)
            
            try:
                await client.get_user(guild.owner_id).send(embed=embed)
            except:
                pass
            embed = discord.Embed(title=f'Server {name4} banned!', description='This message will be automatically deleted in 5 seconds!', color=3566847)
            
            n1 = await client.get_channel(BANNS_CHANNEL_ID).send(name4)
            banned_server.append(str(name4))
            banned_server_obj.append(n1)
            try:
                await guild.leave()
            except:
                pass
            dell = await message.reply(embed=embed)
            await asyncio.sleep(5)

    if message.content.startswith(f"{prefix}v-unban"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        channel = client.get_channel(BANNS_CHANNEL_ID)
        nachricht = message.content.replace(f"{prefix}v-unban ", "")
        db_channel_obj8 = []
        if int(message.author.id) in ADMINS:
            nachrichtx = discord.utils.get(banned_server_obj, content=nachricht)
            await nachrichtx.delete()
            embed = discord.Embed(title=f'Server {nachricht} unbanned!', description='This message will be automatically deleted in 5 seconds!', color=3566847)
            
            await message.reply(embed=embed)
            banned_server.remove(nachricht)
            banned_server_obj.remove(nachrichtx)
            await asyncio.sleep(5)

    if message.content.startswith(f"{prefix}owner2server"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        nachricht = message.content.replace(f"{prefix}owner2server ", "")
        if int(message.author.id) in ADMINS:
            guilds = []
            for guild in client.guilds:
                if guild.owner_id == int(nachricht):
                    guilds.append(guild.id)
            await message.reply(str(guilds))

    if message.content.startswith(f"{prefix}member2server"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        nachricht = message.content.replace(f"{prefix}member2server ", "")
        if int(message.author.id) in ADMINS:
            guilds = []
            for guild in client.guilds:
                for member in guild.members:
                    if member.id == int(nachricht):
                        guilds.append(guild.id)
            await message.reply(str(guilds))

    if message.content.startswith(f"{prefix}sp"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        if int(message.author.id) in ADMINS:
            if not message.author.id in sp:
                sp.append(message.author.id)
                embed = discord.Embed(title=f'You now have super-permissions!', description='This message will be automatically deleted in 5 seconds!', color=3566847)
                
                dell = await message.reply(embed=embed)
                await asyncio.sleep(5)
                await dell.delete()
                try:
                    await message.delete()
                except:
                    pass
            else:
                sp.remove(message.author.id)
                embed = discord.Embed(title=f'You no longer have super-permissions!', description='This message will be automatically deleted in 5 seconds!', color=3566847)
                
                dell = await message.reply(embed=embed)
                await asyncio.sleep(5)
                await dell.delete()
                try:
                    await message.delete()
                except:
                    pass
                
    if message.content.startswith(f"{prefix}serverperm"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        nachricht = message.content.replace(f"{prefix}serverperm ", "")
        if int(message.author.id) in ADMINS:
            guild = client.get_guild(int(nachricht))
            permissions = []
            if message.channel.guild.me.guild_permissions.kick_members:
                permissions.append("kick_members")
            if message.channel.guild.me.guild_permissions.ban_members:
                permissions.append("ban_members")
            if message.channel.guild.me.guild_permissions.administrator:
                permissions.append("administrator")
            if message.channel.guild.me.guild_permissions.manage_channels:
                permissions.append("manage_channels")
            if message.channel.guild.me.guild_permissions.manage_guild:
                permissions.append("manage_guild")
            if message.channel.guild.me.guild_permissions.add_reactions:
                permissions.append("add_reactions")
            if message.channel.guild.me.guild_permissions.view_audit_log:
                permissions.append("view_audit_log")
            if message.channel.guild.me.guild_permissions.priority_speaker:
                permissions.append("priority_speaker")
            if message.channel.guild.me.guild_permissions.stream:
                permissions.append("stream")
            if message.channel.guild.me.guild_permissions.read_messages:
                permissions.append("read_messages")
            if message.channel.guild.me.guild_permissions.view_channel:
                permissions.append("view_channel")
            if message.channel.guild.me.guild_permissions.send_messages:
                permissions.append("send_messages")
            if message.channel.guild.me.guild_permissions.send_tts_messages:
                permissions.append("send_tts_messages")
            if message.channel.guild.me.guild_permissions.manage_messages:
                permissions.append("manage_messages")
            if message.channel.guild.me.guild_permissions.embed_links:
                permissions.append("embed_links")
            if message.channel.guild.me.guild_permissions.attach_files:
                permissions.append("attach_files")
            if message.channel.guild.me.guild_permissions.read_message_history:
                permissions.append("read_message_history")
            if message.channel.guild.me.guild_permissions.mention_everyone:
                permissions.append("mention_everyone")
            if message.channel.guild.me.guild_permissions.external_emojis:
                permissions.append("external_emojis")
            if message.channel.guild.me.guild_permissions.use_external_emojis:
                permissions.append("use_external_emojis")
            if message.channel.guild.me.guild_permissions.view_guild_insights:
                permissions.append("view_guild_insights")
            if message.channel.guild.me.guild_permissions.connect:
                permissions.append("connect")
            if message.channel.guild.me.guild_permissions.speak:
                permissions.append("speak")
            if message.channel.guild.me.guild_permissions.mute_members:
                permissions.append("mute_members")
            if message.channel.guild.me.guild_permissions.deafen_members:
                permissions.append("deafen_members")
            if message.channel.guild.me.guild_permissions.move_members:
                permissions.append("move_members")
            if message.channel.guild.me.guild_permissions.use_voice_activation:
                permissions.append("use_voice_activation")
            if message.channel.guild.me.guild_permissions.change_nickname:
                permissions.append("change_nickname")
            if message.channel.guild.me.guild_permissions.manage_nicknames:
                permissions.append("manage_nicknames")
            if message.channel.guild.me.guild_permissions.manage_roles:
                permissions.append("manage_roles")
            if message.channel.guild.me.guild_permissions.manage_permissions:
                permissions.append("manage_permissions")
            if message.channel.guild.me.guild_permissions.manage_webhooks:
                permissions.append("manage_webhooks")
            if message.channel.guild.me.guild_permissions.manage_emojis:
                permissions.append("manage_emojis")
            await message.reply(permissions)

    if message.content.startswith(f"{prefix}clean"):
    #if message.content.startswith("!clean"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        if int(message.author.id) in ADMINS:
            await message.reply("Cleaning up...")
            await message.channel.trigger_typing()
            pos = -1
            for i in db_channel_obj6:
                pos+=1
                try:
                    int(db_channel_obj6[pos+1].content)
                except:
                    try:
                        int(db_channel_obj6[pos].content)
                    except:
                        await asyncio.sleep(3)
                        try:
                            await message.channel.trigger_typing()
                            await db_channel_obj6[pos].delete()
                            db_channel_obj6.remove(db_channel_obj6[pos])
                        except:
                            pass

            pos = -1
            for i in db_channel_obj2:
                pos+=1
                try:
                    int(db_channel_obj2[pos+1].content)
                except:
                    try:
                        int(db_channel_obj2[pos].content)
                    except:
                        await asyncio.sleep(3)
                        try:
                            await message.channel.trigger_typing()
                            await db_channel_obj2[pos].delete()
                            db_channel_obj2.remove(db_channel_obj2[pos])
                        except:
                            pass
            
            for i in local_verification:
                test = client.get_channel(int(i))
                if test == None:
                    test = client.get_guild(int(i))
                    if test == None:
                        await message.channel.trigger_typing()
                        nachricht = discord.utils.get(db_channel_obj, content=str(i))
                        try:
                            local_verification.remove(str(i))
                            db_channel_obj.remove(nachricht)
                            await nachricht.delete()
                        except:
                            pass
                        await asyncio.sleep(3)
            
            for i in local_verification:
                test = client.get_guild(int(i))
                if test == None:
                    test = client.get_channel(int(i))
                    if test == None:
                        await message.channel.trigger_typing()
                        nachricht = discord.utils.get(db_channel_obj, content=str(i))
                        try:
                            print(nachricht.content)
                        except:
                            pass
                        try:
                            local_verification.remove(str(i))
                            db_channel_obj.remove(nachricht)
                            await nachricht.delete()
                        except:
                            pass
                        await asyncio.sleep(3)

            await message.channel.trigger_typing()
            all_roles = []
            for guild in client.guilds:
                for role in guild.roles:
                    all_roles.append(str(role.id))
            await asyncio.sleep(3)
            for i in local_verified_roles:
                if not i in all_roles:
                    await message.channel.trigger_typing()
                    nachricht = discord.utils.get(local_verified_roles_obj, content=str(i))
                    try:
                        print(nachricht.content)
                    except:
                         pass
                    try:
                        local_verified_roles.remove(str(i))
                        local_verified_roles_obj.remove(nachricht)
                        await nachricht.delete()
                    except:
                        pass
                    await asyncio.sleep(3)
            for i in local_not_verified_roles:
                if not i in all_roles:
                    await message.channel.trigger_typing()
                    nachricht = discord.utils.get(local_not_verified_roles_obj, content=str(i))
                    try:
                        print(nachricht.content)
                    except:
                         pass
                    try:
                        local_not_verified_roles.remove(str(i))
                        local_not_verified_roles_obj.remove(nachricht)
                        await nachricht.delete()
                    except:
                        pass
                    await asyncio.sleep(3)
                
            await message.reply("Finished!")
        return

    if message.content.startswith(f"{prefix}svrclear"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        if int(message.author.id) in ADMINS:
            await message.reply("Leaving unused servers...")
            for guild in client.guilds:
                if not str(guild.id) in local_verification:
                    if not int(guild.id) in ALLOWED_SERVERS:
                        await message.channel.trigger_typing()
                        try:
                            await guild.leave()
                            print(f"Left: {guild.id}")
                        except:
                            print(f"Can't leave: {guild.id}")
                        await asyncio.sleep(3)
            await message.reply("Finished!")

    if message.content.startswith(f"{prefix}channelinfo"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        if int(message.author.id) in ADMINS:
            name1 = message.content
            name1 = name1.replace('!channelinfo ', '')
            try:
                name1 = int(name1)
            except:
                await message.reply("Bitte gebe eine gültige ID ein!")
            try:
                usr = client.get_channel(name1)
            except:
                embed = discord.Embed(title='Dieser Channel wurde nicht gefunden!', description='', color=16711680)
                
                await message.reply(embed=embed)
                return
            await message.channel.trigger_typing()
            await asyncio.sleep(0.05)
            embed = discord.Embed(title=usr.name, description='', color=3566847)
            embed.add_field(name='ID:', value=str(usr.id), inline=False)
            embed.add_field(name='Erstellt am:', value=str(usr.created_at), inline=False)
            
            await message.reply(embed=embed)
        else:
            embed = discord.Embed(title='Du hast keine Rechte auf diesen Befehl!', description='', color=16711680)
            
            await message.reply(embed=embed)

    if message.content.startswith(f"{prefix}restart"):
        if int(message.author.id) in ADMINS:
            await message.reply("restarting!")
            await client.close()
            sys.exit()

    if message.content.startswith(f"{prefix}server2channel"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        nachricht = message.content.replace(f"{prefix}server2channel ", "")
        if int(message.author.id) in ADMINS:
            guild = client.get_guild(int(nachricht))
            channels = []
            for channel in guild.channels:
                if str(channel.id) in local_verification:
                    channels.append(channel.id)
            await message.reply(str(channels))

    if message.content.startswith(f"{prefix}db"):
        if not ready:
            embed = discord.Embed(title="The bot is still starting up. Please wait a few minutes and try again! *(Tip: As soon as my Starting... status is gone, you can try again)*", description='This message will be automatically deleted in 5 seconds.', color=16711680)
            
            failmsg = await message.reply(embed=embed)
            await asyncio.sleep(5)
            await failmsg.delete()
            try:
                await message.delete()
            except:
                pass
            return
        if int(message.author.id) in ADMINS:
            if message.content.startswith(f"{prefix}db "):
                if message.content.startswith(f"{prefix}db add "):
                    nachricht = message.content.replace(f"{prefix}db add ", "")
                    msg = await client.get_channel(VERIFY_CHANNEL_ID).send(nachricht)
                    local_verification.append(nachricht)
                    db_channel_obj.append(msg)
                    embed = discord.Embed(title="Database", description='DB edited!', color=3566847)
                    
                    await message.reply(embed=embed)
                elif message.content.startswith(f"{prefix}db remove "):
                    nachricht = message.content.replace(f"{prefix}db remove ", "")
                    nachricht1 = discord.utils.get(db_channel_obj, content=nachricht)
                    try:
                        await nachricht1.delete()
                        local_verification.remove(nachricht)
                        db_channel_obj.remove(nachricht1)
                        embed = discord.Embed(title="Database", description='DB edited!', color=3566847)
                        
                        await message.reply(embed=embed)
                    except:
                        embed = discord.Embed(title="Database", description='DB entry not available!', color=16711680)
                        
                        await message.reply(embed=embed)
                        
                else:
                    embed = discord.Embed(title="Database", description=f'{prefix}db add [value]\n{prefix}db remove [value]', color=3566847)
                    
                    await message.reply(embed=embed)


    if message.content.startswith(f"{prefix}getprefix"):
        nachricht = message.content.replace(f"{prefix}getprefix ", "")
        code29x7 = []
        for messagex in db_channel_obj2:
            code29x7.append(messagex.content)
        try:
            code307 = code29x7.index(str(nachricht))
            prefix7 = code29x7[code307-1]
        except:
            prefix7 = "!"
        await message.reply(prefix7)

    if message.content.startswith(f"{prefix}servercount"):
        await message.reply(f"The bot is currently in {len(client.guilds)} servers!")

    if message.content.startswith(f"{prefix}update"):
        perm = []
        for i in message.author.guild_permissions:
            perm.append(str(i))
        user = message.author
        if str("('administrator', True)") in perm or message.author.id in sp:
            r = discord.utils.get(message.guild.roles, name="Verified")
            if r == None:
                noverify = True
            else:
                noverify = False
                if not str(r.id) in local_verified_roles:
                    r2 = await client.get_channel(VERIFIED_ROLES_CHANNEL_ID).send(r.id)
                    local_verified_roles.append(r2.content)
                    local_verified_roles_obj.append(r2)
            r = discord.utils.get(message.guild.roles, name="Not verified")
            if r == None:
                nonotverify = True
            else:
                nonotverify = False
                if not str(r.id) in local_not_verified_roles:
                    r2 = await client.get_channel(769855532885344306).send(r.id)
                    local_not_verified_roles.append(r2.content)
                    local_not_verified_roles_obj.append(r2)
            if nonotverify and noverify:
                embed = discord.Embed(title="Could not update \"Verified\" and \"Not verified\"-role!", description='Please check the role-names.', color=16711680)
                
                await message.reply(embed=embed)
            elif nonotverify and not noverify:
                embed = discord.Embed(title="Could not update \"Not verified\"-role!", description='Please check the role-names.', color=16711680)
                
                await message.reply(embed=embed)
            elif noverify and not nonotverify:
                embed = discord.Embed(title="Could not update \"Verified\"-role!", description='Please check the role-names.', color=16711680)
                
                await message.reply(embed=embed)
            else:
                embed = discord.Embed(title="Update done sucessfully!", description='', color=3566847)
                
                await message.reply(embed=embed)
    """


@client.event
async def on_error(event, *args, **kwargs):
    embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
    embed.add_field(name='Event', value=event)
    embed.description = '```py\n%s\n```' % traceback.format_exc()
    await client.get_channel(ERROR_CHANNEL).send(embed=embed)


client.loop.create_task(clear())
client.loop.create_task(clearcache())
#client.loop.create_task(autoneustart())
client.run('NzEzMzg3NTIzNzU3MzEwMDQy.XsfX7A.0pNhIQLa-VxNUWRDGtVZRJKcogQ', reconnect=True)
#client.run("NzU1ODA1MTExNjIzNzQ1NTQ3.GrsK5t.GnZgDzyhdi_LpMA8tWcajfH2FMp5FqA3UVztTM", reconnect=True)
