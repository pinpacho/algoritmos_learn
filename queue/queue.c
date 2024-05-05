#include<stdio.h>
#define SIZE 5

int values[SIZE], front = -1, rear=-1;

void imprimir(int v[]){
  for(int i=front; i<=rear; i++){
    printf("%d, ", v[i]);
  }
  printf("\n");
}

void enQueue(int value){
    if(rear == SIZE-1){
        printf("Nuestro Queue esta lleno \n");
        imprimir(values);
    }else{
        if(front == -1 )
            front = 0;
        
        values[rear] = value;
        printf("Se inserto el valor %d correctamente\n", value);
        imprimir(values);
    }

}


void deQueue(){
    if(front == -1)
        printf("Nuestro Queue esta vacio \n");
    else{
        printf("Se elimino el valor %d \n", values[front]);
        front++;
        imprimir(values);
        if(front > rear)
            front = rear = -1;

    }

}

main(int argc, char const *argv[])
{
    
    enQueue(11);
    enQueue(12);
    enQueue(13);
    enQueue(14);
    enQueue(25);
    deQueue();
    deQueue();
    enQueue(22);
    deQueue();
    deQueue();
    enQueue(23);
    deQueue();
    enQueue(1);
    enQueue(2);
    enQueue(3);
    enQueue(4);
    enQueue(5);
    enQueue(6);
    deQueue();
    

    return 0;
}
