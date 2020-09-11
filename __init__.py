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
        output=report['data']['conditions'][0]['observation']
        waveminam=report['data']['conditions'][0]['am']['minHeight']
        wavemaxam=report['data']['conditions'][0]['am']['maxHeight']
        waveminpm=report['data']['conditions'][0]['pm']['minHeight']
        wavemaxpm=report['data']['conditions'][0]['pm']['maxHeight']
        wavesum='The waves will range from '+str(waveminam)+' feet to '+str(wavemaxam)+' feet in the morning, and will range from '+str(waveminpm)+' feet to '+str(wavemaxpm)+' feet in the afternoon'
        waverateam=report['data']['conditions'][0]['am']['rating']
        waveratepm=report['data']['conditions'][0]['pm']['rating']
        if waverateam==waveratepm:
            waverateoutput=waverateam.replace('_',' ')
        else:
            waverateoutput='The rating will start at '+waverateam.replace('_',' ')+'  in the morning and shift to '+waveratepm.replace('_',' ')+' in the afternoon'

        self.speak(str(output))
        self.speak(str(wavesum))
        self.speak(str(waverateoutput))
        self.speak_dialog('status.surf')


def create_skill():
    return SurfStatus()

