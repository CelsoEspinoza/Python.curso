class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('runnnn')

    @classmethod
    def cls_method(cls, param1):
        return cls(param1)
    
    @staticmethod
    def stc_method(param1, param2):
        pass

player1 = PlayerCharacter('Celsooo')
player1.run()

PlayerCharacter.cls_method('Juan').run()