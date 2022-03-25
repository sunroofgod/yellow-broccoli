class IronBoard():
    def __init__(self,name):
        self.name = name
    
class Iron():
    def __init__(self,board=None,clothing=None):
        # type(board) = IronBoard
        # type(clothing) = Clothes
        # type(temp) = int, in Celcius
        # type(button) = Boolean
        self.board = board if not None else 0
        self.clothing = board if not None else 0
        self.temp = 148 
        self.button = 0
    
    def add_board(self,board):
        self.board = board
    
    def add_clothes(self,clothes):
        self.clothing = clothes
    
    def remove_clothes(self):
        self.clothing = None
    
    def turn_switch(self):
        if self.button != 0:
            self.button = 0
        else:
            self.button = 1

    def get_clothing(self):
        return self.clothing

    def get_temp(self):
        return self.temp
    
    def ironing(self):
        print(f"welcome to the Iron Unit ϵ( 'Θ' )϶, checking for clothes type to start")
        print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        if not self.board:
            print(f"Board not detected! \nPlease use board. \nTurning off power now...")
            if self.button:
                return f"Cancelling power off."
            else:
                return f"Power off."
            
        elif not self.clothing:
            print(f"Please put clothes beneath the iron. \nTurning of power now...")
            if self.button:
                return f"Cancelling power off."
            else:
                return f"Power off."

        else:
            print(f"Type of clothing is '{self.get_clothing().get_type()}' ")
            if self.get_clothing().opt_temp() == self.get_temp():
                return f"Right Temp."
            else:
                print(f"Changing temperature to {self.get_clothing().opt_temp()}")
                self.temp = self.get_clothing().opt_temp()
                print(f" ")
                return f"Temperature has been changed. Continue ironing."

class Clothes():
    def __init__(self,type,temp):
        self.type = type
        self.temp = temp
    
    def get_type(self):
        return self.type
    
    def opt_temp(self):
        return self.temp

cotton = Clothes("Cotton",204)
linen = Clothes("Linen",230)
wool = Clothes("Wool",148)
iron_board = IronBoard("board1")
my_iron = Iron()

print("-------")
print("Once you on the switch and you starting Ironing, the internal iron software sends message to itself")
print("-------")
print(f" ")
print(my_iron.ironing())
print(f" ")
print("-------")

my_iron.add_board(iron_board)
print("Once the ironing board is added:")
print("-------")
print(f" ")
print(my_iron.ironing())
print(f" ")
print("-------")

my_iron.add_clothes(wool)
print("Let's say you add wool clothes, the default temperature at starting is 148 Degree Celcius, which is the right temp")
print("-------")
print(f" ")
print(my_iron.ironing())
print(f" ")
print("-------")

my_iron.remove_clothes()
my_iron.add_clothes(cotton)
print("Let's say you add cotton clothes, but cotton clothes optimal temp is 204 Degree Celcius")
print("-------")
print(f" ")
print(my_iron.ironing())
print(f" ")
print("-------")

