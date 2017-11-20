from Control_Distribuido import *

class Cliente_Distribuido(Control_Distribuido):

    def __init__(self):
        Control_Distribuido.__init__(self, "Cliente")
        print("Constructor CC")
