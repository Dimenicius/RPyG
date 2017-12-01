from PodSixNet.Channel import Channel
from PodSixNet.Server import Server


class ClientChannel(Channel):

    def Network(data):
        print (data)

    def Network_myaction(data):
        print ("myaction:", data)


class MyServer(Server):

    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print ('new connection:', channel)
