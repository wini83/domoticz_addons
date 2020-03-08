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


def pretty_print(payload):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(payload)


def get_total_distance(profile):
    return profile[u'totalDistance'] / 1000


def get_world(client):
    return client.get_world(1)


def get_players_in_world(world_obj):
    players = world_obj.players
    return players['friendsInWorld']

def print_1stplayerpowandcad(client):
    world = get_world(_client)

    firstPlayer_id = get_players_in_world(world)[0]["playerId"]

    status = world.player_status(firstPlayer_id)

    power = status.power

    cadence = status.cadence

    print(power)
    print(cadence)



profile = get_profile(_client)

is_riding = profile["riding"]

print(is_riding)


#pretty_print(profile)
