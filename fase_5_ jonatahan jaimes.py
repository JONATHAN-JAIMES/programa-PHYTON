"""
Fase 5 - Evaluación Final POA
Curso: Fundamentos de Programación (213022)
Problema 1: Nivel de compromiso de sesiones de clientes
"""
 
# Constantes de la lógica de negocio
DURACION_ALTA = 180   # segundos
CLICS_ALTOS = 8
DURACION_BAJA = 60    # segundos
CLICS_BAJOS = 3
 
 
def clasificar_compromiso(duracion, clics):
    """Recibe la duración (segundos) y el número de clics de una sesión
    y devuelve 'Alto', 'Bajo' o 'Medio'."""
    if duracion > DURACION_ALTA and clics > CLICS_ALTOS:
        return "Alto"
    elif duracion < DURACION_BAJA or clics < CLICS_BAJOS:
        return "Bajo"
    else:
        return "Medio"
 
 
def mostrar_informe(sesiones):
    """Recorre la matriz y muestra el ID del cliente con su clasificación."""
    print("=" * 40)
    print("   INFORME DE COMPROMISO DE SESIONES")
    print("=" * 40)
    print(f"{'ID Cliente':<12}{'Compromiso':<12}")
    print("-" * 40)
    for fila in sesiones:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]
        nivel = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<12}{nivel:<12}")
    print("=" * 40)
 
 
# Matriz: [ID del Cliente, Duración (segundos), Número de clics]
sesiones = [
    [101, 240, 12],   # Alto
    [102, 45, 10],    # Bajo (duración < 60)
    [103, 120, 5],    # Medio
    [104, 300, 2],    # Bajo (clics < 3)
    [105, 181, 9],    # Alto
    [106, 180, 8],    # Medio (justo en el límite, no supera)
]
 
mostrar_informe(sesiones)