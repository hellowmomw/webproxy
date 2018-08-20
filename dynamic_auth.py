import tornado.ioloop
import tornado.web
import tornado.httpserver

VERSION='0.3'

from uri import URI

Application=tornado.web.Application(URI)

if __name__ == "__main__":
    server=tornado.httpserver.HTTPServer(Application,xheaders=True)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()



