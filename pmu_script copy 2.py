import Pyro4



class Mats(object):
    
    value = 42                  # not exposed

    def __dunder__(self):       # exposed
        pass

    def _private(self):         # not exposed
        pass

    def __private(self):        # not exposed
        pass

    @Pyro4.expose
    def get_value(self):        # exposed
        return self.value

    @Pyro4.expose
    @property
    def attr(self):             # exposed as 'proxy.attr' remote attribute
        return self.value

    @Pyro4.expose
    @attr.setter
    def attr(self, value):      # exposed as 'proxy.attr' writable
        self.value = value



daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
# register the greeting maker as a Pyro object
uri = daemon.register(Mats)
# register the object with a name in the name server
ns.register("CF", uri)

print("Ready.")
# start the event loop of the server to wait for calls
daemon.requestLoop()
