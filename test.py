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
        <h2>Поле для ввода сообщений</h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(JSON.parse(event.data))
                message.appendChild(content)
                messages.appendChild(message)
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
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    i = 1
    while True:
        data = await websocket.receive_text()
        data = json.loads(data)
        await websocket.send_text(json.dumps(f"{i}: {data}"))
        i += 1
