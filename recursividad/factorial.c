#include<stdio.h>

long resultado;
int n;


long factorial(int n){
    if(n==0)
        return 1;
    else 
        return(n * factorial(n-1));

}

int main(int argc, char const *argv[])
{
    printf("Ingrese el numero a calcular \n");
    scanf("%d",&n);
    if (n <0)
    {
        printf("El numero debe ser positivo\n");
        
    }
    else{
        resultado = factorial(n);
        printf("%d! = %d\n",n,resultado);
    }
    return 0;
}
