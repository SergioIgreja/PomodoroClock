#Classe criada para armazenar os valores inseridos e para validá-los
class Task:

    def __init__(self, name, estimated_pomodoros):
        self.name = name
        if estimated_pomodoros > 0:
            self.estimated_pomodoros = estimated_pomodoros
        else:
            raise ValueError

    def __str__(self):
        return "Nome:"+ self.name + " | Pomodoros:" + str(self.estimated_pomodoros)
    
    