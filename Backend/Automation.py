from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
import requests
from rich import print
from groq import Groq
import os
import webbrowser
import subprocess
import keyboard
import asyncio


env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

classes = ["zCubwf", "hgKElc", "LTKOO sY7ric", "z0LcW", "gsrt vk_bk FzvWSb YwPhnf", "pclqee", "tw-Data-text tw-text-small tw-ta",
           "IZ6rdc", "O5uR6d LTKOO", "vlzY6d", "webanswers-webanswers_table__webanswers-table", "dDoNo ikb4Bb gsrt", "sXLaOe",
           "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"


client = Groq(api_key=GroqAPIKey)


# Predefined responses for user interactions
professional_responses = [
    "I'm here to assist you with anything you need. Feel free to ask anytime!",
    "Your queries are always welcome, and I'm happy to help you further."
]

# List to store chatbot messages
messages = []

# System message providing context to the chatbot
SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like letter."}]
# Function to perform a Google search
def GoogleSearch(topic):
    search(topic) # Assuming a search function to perform Google search
    return True # Indicate success


# Function to generate content using AI and save it to a file.
def Content(Topic):

    # Nested function to open a file in Notepad.
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe' # Default text editor.
        subprocess.Popen([default_text_editor, File]) # Open the file in Notepad.

    # Nested function to generate content using the AI chatbot.
    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f"{prompt}"}) # Add the user's prompt to messages.

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", # Specify the AI model.
            messages=SystemChatBot + messages, # Include system instructions and chat history.
            max_tokens=2048, # Limit on the number of tokens in the output.
            temperature=0.7, # Adjust the randomness of the output.
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = ""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer})
        return Answer
    
    Topic: str = Topic.replace("Content ", "")
    ContentByAI = ContentWriterAI(Topic)

    with open(rf"Data\{Topic.lower().replace(' ','' )}.txt", "w", encoding="utf-8") as file:
        file.write(ContentByAI)
        file.close()

    OpenNotepad(rf"Data\{Topic.lower().replace(' ','' )}.txt")
    return True


def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"  # Construct the YouTube search URL.
    webbrowser.open(Url4Search)  # Open the search URL in a web browser.
    return True  # Indicate success.

# Function to play a video on YouTube.
def PlayYoutube(query):
    playonyt(query)  # Use pywhatkit's playonyt function to play the video.
    return True  # Indicate success.



