class SousChef:

    def make_steak(self):
        print("Chef makes steak")

    def make_ribs(self):
        print("Chef makes ribs")
    
    def make_special(self):
        print("Chef makes special BBQ dish")

#Masterchef class will import all 3 "def" from SousChef, plus others added below
class Masterchef(SousChef):

    def make_special(self):
        print("Masterchef makes special BBQ dish")

    def make_teppan(self):
        print("Masterchef makes Teppanyaki")

