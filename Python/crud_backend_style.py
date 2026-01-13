contactos = []
contador_id = 1
def crear_contacto(nombre, telefono):
    if not telefono.isdigit() or not 0 < len(telefono) < 11:
        return None
    else:
        global contador_id
        contacto = {
            'id': contador_id,
            'nombre': nombre,
            'telefono': telefono
        }
        contador_id += 1
        contactos.append(contacto)
        return contacto

def buscar_contacto(contacto_id):
    for contacto in contactos:
        if contacto['id'] == contacto_id:
            return contacto
    return None

def actualizar_contacto(contacto_id, nuevo_telefono):

    if not nuevo_telefono.isdigit() or not 0 < len(nuevo_telefono) < 11:
        return None
    else:
        for contacto in contactos:
            if contacto['id'] == contacto_id:
                contacto['telefono'] = nuevo_telefono  
                return contacto
    return None

# Para borrar un valor en una lista, Python necesita su indice no el objeto: por eso usamos enumerate()
def eliminar_contacto(contacto_id):
    for posicion, contacto in enumerate(contactos):
        if contacto['id'] == contacto_id:
            del contactos[posicion]
            return True
    return False

def main():
    c1 = crear_contacto('maria','3196320922')
    c2 = crear_contacto('anna','3189151380')

    print(buscar_contacto(c1['id']))
    print(actualizar_contacto(c1['id'], '3111111111'))
    print(eliminar_contacto(c2['id']))

if __name__ == '__main__':
    main()