def validaop(texto,min=None, max=None):
    while True:
        try:
            opc=int(input(texto))
            if min!=None and max!=None:
                if min<=opc<=max:
                    break
                else:
                    print("ERROR! Fuera de rango")
            elif min!=None:
                if min<opc:
                    break
                else:
                    print(f"ERROR! Valor ingresado debe ser mayor a {min}")
            elif max!=None:
                if max>opc:
                    break
                else:
                    print(f"ERROR! Valor ingresado debe ser menor a {max}")
            else:
                break
        except:
            print("ERROR! El valor ingresado debe ser un número")
    return opc

def menu():
    print("*"*40)
    print("\t Registro padel")
    print("*"*40)
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir parejas")
    print("4. Salir")
    opc=validaop("Ingrese opción: ",1,4)
    return opc

def validalargo(texto,largo,booleano):
    while True:
        dato=input(texto)
        if booleano:
            if len(dato)>=largo:
                break
            else:
                print(f"ERROR! Debe tener al menos {largo} digitos/caracteres")
    return dato

def categoria():
    print("1. Oro")
    print("2. Plata")
    print("3. Bronce")
    cat=validaop("Ingrese ctaegoria: ",1,3)
    return cat

def validacorreo():
    while True: 
        dato=validalargo("Ingrese correo de jugador(a): ",6,True)
        if '@' in dato:
            if '.' in dato:
                break
            else:
                print("ERROR! Falta un '.' en correo")
        else:
            print("ERROR! Falta un '@' en correo")
    return dato

def grabar(nombres,ruts,nacimientos,categorias,celulares,idparejas,correos):
    nombres.append(validalargo("Ingrese Nombre del jugador(a): ",2,True))
    ruts.append(str(input("Ingrese rut de jugador(a) sin numero digitador: ")))
    #validar edad
    nacimientos.append(input("Ingrese fecha de nacimiento de jugador(a) [dia 00/mes 00/año 00]: "))
    categorias.append(categoria())
    celulares.append(input("Ingrese fono de jugador(a):  "))
    idparejas.append(input("Ingrese nombre asignado a grupo: "))
    correos.append(validacorreo())
    print("Jugador(a) ingresado con éxito!")
    return nombres,ruts,nacimientos,categorias,celulares,idparejas,correos

def buscar(ruts,nombres,categorias,celulares,correos):
    dato=str(input("Ingrese rut de jugador(a): "))
    rut=ruts.find(dato)#No ocupa find
    if rut!=-1:
        print(f" {nombres[rut]} | {categorias[rut]} | {celulares[rut]} | {correos[rut]}")
    else:
        print("ERROR! El rut ingresado no se encuentra")
    return ruts,nombres,categorias,celulares,correos

def imprimir(idparejas,nombres):##OJITO arreglar
    dato=str(input("Ingrese Id de pareja: ")).upper()
    for i in len(idparejas):
        id=idparejas.find(dato)
        if id!=-1:
            print ({nombres[id]})
        else:
            print("ERROR! Id de equipo no encontrado")

def salir():
    print("Hasta pronto")
    print("Se despide: Katalina Pérez")