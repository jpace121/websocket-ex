These are quick examples on how to do stuff in tornado/jquery/whatever so I can
quickly find them when I get confused.

template = templateEnv.get_template("main.html")
output = template.render({"var:"val", "var2":"val2"})

class GetAPI(tornado.web.RequestHandler):
    def get(self):
        print self.get_arguments("name")
        self.write("Success!")


class API(tornado.web.RequestHandler):
    def post(self):
        jsoned = json.loads(self.request.body)
        print jsoned["name"]
        print jsoned["job"]
        self.write(jsoned)
        
curl -H "Content-Type: application/json" -X POST -d '{"name":"james", "job":"engineer"'} http://localhost:8888/api
