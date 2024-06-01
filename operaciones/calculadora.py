
def sumar(n1,n2):
        try:
            resultado = int(n1)+int(n2)
        except:
            print("Ingrese solo números")
        else:
            return resultado

def restar(n1,n2):
    try:
         resultado=int(n1)-int(n2)
    except:
            print("Ingrese solo números")
    else:
        return resultado


def multiplicar(n1,n2):
    try:
         resultado=int(n1)*int(n2)
    except:
            print("Ingrese solo números")
    else:
        return resultado


def dividir(n1,n2):
    try:
         resultado=int(n1)/int(n2)
    except ValueError:
            print("Ingrese solo números")
    except ZeroDivisionError:
            print("El numero no puede ser dividido entre 0")
    else:
        return resultado
    return 
