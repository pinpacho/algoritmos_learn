class usertype:
    def __init__(self, Name, Id, Credit, Address):
        # Constructor de la clase usertype
        # Se inicializan los atributos de la instancia con los valores proporcionados
        self.Name = Name  # Nombre del usuario
        self.Id = Id  # Identificación del usuario
        self.Credit = float(Credit)  # Crédito del usuario, convertido a tipo float
        self.Address = Address  # Dirección del usuario

# Bloque de código que se ejecuta cuando el script es ejecutado directamente
if __name__ == '__main__':
    # Creación de una instancia de la clase usertype con valores específicos
    cliente1 = usertype('Julian', 123432, 10.01, 'Calle 77 #7-34')
    
    # Impresión de los atributos de la instancia cliente1
    print('Nombre: ', cliente1.Name)  # Imprime el nombre del cliente
    print('Id: ', cliente1.Id)  # Imprime la identificación del cliente
    print('Credito: ', cliente1.Credit)  # Imprime el crédito del cliente
    print('Dirección: ', cliente1.Address)  # Imprime la dirección del cliente
