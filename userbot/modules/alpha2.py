# alfareza

from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.pe$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("p")
        await e.edit("Hai cantik")
        await e.edit("woi")
        await e.edit("p")
        await e.edit("pe")
        await e.edit("p")
        await e.edit("Astaghfirullah")
        await e.edit("p")
        await e.edit("Dicuekin")
        await e.edit("๐")
        await e.edit("๐ฅบ")
        await e.edit("๐ฐ")
        await e.edit("๐ฉ")
        await e.edit("๐ฑ")
        await e.edit("๐ณ")
        await e.edit("๐ง")
        await e.edit("๐")
        await e.edit("๐ค")
        await e.edit("๐")
        await e.edit("๐")
        await e.edit("๐ค")
        await e.edit("๐")
        await e.edit("๐ก")
        await e.edit("maklum gabut")
        await e.edit("gaada kerjaan")
        await e.edit("dahlah")
        await e.edit("(males lah")
        await e.edit("udah ni udah")
        await e.edit("๐")
        await e.edit("Cuekin Terooooossss")


@register(outgoing=True, pattern='^.hoh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(โ_โ)`"
                     "`\n />โค๏ธ *Ini Buat Kamu`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(โ_โ)`"
                     "`\n/>๐  *eh patah`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(โ_โ)`"
                     "`\n๐<\\  *aku ambil lagi deh`")


@register(outgoing=True, pattern='^.noh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(โโฟโ)`"
                     "`\n />๐น *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(โกโฟโก)`"
                     "`\n๐ฅ<\\  *Gajadi Layu`")

# alfareza


CMD_HELP.update({
    "animasialpha":
    "`.noh` ; `.hoh`\
    \nUsage: cobain.\
    \n\n`.pe`\
    \nUsage: spam gajelas."
})
