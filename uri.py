import tornado.web
import tornado.httpclient
import tornado.httputil
import json


tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

class DnsUpdateHandler(tornado.web.RequestHandler):
    def get(self):
        remote_ip=self.request.remote_ip
        self.write("Hello, world")

class TunnelUpdateHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class ProxyUpdateHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class WebProxyHandler(tornado.web.RequestHandler):
    def get(self):
        protocol=self.get_query_argument('protocol')
        host=self.get_query_argument('host')
        uri=self.get_query_argument('uri')
        URL='%s://%s/%s'%(protocol,host,uri)
        http_client=tornado.httpclient.HTTPClient()
        response = http_client.fetch(URL)
        http_client.close()
        self.set_status(response.code)
        for n,v in response.headers.items():
            self.set_header(n,v)
        self.write(response.body)
    def post(self):
        protocol=self.get_query_argument('protocol')
        host=self.get_query_argument('host')
        uri=self.get_query_argument('uri')
        URL='%s://%s/%s'%(protocol,host,uri)
        http_client=tornado.httpclient.HTTPClient()
        response = http_client.fetch(URL)
        http_client.close()
        self.set_status(response.code)
        for n,v in response.headers.items():
            self.set_header(n,v)
        self.write(response.body)


class ClientInfoHandler(tornado.web.RequestHandler):
    def get(self):
        request=self.request
        info={
            'protocol' : request.protocol,
            'host' : request.host,
            'method' : request.method,
            'uri_path' : request.path,
            'uri_query' : request.query,
            'remote_ip' : request.remote_ip,
            'headers' : request.headers,
            'body' : request.body
        }
        self.write(json.dumps(info,indent=4,sort_keys=True)+'<BR>'+str(request)+'\n')
    def post(self):
        request=self.request
        info={
            'protocol' : request.protocol,
            'host' : request.host,
            'method' : request.method,
            'uri_path' : request.path,
            'uri_query' : request.query,
            'remote_ip' : request.remote_ip,
            'headers' : request.headers,
            'body' : request.body
        }
        self.write(json.dumps(info,indent=4,sort_keys=True)+'<BR>'+str(request)+'\n')
    def put(self):
        request=self.request
        info={
            'protocol' : request.protocol,
            'host' : request.host,
            'method' : request.method,
            'uri_path' : request.path,
            'uri_query' : request.query,
            'remote_ip' : request.remote_ip,
            'headers' : request.headers,
            'body' : request.body
        }
        self.write(json.dumps(info,indent=4,sort_keys=True)+'<BR>'+str(request)+'\n')
    def head(self):
        request=self.request
        info={
            'protocol' : request.protocol,
            'host' : request.host,
            'method' : request.method,
            'uri_path' : request.path,
            'uri_query' : request.query,
            'remote_ip' : request.remote_ip,
            'headers' : request.headers,
            'body' : request.body
        }
        self.write(json.dumps(info,indent=4,sort_keys=True)+'<BR>'+str(request)+'\n')
    def delete(self):
        request=self.request
        info={
            'protocol' : request.protocol,
            'host' : request.host,
            'method' : request.method,
            'uri_path' : request.path,
            'uri_query' : request.query,
            'remote_ip' : request.remote_ip,
            'headers' : request.headers,
            'body' : request.body
        }
        self.write(json.dumps(info,indent=4,sort_keys=True)+'<BR>'+str(request)+'\n')
    def patch(self):
        request=self.request
        info={
            'protocol' : request.protocol,
            'host' : request.host,
            'method' : request.method,
            'uri_path' : request.path,
            'uri_query' : request.query,
            'remote_ip' : request.remote_ip,
            'headers' : request.headers,
            'body' : request.body
        }
        self.write(json.dumps(info,indent=4,sort_keys=True)+'<BR>'+str(request)+'\n')
    def options(self):
        request=self.request
        info={
            'protocol' : request.protocol,
            'host' : request.host,
            'method' : request.method,
            'uri_path' : request.path,
            'uri_query' : request.query,
            'remote_ip' : request.remote_ip,
            'headers' : request.headers,
            'body' : request.body
        }
        self.write(json.dumps(info,indent=4,sort_keys=True)+'<BR>'+str(request)+'\n')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


URI= {
    (r"/dns/update", DnsUpdateHandler),
    (r"/tunnel/update", TunnelUpdateHandler),
    (r"/proxy/update", ProxyUpdateHandler),
    (r"/clientinfo", ClientInfoHandler),
    (r"/webproxy", WebProxyHandler),
    (r"/", MainHandler),
}