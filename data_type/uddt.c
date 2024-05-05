#include "stdlib.h"
#include "stdio.h"
#include "string.h"

struct client
{
    char Name[50];
    char Id[10];
    float Credit;
    char Address[100];
};


main(int argc,char const *argv[])
{
    struct client client1 ={0};
    strcpy(client1.Name,"Julian Pinchao");
    strcpy(client1.Id,"00000001");
    client1.Credit=1000.160;
    strcpy(client1.Address,"Calle 65 Medellin");

    printf("Nombre: %s \n" ,client1.Name);
    printf("Id: %s \n",client1.Id);
    printf("Credito: %d \n",client1.Credit);
    printf("Direccion: %s \n",client1.Address);
 




    return 0;

    
}

