from mycroft import MycroftSkill, intent_file_handler
import datetime, urllib.request, urllib.error, urllib.parse, json, time, calendar
from decimal import *

def report_pull(spotName,spotID,regionalID,statezip):
    surflinewavesbase="http://services.surfline.com/kbyg/spots/forecasts/conditions?spotId=00000&6&maxHeights=false"
    surflinewaves=surflinewavesbase.replace('00000',spotID)

    webreq=urllib.request.Request(surflinewaves)
    opener=urllib.request.build_opener()
    f=opener.open(webreq)
    fstr=f.read().decode('utf-8')
    rep=json.loads(fstr)
    return rep

class SurfStatus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('status.surf.intent')
    def handle_status_surf(self, message):
        # For initial tests this will only cover one location.
        # Eventually need to expand to be flexible. 
        report=report_pull('Belmar','5842041f4e65fad6a7708a01','2147','NJ/07715')
        output=report[['data']['conditions'][0]['observation']]
        self.speak(str(output))
        self.speak_dialog('status.surf')


def create_skill():
    return SurfStatus()

