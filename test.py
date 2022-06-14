from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import json

app = FastAPI()
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h2>Write</h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form><br>
        <table id="tbody" border="1">
           <tr>
            <th>Number</th>
            <th>Message</th>
            </tr>
        </table>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var row = document.createElement('tr')
                var num = document.createElement('td')
                var mess = document.createElement('td')
                num.appendChild(document.createTextNode(JSON.parse(event.data)['num']))
                mess.appendChild(document.createTextNode(JSON.parse(event.data)['text']))
                row.appendChild(num)
                row.appendChild(mess)
                document.getElementById('tbody').appendChild(row)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(JSON.stringify(input.value))
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
def get_html():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    num_mess = 0
    while True:
        num_mess += 1
        text = await websocket.receive_text()
        data = {
            "num": num_mess,
            "text": json.loads(text)
        }
        await websocket.send_text(json.dumps(data))
