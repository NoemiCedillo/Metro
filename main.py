from modules.pintar import imprimir_mapa, imprimir_menu, imprimir_estaciones, pintar_info, pintar_trayectoria
from modules.sacar_distancias import obtener_datos, obtener_tiempo, sacar_estaciones_destino

def main():
    opcion = 'Z'
    while opcion != 'D':
        imprimir_menu()
        opcion = input("\nIngresa tu opción: ")
        if opcion == 'A':
            imprimir_mapa(obtener_datos())
        elif opcion == 'B':
            imprimir_estaciones(obtener_datos())
        elif opcion == 'C':
            origen = input('Escribe la estación Origen: ').lower()
            destino = input('Escribe la estación Destino: ').lower()
            lista_estaciones = sacar_estaciones_destino(origen,destino)
            tiempo1, tiempo2, minutos, tiempo_entre_estacion = obtener_tiempo(lista_estaciones)
            pintar_info(origen,destino,tiempo1, tiempo2, minutos)
            pintar_trayectoria(lista_estaciones, tiempo_entre_estacion, obtener_datos())

if __name__ == '__main__':
    main()