APP_WEBSITES = {
    # 🎬 Streaming Services
    "netflix": "https://www.netflix.com",
    "netflix.": "https://www.netflix.com",
    "amazon prime": "https://www.primevideo.com",
    "amazon prime.": "https://www.primevideo.com",
    "hotstar": "https://www.hotstar.com",
    "hotstar.": "https://www.hotstar.com",
    "hulu": "https://www.hulu.com",
    "hulu.": "https://www.hulu.com",
    "disney+": "https://www.disneyplus.com",
    "disney+.": "https://www.disneyplus.com",
    "apple tv": "https://tv.apple.com",
    "hbo max": "https://www.hbomax.com",
    "hbo max.": "https://www.hbomax.com",
    "youtube": "https://www.youtube.com",
    "youtube.": "https://www.youtube.com",

    # 🎵 Music & Audio Streaming
    "spotify": "https://www.spotify.com",
    "spotify.": "https://www.spotify.com",
    "apple music": "https://music.apple.com",
    "apple music.": "https://music.apple.com",
    "soundcloud": "https://soundcloud.com",
    "soundcloud.": "https://soundcloud.com",
    "gaana": "https://gaana.com",
    "gaana.": "https://gaana.com",
    "wynk music": "https://wynk.in/music",
    "wynk music.": "https://wynk.in/music",
    "jiosaavn": "https://www.jiosaavn.com",
    "jiosaavn.": "https://www.jiosaavn.com",

    # 📱 Social Media & Communication
    "facebook": "https://www.facebook.com",
    "facebook.": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "instagram.": "https://www.instagram.com",
    "twitter": "https://twitter.com",
    "twitter.": "https://twitter.com",
    "linkedin": "https://www.linkedin.com",
    "linkedin.": "https://www.linkedin.com",
    "snapchat": "https://www.snapchat.com",
    "snapchat.": "https://www.snapchat.com",
    "reddit": "https://www.reddit.com",
    "reddit.": "https://www.reddit.com",
    "telegram": "https://web.telegram.org",
    "telegram.": "https://web.telegram.org",
    "whatsapp": "https://web.whatsapp.com",
    "whatsapp.": "https://web.whatsapp.com",
    "discord": "https://discord.com",
    "discord.": "https://discord.com",
    "messenger": "https://www.messenger.com",
    "messenger.": "https://www.messenger.com",
    "tiktok": "https://www.tiktok.com",
    "tiktok.": "https://www.tiktok.com",

    # 🔍 Search Engines
    "google": "https://www.google.com",
    "google.": "https://www.google.com",
    "bing": "https://www.bing.com",
    "bing.": "https://www.bing.com",
    "duckduckgo": "https://www.duckduckgo.com",
    "duckduckgo.": "https://www.duckduckgo.com",
    "yahoo": "https://www.yahoo.com",
    "yahoo.": "https://www.yahoo.com",

    # 👨‍💻 Developer & Coding Platforms
    "github": "https://github.com",
    "github.": "https://github.com",
    "gitlab": "https://gitlab.com",
    "gitlab.": "https://gitlab.com",
    "stackoverflow": "https://stackoverflow.com",
    "stackoverflow.": "https://stackoverflow.com",
    "chatgpt": "https://chat.openai.com",
    "chatgpt.": "https://chat.openai.com",
    "huggingface": "https://huggingface.co",
    "huggingface.": "https://huggingface.co",
    "kaggle": "https://www.kaggle.com", 
    "kaggle.": "https://www.kaggle.com",
    "w3schools": "https://www.w3schools.com",
    "w3schools.": "https://www.w3schools.com",
    "leetcode": "https://leetcode.com",
    "leetcode.": "https://leetcode.com",
    "codeforces": "https://codeforces.com",
    "codeforces.": "https://codeforces.com",
    "geeksforgeeks": "https://www.geeksforgeeks.org",
    "geeksforgeeks.": "https://www.geeksforgeeks.org",

    # 💼 Productivity & Work Tools
    "zoom": "https://zoom.us",
    "zoom.": "https://zoom.us",
    "microsoft teams": "https://teams.microsoft.com",
    "microsoft teams.": "https://teams.microsoft.com",
    "slack": "https://slack.com",
    "slack.": "https://slack.com",
    "notion": "https://www.notion.so",
    "notion.": "https://www.notion.so",
    "evernote": "https://www.evernote.com",
    "evernote.": "https://www.evernote.com",
    "google drive": "https://drive.google.com",
    "google drive.": "https://drive.google.com",
    "onedrive": "https://onedrive.live.com",
    "onedrive.": "https://onedrive.live.com",
    "dropbox": "https://www.dropbox.com",
    "dropbox.": "https://www.dropbox.com",
    "canva": "https://www.canva.com",
    "canva.": "https://www.canva.com",
    "figma": "https://www.figma.com",
    "figma.": "https://www.figma.com",
    "trello": "https://trello.com",
    "trello.": "https://trello.com",

    # 📚 Education & Learning
    "coursera": "https://www.coursera.org",
    "coursera.": "https://www.coursera.org",
    "udemy": "https://www.udemy.com",
    "udemy.": "https://www.udemy.com",
    "udemi": "https://www.udemy.com",
    "udemi.": "https://www.udemy.com",
    "edx": "https://www.edx.org",
    "edx.": "https://www.edx.org",
    "khan academy": "https://www.khanacademy.org",
    "khan academy.": "https://www.khanacademy.org",
    "brilliant": "https://www.brilliant.org",
    "brilliant.": "https://www.brilliant.org",
    "chegg": "https://www.chegg.com",
    "chegg.": "https://www.chegg.com",
    "wolfram alpha": "https://www.wolframalpha.com",
    "wolfram alpha.": "https://www.wolframalpha.com",
    "nptel": "https://nptel.ac.in",
    "nptel.": "https://nptel.ac.in",
    "byju's": "https://byjus.com",
    "byju's.": "https://byjus.com",

    # 🛒 Shopping & E-commerce
    "amazon": "https://www.amazon.com",
    "amazon.": "https://www.amazon.com",
    "flipkart": "https://www.flipkart.com",
    "flipkart.": "https://www.flipkart.com",
    "ebay": "https://www.ebay.com",
    "ebay.": "https://www.ebay.com",
    "snapdeal": "https://www.snapdeal.com",
    "snapdeal.": "https://www.snapdeal.com",
    "shopify": "https://www.shopify.com",
    "shopify.": "https://www.shopify.com",
    "myntra": "https://www.myntra.com",
    "ajio": "https://www.ajio.com",

    # 🏦 Banking & Finance
    "paypal": "https://www.paypal.com",
    "paypal.": "https://www.paypal.com",
    "stripe": "https://stripe.com",
    "stripe.": "https://stripe.com",
    "paytm": "https://paytm.com",
    "paytm.": "https://paytm.com",
    "phonepe": "https://www.phonepe.com",
    "phonepe.": "https://www.phonepe.com",
    "google pay": "https://pay.google.com",
    "google pay.": "https://pay.google.com",
    "razorpay": "https://razorpay.com",
    "razorpay.": "https://razorpay.com",
    "upstox": "https://upstox.com",
    "upstox.": "https://upstox.com",
    "zerodha": "https://zerodha.com",
    "zerodha.": "https://zerodha.com",
    "groww": "https://groww.in",
    "groww.": "https://groww.in",

    # 🎮 Gaming & Esports
    "twitch": "https://www.twitch.tv",
    "twitch.": "https://www.twitch.tv",
    "steam": "https://store.steampowered.com",
    "steam.": "https://store.steampowered.com",
    "epic games": "https://www.epicgames.com",
    "epic games.": "https://www.epicgames.com",
    "roblox": "https://www.roblox.com",
    "roblox.": "https://www.roblox.com",
    "fortnite": "https://www.fortnite.com",
    "fortnite.": "https://www.fortnite.com",
    "valorant": "https://playvalorant.com",
    "valorant.": "https://playvalorant.com",
    "pubg": "https://www.pubg.com",
    "pubg.": "https://www.pubg.com",

    # 📊 News & Information
    "bbc": "https://www.bbc.com",
    "bbc.": "https://www.bbc.com",
    "cnn": "https://www.cnn.com",
    "cnn.": "https://www.cnn.com",
    "nytimes": "https://www.nytimes.com",
    "nytimes.": "https://www.nytimes.com",
    "the guardian": "https://www.theguardian.com",
    "the guardian.": "https://www.theguardian.com",
    "hindustan times": "https://www.hindustantimes.com",
    "hindustan times.": "https://www.hindustantimes.com",
    "times of india": "https://timesofindia.indiatimes.com",
    "times of india.": "https://timesofindia.indiatimes.com",

    # 🚀 Miscellaneous
    "speedtest": "https://www.speedtest.net",
    "speedtest.": "https://www.speedtest.net",
    "weather": "https://www.weather.com",
    "weather.": "https://www.weather.com",
    "translate": "https://translate.google.com",
    "translate.": "https://translate.google.com",
    "wikipedia": "https://www.wikipedia.org",
    "wikipedia.": "https://www.wikipedia.org",
    "quora": "https://www.quora.com",
    "quora.": "https://www.quora.com",
    "medium": "https://medium.com",
    "medium.": "https://medium.com",

}




