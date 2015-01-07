import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen
import os
import signal

class mainhandler(tornado.web.RequestHandler):
    '''
    When a user goes first goes  to /wgsi, the browser sends a GET HTTP
    request to the server which in turn calls the 'get' method. 
    
    When the uses fills out the form and clicks on the 'submit' button.
    The browser will send a POST request to the server and call the 'post'
    method, which will get the arguments passed to the server and render
    a new page based on the submitted data.
    '''
    def get(self):
        self.render('form.html')

    def post(self):
        name = self.get_arguments('name')[0]
        #print name
        self.render('submit.html', name=name)

class urlhandler(tornado.web.RequestHandler):
    '''
    This will take any text after '/name/' and render a template with 
    that string. A regex is used to extract the name.
    '''
    def get(self, name):
        self.render('submit.html', name=name)

routes = [
    (r'/wsgi', mainhandler),
    (r'/name/([0-9A-Za-z ]+)', urlhandler),
]

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
)

application = tornado.web.Application(routes, **settings)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    port_listen = 8800
    http_server.listen(port_listen)
    loop = tornado.ioloop.IOLoop.instance()

    def sigint_handler(signum, frame):
        print('signal handler called with %s, frame %s' % (signum, frame))
        #periodic_cbk.stop()
        loop.stop()
    signal.signal(signal.SIGINT, sigint_handler)
    signal.signal(signal.SIGHUP, sigint_handler)
    signal.signal(signal.SIGTERM, sigint_handler)
    #periodic_cbk = tornado.ioloop.PeriodicCallback(ip_poll, 
    #                                               poll_interval*60*1000,
    #                                               loop)
    #periodic_cbk.start()
    loop.start()
 
# vim: set tabstop=4 shiftwidth=4 softtabstop=4 expandtab:
