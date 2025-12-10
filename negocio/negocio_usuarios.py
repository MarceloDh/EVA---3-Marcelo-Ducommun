from modelos.modelos import Usuario
from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_usuario_por_username
from auxiliares.seguridad import Encriptador

def registrar_usuario_negocio(username, password):
    """
    Lógica para registrar un usuario:
    1. Verifica si ya existe.
    2. Encripta la contraseña.
    3. Lo manda a guardar a la BD.
    """
    if obtener_usuario_por_username(username):
        print(f"Error: El usuario '{username}' ya existe.")
        return False

    pass_encriptada = Encriptador.encriptar(password)
    
    nuevo_usuario = Usuario(username=username, password=pass_encriptada)

    id_creado = insertar_objeto(nuevo_usuario)
    
    if id_creado:
        print(f"¡Usuario {username} registrado con éxito!")
        return True
    return False

def login_negocio(username, password):
    """
    Lógica de inicio de sesión:
    1. Busca el usuario.
    2. Compara contraseñas (Hash vs Hash).
    """
    usuario_db = obtener_usuario_por_username(username)
    
    if usuario_db:
        if Encriptador.verificar(password, usuario_db.password):
            print(f"¡Bienvenido al sistema, {username}!")
            return True
        else:
            print("Error: Contraseña incorrecta.")
    else:
        print("Error: Usuario no encontrado.")
    
    return False