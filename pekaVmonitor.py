import json
import urllib.request
import time
import string
import codecs

PEKA_URL = "http://www.peka.poznan.pl/vm/method.vm?ts="


def now_milliseconds():
    return int(time.time() * 1000)


class pekaVmonitor:

    def peka_vm_get(self, met, p0):
        url = PEKA_URL + str(now_milliseconds())
        headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
        payload = urllib.parse.urlencode({'method': met,
                                          'p0': p0}).encode("utf-8")
        req = urllib.request.Request(url, payload, headers)
        response = urllib.request.urlopen(req)
        reader = codecs.getreader("utf-8")
        # Parse Json
        data = json.load(reader(response))
        return data

    def get_1st_departure_json(self, bollard):
        json_data = self.peka_vm_get('getTimes', '{"symbol":"' + bollard + '"}')
        try:
            departure = json_data["success"]["times"][0]
            return departure
        except:
            return "error"  # .ljust(15," ")

    def get_1st_departure(self, bollard):
        departure = self.get_1st_departure_json(bollard)
        if departure != "error":
            direction = departure[
                "direction"]  # .replace(" ", "")#.encode('UTF-8')#[0:10].translate(string.punctuation)
            line = departure["line"]
            minutes = departure["minutes"]
            result = (line, direction, minutes)
            return result
        else:
            return "error"

    def get_1st_departure_xchar(self, bollard, length):
        departure = self.get_1st_departure(bollard)
        if len(departure) != 1:
            line_len = len(departure[0])
            minutes_len = len(str(departure[2]))
            length = length - line_len - minutes_len - 2  # 2 char for separators
            direction = departure[1].replace(" ", "")
            translator = str.maketrans('', '', string.punctuation)
            direction = direction.translate(translator)[0:length]
            line = departure[0]
            minutes = departure[2]
            result = '{}>{}:{}'.format(line, direction, minutes)
            return result
        else:
            return "error".ljust(length, " ")
