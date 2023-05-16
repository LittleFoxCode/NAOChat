from Talker import Talker

class NAOTalker(Talker):
    def __init__(self, language: str = "en"):
        super().__init__(language)

    def say(self, to_say: str):
        raise NotImplementedError