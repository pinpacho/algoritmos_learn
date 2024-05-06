#include<stdio.h>

void cambiar_posicion(int *n1, int *n2){
    int temp= *n1;
    *n1 = *n2;
    *n2 = temp;
}

void bubbleSort(int vector_entrada[], int n)
{
    int i, j;
    for(i=0; i<n-1; i++)
    {
        for(j=0; j<n-i-1;j++){
            if(vector_entrada[j]>vector_entrada[j+1])
            cambiar_posicion(&vector_entrada[j],&vector_entrada[j+1]);
        }
    }    

}

int print_array(int vector_entrada[], int n)
{
    int i;
    for(i=0;i<n;i++)
        printf("%d  ,",vector_entrada[i]);
    printf("\n Fin del ordenamiento");
}

int main(int argc, char const *argv[])
{
    int vector_entrada[]={100,1992,9,0,-2,45,234,2};
    int n = sizeof(vector_entrada)/sizeof(vector_entrada[0]);
    bubbleSort(vector_entrada,n);
    print_array(vector_entrada,n);
    printf("\n");
    return 0;
}
