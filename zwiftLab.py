from zwift import Client
import json
import pprint
import config

_client = Client(config.zwift_username, config.zwift_password)


def get_profile(client):
    profile = client.get_profile()
    return profile.profile  # fetch your profile data


def get_activities(profile):
    return profile.get_activities()  # metadata of your activities


def pretty_print(input):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(input)


def get_TotalDistance(profile):
    return profil[u'totalDistance'] / 1000


def get_world(client):
    return client.get_world(1)


def get_players_in_world(world):
    players = world.players
    return players['friendsInWorld']


world = get_world(_client)

firstPlayer_id = get_players_in_world(world)[0]["playerId"]

status = world.player_status(firstPlayer_id)

power = status.power

cadence = status.cadence

print(power)
print(cadence)

# json = json.dumps(players)
# f = open("dict.json","w")
# f.write(json)
# f.close()

# print(players)