def OpenApp(app, sess=requests.session()):
    app_lower = app.lower()

    # Try opening the installed app
    try:
        print(f"[cyan]Trying to open {app}...[/cyan]")
        appopen(app, match_closest=True, output=True, throw_error=True)
        return True

    except Exception:
        print(f"[red]Failed to open {app}. Checking for official website...[/red]")

        # Check predefined websites
        if app_lower in APP_WEBSITES:
            print(f"[green]Opening official website: {APP_WEBSITES[app_lower]}[/green]")
            webopen(APP_WEBSITES[app_lower])
            return True

        # If not found, fallback to Google search
        def search_google(query):
            url = f"https://www.google.com/search?q={query} official site"
            headers = {"User-Agent": useragent}
            response = sess.get(url, headers=headers)
            return response.text if response.status_code == 200 else None

        def extract_links(html):
            if not html:
                return []
            soup = BeautifulSoup(html, "html.parser")
            first_link = soup.select_one("div.tF2Cxc a")  # Reliable selector
            return [first_link["href"]] if first_link else []

        # Perform Google search
        html = search_google(app)
        links = extract_links(html)

        if links:
            print(f"[green]Opening official website: {links[0]}[/green]")
            webopen(links[0])  # Open first valid link
        else:
            print(f"[red]Could not find an official site for {app}.[/red]")

        return True
    

def CloseApp(app):

    if "chrome" in app:
        pass
    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
            return True
        except:
            return False


def System(command):

    def mute():
        keyboard.press_and_release("volume mute")

    def unmute():
        keyboard.press_and_release("volume mute")

    def volume_up():
        keyboard.press_and_release("volume up")

    def volume_down():
        keyboard.press_and_release("volume down")
    


    if command == "mute":
        mute()
    elif command == "unmute":
        unmute()
    elif command == "volume up":
        volume_up()
    elif command == "volume down":
        volume_down()
    
    return True


async def TranslateAndExecute(commands: list[str]):

    funcs = []

    for command in commands:

        if command.startswith("open "):

            if "open it" in command:
                pass

            if "open file" == command:
                pass

            else:
                fun = asyncio.to_thread(OpenApp, command.removeprefix("open "))
                funcs.append(fun)

        elif command.startswith("general "):
            pass

        elif command.startswith("realtime "):
            pass

        elif command.startswith("close "):
            fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))
            funcs.append(fun)

        elif command.startswith("play "):
            fun = asyncio.to_thread(PlayYoutube, command.removeprefix("play "))
            funcs.append(fun)

        elif command.startswith("content "):
            fun = asyncio.to_thread(Content, command.removeprefix("content "))
            funcs.append(fun)

        elif command.startswith("youtube search "):
            fun = asyncio.to_thread(YouTubeSearch, command.removeprefix("youtube search "))
            funcs.append(fun)

        elif command.startswith("system "):
            fun = asyncio.to_thread(System, command.removeprefix("system "))
            funcs.append(fun)

        elif command.startswith("google search "):
            fun = asyncio.to_thread(GoogleSearch, command.removeprefix("google search "))
            funcs.append(fun)

        else:
            print(f"No Function Found. For {command}")

    
    results = await asyncio.gather(*funcs)

    for result in results:
        if isinstance(result, str):
            yield result
        else:
            yield result
            

async def Automation(commands: list[str]):

    async for result in TranslateAndExecute(commands):
        pass

    return True

# if __name__ == "__main__":
#     asyncio.run(Automation(["open netflix","open spotify", "open zoom", "open whatsapp", "open telegram"]))
