class Musician(object):
    def __init__(self,sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
    
    

class Bassist(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink","Bow", "Boom"])
    
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bum", "Brum", "Brrumble"])
    
    def count(self):
        print("One, Two, Three, Four")
    
    def combust(self):
        print("Combust!")

class Band(object):
    def __init__(self, members = []):
        self.members = members
    
    def hire(self, member):
        self.members.append(member)
    
    def fire(self, member):
        self.members.remove(member)
    
    def solos(self):
        print("Solos for every member in the band. Drums, start us off!")
        Drummer().count()
        for i in range(len(self.members)):
            self.members[i].solo(6)
        

Scalding_Hot = Band()
Scalding_Hot.hire(Drummer())
Scalding_Hot.hire(Guitarist())

Scalding_Hot.solos()