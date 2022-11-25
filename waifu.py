import os
import time
import aiohttp
import urllib
import requests

from bs4 import BeautifulSoup
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_HASH, APP_ID, CHATS, STRING_SESSION, DELAY

waifu = Client(
    name="userbot",
    session_string=STRING_SESSION,
    api_id=APP_ID,
    api_hash=API_HASH,
)


u_ = """Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"""

headers_ = [("User-agent", u_)]


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""
    async with aiohttp.ClientSession(headers=headers_) as session:
        async with session.get(googleurl) as resp:
            source = await resp.read()
    soup = BeautifulSoup(source, "html.parser")
    results = {"similar_images": "", "best_guess": ""}
    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass
    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()
    return results


def get_data(img):
    searchUrl = "https://www.google.com/searchbyimage/upload"
    file_img = {"encoded_image": (img, open(img, "rb")), "image_content": ""}
    response = requests.post(searchUrl, files=file_img, allow_redirects=False)
    if os.path.exists(img):
        os.remove(img)
    if response.status_code == 400:
        return print("(Waifu Catch Failed) - [Invalid Response]")
    return response.headers["Location"]


@waifu.on_message(
    filters.photo
    & filters.chat(CHATS)
    & filters.user(users=[792028928, 1232515770, 1964681186])
)
async def autoprotecc(_, message: Message):
    path = await waifu.download_media(message, file_name="waifu.jpg")
    print("Now working.")
    time.sleep(1)
    fetchUrl = await get_data(path)
    match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
    guess = match["best_guess"]
    if not guess:
        return print("Failed to protecc this waifu.")
    guess = guess.replace("Results for", "")
    res = await message.reply_text(f"/protecc {guess}")
    print(f"Success protecc {guess}")
    time.sleep(DELAY)
    await res.delete()
    await os.remove(path)


if __name__ == "__main__":
    waifu.run()
