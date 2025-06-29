def datos_gabriel():
    print("Mi nombre es Gabriel y tengo 20 años.")
def datos_mauricio():
    print("Mi nombre es Mauricio y tengo 29 años.")

# Menú base del programa
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de Gabriel")
    print("2. Función de Mauricio")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        datos_gabriel() # Aquí se llamará a la función del integrante 1
    elif op == "2":
        datos_mauricio() # Aquí se llamará a la función del integrante 2
    else:
        print(" Opción inválida.")
