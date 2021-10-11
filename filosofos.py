import time
import random
import threading
import queue


platos = queue.Queue(maxsize=5)
comensales = ['filoso 1', 'filosofo 2', 'filosofo 3', 'filosofo 4', 'filosofo 5']
contador = 0

def filosofos():
    global contador
    while contador<5:
        if not platos.full():
            comensal = random.choice(comensales)
            comensales.remove(comensal)
            platos.put(comensal)
            print(comensal, 'comiendo')
            contador+=1
            time.sleep(random.randint(1,3))

def comer():
    while contador<=5:
        if not platos.empty():
            persona_cenando = platos.get()
            platos.task_done()
            print(persona_cenando, 'termino')
            time.sleep(random.randint(1,3))


if __name__ == "__main__":
    thread_filosofo = threading.Thread(target=filosofos)
    thread_comer = threading.Thread(target=comer)

    thread_filosofo.daemon = True
    thread_comer.daemon = True

    thread_filosofo.start()
    thread_comer.start()
    
    
    

    while True:
        if contador == 5:
            time.sleep(2)
            break
            

        
        
