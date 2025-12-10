from datos.conexion import Base, motor_db
from negocio import (
    registrar_usuario_negocio, 
    login_negocio,
    sincronizar_posts_api_db,
    listar_posts_locales,
    crear_post_nuevo,
    modificar_post_existente,
    eliminar_post_existente
)

def menu_principal():
    print("Iniciando sistema y verificando base de datos...")
    Base.metadata.create_all(motor_db)

    usuario_autenticado = False

    while True:
        print("\n" + "="*30)
        print("   SISTEMA DE GESTIÓN API")
        print("="*30)

        if not usuario_autenticado:
            print("1. Registrar Usuario (Encriptado)")
            print("2. Iniciar Sesión")
            print("0. Salir")
        else:
            print("--- Modulo de Posts (JSONPlaceholder) ---")
            print("3. Obtener Posts de API y guardar en la base de datos (GET)")
            print("4. Ver Posts guardados localmente")
            print("5. Crear nuevo Post en API (POST)")
            print("6. Modificar Post en API (PUT)")
            print("7. Eliminar Post en API (DELETE)")
            print("0. Cerrar Sesión / Salir")

        opcion = input("\nSeleccione una opción: ")

        try:
            if not usuario_autenticado:
                if opcion == "1":
                    u = input("Ingrese nuevo usuario: ")
                    p = input("Ingrese contraseña: ")
                    registrar_usuario_negocio(u, p)
                
                elif opcion == "2":
                    u = input("Usuario: ")
                    p = input("Contraseña: ")
                    if login_negocio(u, p):
                        usuario_autenticado = True
                
                elif opcion == "0":
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida.")

            else: 
                if opcion == "3":
                    sincronizar_posts_api_db()
                
                elif opcion == "4":
                    listar_posts_locales()

                elif opcion == "5":
                    print("\n--- Nuevo Post ---")
                    t = input("Título: ")
                    b = input("Contenido (Body): ")

                    codigo, resp = crear_post_nuevo(t, b, 1)
                    print(f"Resultado: {codigo} - {resp}")

                elif opcion == "6":
                    print("\n--- Modificar Post ---")
                    i = input("ID del Post a modificar: ")
                    t = input("Nuevo título: ")
                    modificar_post_existente(i, t)

                elif opcion == "7":
                    print("\n--- Eliminar Post ---")
                    i = input("ID del Post a eliminar: ")
                    eliminar_post_existente(i)

                elif opcion == "0":
                    print("Cerrando sesión...")
                    usuario_autenticado = False
                else:
                    print("Opción no válida.")
        
        except Exception as e:
            print(f"Ocurrió un error inesperado en el menú: {e}")

if __name__ == "__main__":
    menu_principal()