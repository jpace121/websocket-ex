import os
import tornado.ioloop
import tornado.web
from jinja2 import Environment, FileSystemLoader

templateEnv = Environment(loader=FileSystemLoader(searchpath="./templates"))
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }

# template = templateEnv.get_template("main.html")
# output = template.render({"var:"val", "var2":"val2"})

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        template = templateEnv.get_template("index.html")
        self.write(template.render({"name":"James"}))

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ], **settings)
    app.listen(8888)
    print "Hosting at: http://localhost:8888/"
    tornado.ioloop.IOLoop.current().start()
