These are quick examples on how to do stuff in tornado/jquery/whatever so I can
quickly find them when I get confused.

class GetAPI(tornado.web.RequestHandler):
    def get(self):
        print self.get_arguments("name")
        self.write("Success!")
