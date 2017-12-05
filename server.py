from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep
import random


class Player():
    def __init__(self, channel, uid):
        self.channel = channel
        self.id = uid
        self.isPlayer = False


class Enemy():
    def __init__(self, masterchannel, uid):
        self.channel = masterchannel
        self.id = uid


class ClientChannel(Channel):
    def Network(self, data):
        print (data)

    def Network_addplayer(self, data):
        player_id = data["char"]
        self._server.addplayer(player_id)

    def Network_passTurn(self, data):
        self._server.passTurn()

    def Network_addenemy(self, data):
        enemy_id = data["enemy"]
        self._server.addenemy(enemy_id)

    def Network_checkturn(self, data):
        current_turn = data["turn"]
        self._server.sendTurn(current_turn)

    def Network_turnOrder(self, data):
        turn_order = data["turn_order"]
        self._server.sendTurnOrder(turn_order)

    def Network_sendToAll(self, data):
        data_action = data['data_action']
        data_name = data['data_name']
        data_data = data['data']
        self._server.sendToAll(data_action, data_name, data_data)

    def Network_startbattle(self, data):
        self._server.startbattle(data)

    def Network_isPlayer(self, data):
        self._server.isPlayer(data)


class GameServer(Server):
    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):

        # Call the super constructor
        Server.__init__(self, *args, **kwargs)
        self.playerChannels = []
        self.chars = []
        self.enemys = []
        self.players = []
        self.battleTurn = []

    def Connected(self, channel, addr):
        self.playerChannels.append(channel)
        self.players.append(Player(channel, len(self.playerChannels) - 1))
        print ('new connection:', channel)

        channel.Send(
            {"action": "isPlayer", "channel": len(self.playerChannels) - 1})

    def actualPlayers(self):
        self.actualplayers = []
        for player in self.players:
            if player.isPlayer:
                self.actualplayers.append(player)

    def isPlayer(self, data):
        print(self.players)
        for player in self.players:
            print(player.id)
            if player.id == data["channel"]:
                print(data["response"])
                print("NOW", player.isPlayer)
                player.isPlayer = data["response"]
                print("THEN", player.isPlayer)

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

    def addenemy(self, data):
        self.enemys.append(Enemy(self.playerChannels[0], len(self.enemys)))
        self.battleTurn = self.players + self.enemys

        for channel in self.channels:
            string = {"action": 'addenemy', 'enemy': data}
            channel.Send(string)

    def sendToAll(self, action, data_name, data):
        for channel in self.channels:
            string = {"action": action, data_name: data}
            channel.Send(string)

    def startbattle(self, data):
        self.actualPlayers()
        self.battleTurn = self.actualplayers + self.enemys

        self.turnCounter = []
        for i in range(len(self.battleTurn)):
            self.turnCounter.append(i)

        print(self.turnCounter)
        random.shuffle(self.turnCounter)
        print(self.turnCounter)

        for channel in self.playerChannels:
            channel.Send({"action": "startbattle", "start": True})

        sleep(0.10)

        self.currTurn = 0
        self.turnManager()

    def turnManager(self):
        for channel in self.channels:
            channel.Send({'action': 'yourTurn', 'isTrue': False,
                          'currTurn': self.turnCounter[self.currTurn]})
        self.battleTurn[self.turnCounter[self.currTurn]].channel.Send(
            {'action': 'yourTurn', 'isTrue': True, 'currTurn': self.turnCounter[self.currTurn]})

    def passTurn(self):
        self.currTurn = (self.currTurn + 1) % len(self.battleTurn)

        for channel in self.channels:
            channel.Send({'action': 'yourTurn', 'isTrue': False,
                          'currTurn': self.turnCounter[self.currTurn]})

        self.battleTurn[self.turnCounter[self.currTurn]].channel.Send(
            {'action': 'yourTurn', 'isTrue': True, 'currTurn': self.turnCounter[self.currTurn]})


print ("STARTING SERVER ON LOCALHOST")
gameServe = GameServer()
while True:
    gameServe.Pump()
    sleep(0.01)
