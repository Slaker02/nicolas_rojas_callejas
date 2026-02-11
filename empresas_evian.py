import os, json

PROV_FILE = 'proveedores.json'
ART_FILE = 'articulos.json'

def ensure_file(path):
    if not os.path.exists(path):
        with open(path,'w',encoding='utf-8') as f:
            json.dump([], f, indent=4, ensure_ascii=False)

def load(path):
    ensure_file(path)
    with open(path,'r',encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save(path, data):
    with open(path,'w',encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def agregar_proveedor():
    nombre = input('Nombre proveedor: ').strip()
    ubic = input('Ubicación: ').strip()
    provs = load(PROV_FILE)
    provs.append({'nombre': nombre, 'ubicacion': ubic})
    save(PROV_FILE, provs)
    print('Proveedor agregado con éxito.')

def agregar_articulo():
    nombre = input('Nombre artículo: ').strip()
    categoria = input('Categoría: ').strip()
    while True:
        try:
            precio = float(input('Precio: '))
            break
        except ValueError:
            print('Ingrese un número válido para el precio.')
    proveedor = input('Proveedor asociado: ').strip()
    arts = load(ART_FILE)
    arts.append({'nombre': nombre, 'categoria': categoria, 'precio': precio, 'proveedor': proveedor})
    save(ART_FILE, arts)
    print('Artículo agregado con éxito.')

def mostrar_info():
    provs = load(PROV_FILE)
    arts = load(ART_FILE)
    print('\n--- Proveedores ---')
    print(json.dumps(provs, indent=4, ensure_ascii=False))
    print('\n--- Artículos ---')
    print(json.dumps(arts, indent=4, ensure_ascii=False))

def menu():
    while True:
        print('\n1) Agregar proveedor\n2) Agregar artículo\n3) Mostrar información\n4) Salir')
        op = input('Opción: ').strip()
        if op=='1': agregar_proveedor()
        elif op=='2': agregar_articulo()
        elif op=='3': mostrar_info()
        elif op=='4': break
        else: print('Opción inválida.')

if __name__=='__main__':
    ensure_file(PROV_FILE); ensure_file(ART_FILE)
    menu()