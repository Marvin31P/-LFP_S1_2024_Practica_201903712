import file_handler
from pet_manager import PetManager

def main_menu():
    print("=== Menú Principal ===")
    print("1. Módulo PetManager")
    print("2. Salir")

def pet_manager_menu():
    print("=== Menú PetManager ===")
    print("1. Crear Gato")
    print("2. Dar de Comer")
    print("3. Jugar")
    print("4. Resumen Mascota")
    print("5. Resumen Global")
    print("6. Cargar Archivo")
    print("7. Salir")

def main():
    print("Bienvenido al Programa de Gestión de Mascotas")

    pet_manager = PetManager()

    while True:
        main_menu()
        choice = input("Seleccione una opción: ")

        if choice == '1':
            while True:
                pet_manager_menu()
                pet_choice = input("Seleccione una opción de PetManager: ")

                if pet_choice == '1':
                    name = input("Ingrese el nombre del gato: ")
                    pet_manager.create_pet(name)
                elif pet_choice == '2':
                    name = input("Ingrese el nombre del gato: ")
                    weight = int(input("Ingrese el peso del ratón: "))
                    if not pet_manager.feed_pet(name, weight):
                        print("No se encontró la mascota.")
                elif pet_choice == '3':
                    name = input("Ingrese el nombre del gato: ")
                    time = int(input("Ingrese el tiempo de juego en minutos: "))
                    if not pet_manager.play_with_pet(name, time):
                        print("No se encontró la mascota.")
                elif pet_choice == '4':
                    name = input("Ingrese el nombre del gato: ")
                    summary = pet_manager.get_pet_summary(name)
                    if summary:
                        print(summary)
                    else:
                        print("No se encontró la mascota.")
                elif pet_choice == '5':
                    for summary in pet_manager.get_global_summary():
                        print(summary)
                elif pet_choice == '6':
                    file_path = input("Ingrese la ruta del archivo .petmanager: ")
                    commands = file_handler.read_pet_manager_file(file_path)
                    for command in commands:
                        pass
                elif pet_choice == '7':
                    break
                else:
                    print("Opción no válida")
        elif choice == '2':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()