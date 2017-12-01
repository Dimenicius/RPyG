from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep


class ClientChannel(Channel):
    def Network(self, data):
        print (data)

    def Network_addplayer(self, data):
        player_id = data["char"]
        self._server.addplayer(player_id)


class GameServer(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):

        # Call the super constructor
        Server.__init__(self, *args, **kwargs)
        self.playerChannels = []
        self.chars = []

    def Connected(self, channel, addr):
        self.playerChannels.append(channel)
        print ('new connection:', channel)

    def addplayer(self, data):
        self.chars.append(data)

        for channel in self.channels:
            if channel not in self.playerChannels:
                channel.Send({"action": "addplayer", "char": data})

        for index, channel in enumerate(self.playerChannels):
            if index == len(self.playerChannels) - 1:
                for char in self.chars:
                    channel.Send(
                        {"action": "addplayer", "char": char})
            else:
                channel.Send({"action": "addplayer", "char": data})


print ("STARTING SERVER ON LOCALHOST")
gameServe = GameServer()
while True:
    gameServe.Pump()
    sleep(0.01)
