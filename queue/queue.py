SIZE = 5
values = [0] * SIZE
front = -1
rear = -1

def imprimir(v):
    for i in range(front, rear + 1):
        print(v[i], end=", ")
    print()

def enQueue(value):
    global front, rear
    if rear == SIZE - 1:
        print("Nuestro Queue está lleno")
        imprimir(values)
    else:
        if front == -1:
            front = 0
        rear += 1
        values[rear] = value
        print(f"Se insertó el valor {value} correctamente")
        imprimir(values)

def deQueue():
    global front, rear
    if front == -1:
        print("Nuestro Queue está vacío")
    else:
        print(f"Se eliminó el valor {values[front]}")
        front += 1
        imprimir(values)
        if front > rear:
            front = rear = -1

enQueue(11)
enQueue(12)
enQueue(13)
enQueue(14)
enQueue(25)
deQueue()
deQueue()
enQueue(22)
deQueue()
deQueue()
enQueue(23)
deQueue()
enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
enQueue(5)
enQueue(6)
deQueue()
