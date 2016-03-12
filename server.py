import os
import json
import tornado.ioloop
import tornado.web
import tornado.websocket
from jinja2 import Environment, FileSystemLoader

# Setting Globals
templateEnv = Environment(loader=FileSystemLoader(searchpath="./templates"))
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

# Websocket Client List
ws_clients = []

def send_to_all(msg):
    """Send a message to all connected clients."""
    for client in ws_clients:
        client.write_message(msg)

# Handlers
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        template = templateEnv.get_template("index.html")
        self.write(template.render({"name":"James"}))

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        ws_clients.append(self)
        print "Open"

    def on_close(self):
        ws_clients.remove(self)
        print "Close"

    def on_message(self, message):
        print message


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/ws", WebSocketHandler),
    ], **settings)
    app.listen(8888)
    print "Hosting at: http://localhost:8888/"
    tornado.ioloop.IOLoop.current().start()
