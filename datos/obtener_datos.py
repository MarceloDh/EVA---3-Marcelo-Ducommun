from datos.conexion import sesion
from modelos.modelos import Usuario, Post

def obtener_usuario_por_username(username_buscado):
    """Busca un usuario por su nombre de usuario (para Login)"""
    resultado = sesion.query(Usuario).filter(Usuario.username == username_buscado).first()
    return resultado

def obtener_todos_los_posts():
    """Devuelve todos los posts guardados en la BD"""
    resultados = sesion.query(Post).all()
    return resultados

def obtener_post_por_id(id_post):
    """Busca un post específico"""
    return sesion.query(Post).filter(Post.id == id_post).first()