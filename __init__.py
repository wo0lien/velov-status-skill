from mycroft import MycroftSkill, intent_file_handler


class VelovStatus(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('status.velov.intent')
    def handle_status_velov(self, message):
        self.speak_dialog('status.velov')


def create_skill():
    return VelovStatus()

