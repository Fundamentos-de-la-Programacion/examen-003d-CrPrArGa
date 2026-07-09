planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
    }

inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15],
}

def validar_texto(texto):
    return texto.strip() != ""

def validar_plan(texto):
    return texto.lower() in ["mensual", "trimestral", "anual"]

def validar_postivo(valor):
    try:
        num = int(valor)
        return num > 0
    except ValueError:
        return False
    
def validar_acceso(acceso):
    return acceso.lower() in ["s", "n"]

def validar_clases(clases):
    return clases.lower() in ["s", "n"]

def leer_opcion():
    while True:
        opc = int(input("Ingrese una opcion (1-6): "))
        try:
            if (1 <= opc <= 6):
                return opc
            else:
                print("Error: Debe ingresar un numero dentro del rango.")
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")

def validar_horario(valor):
    return valor.lower().strip() != ""

def buscar_codigo(codigo, diccionario):
    for cod in diccionario:
        if cod.lower() == codigo.lower():
            return cod
    return None

def cupos_tipo(tipo, planes, inscripciones):
    total = 0
    for codigo, datos in planes.items():
        if datos[1].lower() == tipo.lower():
            cant = inscripciones[codigo][1]
            total += cant
    print(f"El total de planes {tipo} es: {total}.")

def busqueda_precio(p_min, p_max, planes, inscripciones):
    resultados = []
    for codigo, datos in inscripciones.items():
        if p_min <= datos[0] <= p_max and datos[1] != 0:
            resultados.append(f"{planes[codigo][0]}--{codigo}")
        resultados.sort()
        if len(resultados) == 0:
            print("No se encontraron resultados.")
        else:
            print(f"Los resultados fueron: {resultados}")            
            

def actualizar_precio(codigo, nuevo_precio):
    codigo_exacto = buscar_codigo(codigo, planes)
    if codigo_exacto:
        inscripciones[codigo][0] = nuevo_precio
        return True
    return None

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos):
    if buscar_codigo(codigo, planes) is not None:
        return False
    
    tiene_acceso = True if acceso_piscina.lower() == "s" else False
    tiene_clases = True if incluye_clases.lower() == "s" else False

    cod_upper = codigo.upper()
    planes[cod_upper] = [nombre, tipo.lower(), duracion, acceso_piscina, incluye_clases, horario, precio, cupos]
    inscripciones[cod_upper] = [int(precio), int(cupos)]
    return True

def eliminar_plan(codigo, planes, inscripciones):
    codigo_exacto = buscar_codigo(codigo, planes)
    if codigo_exacto:
        del planes[codigo_exacto]
        del inscripciones[codigo_exacto]
        return True
    return False

def main(): 
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por tipo de plan")
        print("2. Búsqueda de planes por rango de precio")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar plan")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()
        if opcion == 1:
            plan = input("Ingrese el tipo de plan a consultar: ")
            cupos_tipo(tipo.lower(), planes, inscripciones)
        
        elif opcion == 2:
            try:
                p_min = int(input("Ingrese precio minimo: "))
                p_max  = int(input("Ingrese precio maximo: "))
                if p_min < 0 or p_max < 0:
                    print("El precio minimo o máximo no puede ser menor que 0")
                elif p_min > p_max:
                    print("El precio minimo no puede ser mayor que el máximo")
                else:
                    busqueda_precio(p_min, p_max, planes, inscripciones)
            except ValueError:
                print("")

        elif opcion == 3:
            while True:
                codigo = input("Ingrese el codigo del plan: ")
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    if nuevo_precio <= 0:
                        print()
                        continue

                    if actualizar_precio(codigo, nuevo_precio, inscripciones):
                        print ("Precio actualizado con exito.")
                    else:
                        print("Error")
                except ValueError:
                    print("Error")

                repetir = input("¿Desea actualizar otro precio (s/n)? ").lower()
                if repetir != "s":
                    break

        elif opcion == 4:
            print("Registro nuevo plan")
            codigo = input("codigo: ")
            nombre = input("Nombre: ")
            tipo = input("Tipo: ")
            duracion = int(input("Duracion: "))
            acceso = input("Acceso (s/n): ")
            clases = input("Clases (s/n): ")
            horario = input("Horario: ")
            precio = int(input("Precio: "))
            cupos = input("Cantidad de cupos: ")
            
            if (validar_texto(codigo), validar_texto(nombre), validar_plan(tipo), validar_postivo(duracion), validar_acceso(acceso), validar_clases(clases), validar_horario(horario), validar_texto(cupos), validar_postivo(precio)):
                exito = agregar_plan(codigo, nombre, tipo, duracion, acceso, clases, precio, cupos, horario)
            else:
                print("Error")
        elif opcion == 5:
            codigo = input("Ingrese el codigo del plan que desea eliminar: ")
            if eliminar_plan(codigo, planes, inscripciones):
                print("Plan eliminado correctamente.")
            else:
                print("Error")

        elif opcion == 6:
            print("Programa finalizado.")
            break     

if __name__ == "__main__":
    main()

