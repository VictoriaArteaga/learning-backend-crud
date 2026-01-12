contactos = {}

def crear_contacto():

    nombre = input('Ingrese el nombre:').strip().lower() #.strip() para evitar espacios adicionales
    telefono = input('Ingrese el número de telefono: ')
    if nombre in contactos:
        print('El contacto ya existe')
    else:
        # .isdigit() Es para verificar si un texto es un número
        if telefono.isdigit() and 0 < len(telefono) < 11:
            contactos[nombre] = telefono
        else: 
            print('Debes introducir un número de telefono valido')
    print (f'Contacto creado correctamente')

#print(crear_contacto())
def buscar_contacto():
    buscar = input('Ingrese el nombre del contacto a buscar:').lower()
    
    if buscar in contactos:
        print(f'{buscar}: {contactos[buscar]}')
    else:
        print(f'El contacto {buscar} no existe / no se encontro')

def actualizar_contacto():
    actualizar = input('Ingrese el contacto a actualizar: ').lower()

    if actualizar in contactos:
        telefono = input('Ingrese el nuevo telefono:')
        if telefono .isdigit() and 0 < len(telefono) < 11:
            contactos[actualizar] = telefono  
            print(f'El contacto {actualizar} ha sido actualizado: {contactos[actualizar]}')
        else:
            print('Debes ingresar un número de telefono valido ')
    else:
        print('Contacto no encontrado')


def eliminar_contacto():
    eliminar = input('Escribe el nombre del contacto a eliminar: ').lower()
    if eliminar in contactos:
        del contactos[eliminar]
        print('Contacto eliminado')
        print(contactos)
    else: 
        print(f'El contacto {eliminar} no existe, no se puede eliminar.')

def mostrar_contactos():
    posicion = 1
    for nombre, telefono in contactos.items():
        print(f'{posicion}. {nombre}: {telefono} ')
        posicion += 1

def menu():

    while True:
        print(' --- BIENVENID@ A LA AGENDA DE CONTACTOS POR CONSOLA ---')
        print('1. Crear contacto')
        print('2. Buscar contacto')
        print('3. Actualizar dato del contacto')
        print('4. Eliminar contacto')
        print('5. Ver todos los contactos')
        print('6. Salir')
        
        try:
            opcion = int(input('Por favor escriba el número de la opción que desea realizar: '))
        except ValueError:
            print('Debes ingresar solo números validos. ')
            continue

        match opcion:
            case 1: 
                crear_contacto()
            case 2:
                buscar_contacto()
            case 3:
                actualizar_contacto()
            case 4:
                eliminar_contacto()
            case 5:
                mostrar_contactos()
            case 6:
                print('GRACIAS POR USAR LA AGENDA DE CONTACTOS, ADIOS!')
                break
            case _:
                print('Opción incorrecta. ')


def main():
    menu()


if __name__ == '__main__':
    main()
