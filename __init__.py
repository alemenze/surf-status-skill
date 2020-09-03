from mycroft import MycroftSkill, intent_file_handler


class SurfStatus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('status.surf.intent')
    def handle_status_surf(self, message):
        self.speak_dialog('status.surf')


def create_skill():
    return SurfStatus()

