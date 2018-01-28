import queue

#Classe criada para alterar o __str__ original da classe Queue, uma vez que esse imprimia a localização do 
#objeto na memória. Esta classe extende a classe nativa Queue.
class MyQueue(queue.Queue):
    def __str__(self):
        string = "Tarefas:\n"
        for elem in list(self.queue):
            string += elem.__str__() + "\n" 

        return string    