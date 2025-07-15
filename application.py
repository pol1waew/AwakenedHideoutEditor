from hideout import Hideout


class Application:
    hideout : Hideout


    def __init__(self):
        pass


    def load_hideout(self, file_name : str):
        self.hideout = Hideout(file_name)        

    def export_hideout(self):
        pass 