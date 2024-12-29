#FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
#SECCIÓN DEL CURSO: L-4
#PROFESOR DE TEORÍA: Luis Corral,
#PROFESOR DE LABORATORIO: Fancisco Moreno
#GRUPO: 2
#
#INTEGRANTES
#1. Benjamín Emmanuel Estrada Villagra 21.820.688-3
#2. Belén Victoria Jara Rivera 21.616.279-k
#3. Patricia Irarrazabal 21.353.550-1
#4. Nicolas Leiva 21.468.933-2
#5. Karla Gonzalez
# DESCRIPCIÓN DEL PROGRAMA: Este programa gestiona la disponibilidad de baños en diferentes sectores durante un evento de corte de agua.
# Su propósito es identificar cuáles baños están operativos en cada sector afectado y mostrar alternativas disponibles para los usuarios.


# Función para obtener los baños disponibles
def obtener_banos_disponibles(sectores_afectados, sectores_baños):
    """
    Obtiene los baños disponibles considerando los sectores afectados.

    Args:
        sectores_afectados: Lista de sectores afectados con sus baños funcionales.
        sectores_baños: Lista de sectores y todos sus baños disponibles.

    Returns:
        Lista de tuplas con sectores y sus baños disponibles.
    """
    baños_disponibles = []

    for sector, baños_totales in sectores_baños:
        # Buscar si el sector está afectado
        for afectado_sector, baños_funcionales in sectores_afectados:
            if sector == afectado_sector:
                # Si el sector está afectado, verificar baños funcionales
                if baños_funcionales:
                    baños_disponibles.append((sector, baños_funcionales))
                else:
                    baños_disponibles.append((sector, ["No hay baños disponibles"]))
                break
        else:
            # Si el sector no está afectado, incluir todos sus baños
            baños_disponibles.append((sector, baños_totales))
    
    return baños_disponibles

# Lista de sectores y sus baños
sectores_baños = [
    ["Sector ED", ["Baño 1er piso(ED)", "Baño 2do piso(ED)", "Baño 3er piso(ED)", "Baño 4to piso(ED)", 
                   "Baño 5to piso(ED)", "Baño 6to piso(ED)", "Baño 7mo piso(ED)", "Baño 8vo piso(ED)"]],
    ["Sector EAO", ["Baño 1(EAO)", "Baño 2(EAO)"]],
    ["Sector Biblioteca Central", ["Baño Biblioteca Central"]],
    ["Sector Departamento de Física", ["Baño 1er piso(Dep.Física)", "Baño 2do piso(Dep.Física)"]],
]

# Solicitar datos al usuario
sectores_afectados = []
while True:
    sectores = input("Ingrese los sectores afectados separados por comas: ").split(", ")
    sectores_validos = [sec[0] for sec in sectores_baños]
    if all(sector.strip() in sectores_validos for sector in sectores):
        break
    else:
        print("No existe ese sector. Intente nuevamente.")

for sector in sectores:
    sector = sector.strip()
    for sec, baños in sectores_baños:
        if sec == sector:
            print("\nBaños disponibles en el " + sector + ":")
            for baño in baños:
                print("- " + baño)
            # Solicitar baños funcionales válidos
            while True:
                baños_funcionales = input(
                    "Ingrese los baños funcionales separados por comas (o deje vacío si no hay ninguno): "
                ).split(", ")
                baños_funcionales = [baño.strip() for baño in baños_funcionales if baño.strip()]
                if all(baño in baños for baño in baños_funcionales) or not baños_funcionales:
                    sectores_afectados.append([sector, baños_funcionales])
                    break
                else:
                    print("No existe ese baño. Intente nuevamente.")
            break

# Obtener baños alternativos
baños_alternativos = obtener_banos_disponibles(sectores_afectados, sectores_baños)

# Verificar si no hay baños disponibles en ningún sector
no_hay_baños = all("No hay baños disponibles" in baños for _, baños in baños_alternativos)

# Imprimir resultados
if no_hay_baños:
    print("\nNo hay baños disponibles en el sector que abordamos")
else:
    print("\n¡Corte de agua en los siguientes sectores!")
    for afectado in sectores_afectados:
        print("- " + afectado[0])

    print("\nBaños disponibles:")
    for sector, baños in baños_alternativos:
        if "No hay baños disponibles" in baños:
            print(sector + ": No hay baños disponibles")
        else:
            print(sector + ": " + ", ".join(baños))

