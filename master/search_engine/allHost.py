#!/usr/bin/python
# WebHunter Run


class all_host:
    def __init__(self):
        pass

    def atom(self, host):

        import bingHostClass
        import googleHostClass
        import yahooHostClass
        from core.urli import sansor

        sans = sansor()
        host = sans.pransor(host)

        if sans.cransor(host):

            this = []
            host = str(host).replace('.', '\.')

            a = bingHostClass.bingHostClass(host)
            a.explore()
            hosts1 = a.hosts()

            b = googleHostClass.googleHostClass(host)
            b.explore()
            hosts2 = b.hosts()

            c = yahooHostClass.yahooHostClass(host)
            c.explore()
            hosts3 = c.hosts()

            for hs1 in hosts1:
                if hs1 not in this:
                    this.append(hs1)
                for hs2 in hosts2:
                    if hs2 not in this:
                        this.append(hs2)
                    for hs3 in hosts3:
                        if hs3 not in this:
                            this.append(hs3)

            return this
        else:
            return None

    def run(self):
        import sys

        W = '\x1b[37m'
        R = '\x1b[36m'
        C = '\x1b[32m'
        while True:
            host = raw_input('WH->[all engine host search] Host: ')
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] problem Connection (invalid URL or network) [-]")
                continue

            if wread == []:
                print("\thost not found.\n")
                break

            print('\n' + C)
            for host in wread:
                print('\t' + host)

            print('\n' + W)
            print('\t[Type exit to Exit]')
            print('\t[Type back to back]')
            break
