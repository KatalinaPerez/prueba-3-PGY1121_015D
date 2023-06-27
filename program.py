import funciones as fn
nombres=[]
ruts=[]
nacimientos=[]
categorias=[]
celulares=[]
idparejas=[]
correos=[]
while True:
    opc=fn.menu()
    if opc==1:
        nombres,ruts,nacimientos,categorias,celulares,idparejas,correos=fn.grabar(nombres,ruts,nacimientos,categorias,celulares,idparejas,correos)
    elif opc==2:
        ruts,nombres,categorias,celulares,correos=fn.buscar(ruts,nombres,categorias,celulares,correos)
    elif opc==3:
        idparejas,nombres=fn.imprimir(idparejas,nombres)
    else:
        fn.salir
        break
