#!/usr/bin/python
# -*- mode: python; coding: utf-8 -*-

import sys
import Ice

Ice.loadSlice("sample.ice")
import Example


class Client(Ice.Application):
    def run(self, args):
        prx = self.communicator().stringToProxy(args[1])
        prx = Example.HelloPrx.checkedCast(prx)
        prx.say("Hello")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: {0} <proxy>".format(sys.argv[0])
        sys.exit(1)

    sys.exit(Client().main(sys.argv))
