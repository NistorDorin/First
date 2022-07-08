'''
revolver

model
gloante
piedica pusa

constructor - model

descrie()
incarca()
trage()
pune_piedica()
scoate_piedica()
'''

class Revolver:
    model = None
    gloante = 3
    piedica_pusa = True

    def __init__(self, model):
        self.model = model

    def descrie(self):
        print(f'model = {self.model}, gloante = {self.gloante} și piedica pusa = {self.piedica_pusa}')

    def incarca(self, gloante):
        self.gloante += gloante

    def trage(self):
        if self.piedica_pusa == True:
            print("Nu putem trage! Piedica este pusa")
        else:
            if self.gloante > 0:
                print('BOOM')
                self.gloante -=1
            else:
                print('Nu avem gloante')


    def pune_piedica(self):
        self.piedica_pusa = True

    def scoate_piedica(self):
        self.piedica_pusa = False

pistol = Revolver('Glock')
pistol.trage()
pistol.scoate_piedica()
pistol.trage()
pistol.trage()
pistol.trage()
pistol.trage()

pistol.incarca(5)
pistol.trage()