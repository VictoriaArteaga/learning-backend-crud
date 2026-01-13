contactos = [{'id': 1, 'nombre': 'Maria', 'telefono': '3145588274'},
            {'id': 2, 'nombre': 'Sara', 'telefono': '3194858361'},
            {'id': 3, 'nombre': 'Anna', 'telefono': '3189151380'}]

def buscar_por_id(id):
    for contacto in contactos:
        if contacto['id'] == id:
            return contacto 
        
    return None
        
def eliminar_por_id(id):
    for posicion, contacto in enumerate(contactos):
        if contacto['id'] == id:
            del contactos[posicion]
            return True
    return False

print(buscar_por_id(2))
print(eliminar_por_id(3))
print(contactos)

