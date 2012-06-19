This is a minimal working example to demostrate Ice-websocket integration:

- Run 'python ice-tornado-server.py' in a terminal
- Open "client.html" in a websocket compliant web browser (ie. chrome)
- Press "Attach" button

  - A new Ice object is created and its proxy is printed at terminal

- Run 'python ./ice-client.py "<printed proxy>"' in other terminal

  - Invocation is sent to browser through the websocket
  - Run it again...

- Note that HelloWebSocket instance is Ice and websocket servant at a time!
