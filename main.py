from win10toast import ToastNotifier
from task import Task
from time import sleep
from myqueue import MyQueue
import config
import queue
    
#ToastNotifier é uma biblioteca que acede á API do windows para criar notificações
NOTIFIER = ToastNotifier()
task_queue = MyQueue(0)

#Loop do menu do programa
def main():
    while True:
        print("---------------------\nPomodoro Clock\n"
        "Inserir tarefas - 0\n"
        "Listar tarefas - 1\n"
        "Iniciar - 2\n"
        "Sair - s/S q/Q\n"
        "---------------------")
        function = input()
        if function in ["s","S","q","Q"]:
            break
        elif function == "0":
            insert_tasks()
        elif function == "1":
            list_tasks()
        elif function == "2":
            start()

#Método utilizado para listar as tarefas criadas
def list_tasks():
    print(task_queue.__str__())

#Método utilizado para criar tarefas. O input está a ser validado na classe Task, caso haja algum erro
#será levantada a exceção ValueError e o programa pede para introduzir novos valores
def insert_tasks():
    print("Está a inserir tarefas, para terminar insira s/S ou q/Q!\n----------------------------")
    while True:
        name = input("Nome da tarefa: ")
        if name in ["s","S","q","Q"]:
            break
        elif name:
            estimated_pomodoros = input("Número estimado de pomodoros: ")
            try:
                task_queue.put(Task(name,int(estimated_pomodoros)))
                print("----------------------------")
            except ValueError:
                print("Número inválido!\n----------------------------")

"""
Inicia a execução das tarefas. É utilizado um contador auxiliar para verificar se a pessoa já
trabalhou em 4 pomodoros. Se esse for o caso, a pessoa tem direito a um descanso mais elevado
do que o normal. É utilizada a função sleep para cronometrar o tempo que a pessoa se encontra 
em trabalho e em descanso. São também utilizadas as notificações para a pessoa saber em que 
fase está.
"""
def start():
    counter = 0
    while True:
        try:
            task = task_queue.get(False)
            NOTIFIER.show_toast("Pomodoro Clock",
                "Inicio da tarefa " + task.name ,
                icon_path="img\clock.ico",
                duration=5)
            while task.estimated_pomodoros > 0:
                sleep(config.POMODORO_TIMER*60)
                task.estimated_pomodoros -= 1
                counter += 1
                if counter % 4 == 0:
                    NOTIFIER.show_toast("Pomodoro Clock",
                        "Fim de um set de 4 pomodoros, descanse "+ str(config.POMODORO_LONG_BREAK) + " minutos!",
                        icon_path="img\clock.ico",
                        duration=5)
                    sleep(config.POMODORO_LONG_BREAK*60)
                else:
                    NOTIFIER.show_toast("Pomodoro Clock",
                        "Fim do pomodoro, descanse "+ str(config.POMODORO_SHORT_BREAK) + " minutos!",
                        icon_path="img\clock.ico",
                        duration=5)
                    sleep(config.POMODORO_SHORT_BREAK*60)
                
                
                if task.estimated_pomodoros != 0:
                    NOTIFIER.show_toast("Pomodoro Clock",
                        "Fim do descanso, volte ao trabalho!",
                        icon_path="img\clock.ico",
                        duration=5)
                
        except queue.Empty:
            NOTIFIER.show_toast("Pomodoro Clock",
                   "Bom trabalho, acabou as suas tarefas!" ,
                   icon_path="img\clock.ico",
                   duration=5)
            
            break

#Execução do menu
main()