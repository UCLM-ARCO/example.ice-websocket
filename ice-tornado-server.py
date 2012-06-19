#!/usr/bin/python
# -*- mode: python; coding: utf-8 -*-

import sys
import Ice
from tornado import ioloop, web, websocket

Ice.loadSlice("sample.ice")
import Example


class HelloWebSocketFactory:
    def __init__(self, adapter, identity):
        self.adapter = adapter
        self.identity = identity

    def __call__(self, *args):
        servant = HelloWebSocket(*args)
        proxy = self.adapter.add(servant, self.identity)
        print proxy
        return servant


class HelloWebSocket(websocket.WebSocketHandler, Example.Hello):
    def say(self, msg, current=None):
        self.write_message(msg)


class Server(Ice.Application):
    def run(self, args):
        ic = self.communicator()
        oid = ic.stringToIdentity("Hello")

        adapter = ic.createObjectAdapterWithEndpoints("Adapter", "tcp -p 9000")
        adapter.activate()

        webapp = web.Application(
            [(r"/hello", HelloWebSocketFactory(adapter, oid))])
        webapp.listen(9999)

        self.shutdownOnInterrupt()
        ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    sys.exit(Server().main(sys.argv))
