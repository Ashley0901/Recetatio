import os
from pathlib import Path

mi_ruta = Path(Path.home(),'Recetas')

def contar_recetas(ruta):
    this_ruta = Path(ruta)
    contador = 0
    for txt in this_ruta.glob('**/*.txt'):
        contador +=1
    return contador

def inicio():
    print(f"Hola bienvenido este es un administrador de Recetas\n"
          f"Las recetas se encuentran en la ruta {mi_ruta}\n"
          f"Cuentas con {contar_recetas(mi_ruta)} recetas ")
    eleccion_menu ='x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Menu:\n[1]Elegir receta\n[2]Crear Receta\n[3]Crear Categoria\n[4]Eliminar Receta\n"
              "[5]Eliminar Categoria\n[6]Finalizar Programa\nSeleciona una opcion: ")
        eleccion_menu = input()
    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print("Categoria: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categoria(lista):
    print("Escoge una categoria: ")
    numero = 'x'
    while not numero.isnumeric() or int(numero) not in range(1,len(lista)+1):
        numero = input()

    return lista[int(numero)-1]

def mostrar_recetas(categoria):
    print("Recetas: ")
    lista_recetas = []
    contador = 1
    ruta = Path(mi_ruta,categoria)
    for receta in ruta.glob('*txt'):
        receta_str = str(receta.name)
        lista_recetas.append(receta)
        print(f'[{contador}] {receta_str}')
        contador+=1
    return lista_recetas

def elegir_recetas(lista_recetas):
    eleccion = 'x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1,len(lista_recetas)+1):
        eleccion = input("Escoge una receta: ")

    return lista_recetas[int(eleccion)-1]

def leer_receta(receta):

    print(Path(receta).read_text())

def crear_receta(categoria):
    existe = False
    while not existe:
        print("Escriba el nombre de la nueva receta: ")
        nueva_receta = input()+".txt"
        print("Esctibe el contenido de la nueva receta: ")
        contenido = input()
        this_categoria = Path(categoria, nueva_receta)
        if not os.path.exists(this_categoria):
            Path.write_text(this_categoria,contenido)
            print(f'{nueva_receta} ha sido creada exitosamente\n')
            existe = True
        else:
            print("Esta receta ya existe")

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escriba el nombre de la nueva categoria: ")
        nueva_categoria= input()
        categoria_nueva = Path(ruta,nueva_categoria)
        if not os.path.exists(categoria_nueva):
            Path.mkdir(categoria_nueva)
            print(f'{nueva_categoria} ha sido creada exitosamente\n')
            existe = True
        else:
            print("Esta categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} ha sido eliminada')

def volver_inicio():
    regresar = 'x'
    while not regresar.lower() == "v":
        regresar = input("\nEscriba V para volver al inicio: ")


finalizar = False
while not finalizar:
    menu = inicio()
    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(categoria_elegida)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoria(mis_categorias)
        crear_receta(categoria_elegida)
        volver_inicio()

    elif menu == 3:
        crear_categoria(mi_ruta)

        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(categoria_elegida)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
           receta_elegida = elegir_recetas(mis_recetas)
           eliminar_receta(receta_elegida)
        volver_inicio()


    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoria(mis_categorias)
        eliminar_categoria(categoria_elegida)
        volver_inicio()

    elif menu == 6:
        finalizar = True

