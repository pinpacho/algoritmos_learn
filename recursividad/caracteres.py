def reverseString(string):
    if string == "":
        return string
    else:
        return reverseString(string[1:]) + string[0]

def reverseStringlist(stringlist):
    return stringlist[::-1]

if __name__=='__main__':

    string = input("Escribe el string que quieres voltear: ")
        
    print(reverseString(string))
    print(reverseStringlist(string))