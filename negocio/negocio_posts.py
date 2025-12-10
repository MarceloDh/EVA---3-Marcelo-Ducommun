from modelos.modelos import Post
from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_todos_los_posts
from servicios.api_data import ClienteAPI 

cliente = ClienteAPI()

def sincronizar_posts_api_db():
    """
    Trae los posts de la API (JSON) y los guarda en la base de datos local (SQL).
    Cumple con: 'Los datos obtenidos se almacenarán en base de datos local'
    """
    print("--- Sincronizando datos con JSONPlaceholder ---")
    lista_json = cliente.obtener_posts()
    
    contador = 0
    for p_json in lista_json:
        nuevo_post = Post(
            id=p_json['id'],
            userId=p_json['userId'],
            title=p_json['title'],
            body=p_json['body']
        )
        if insertar_objeto(nuevo_post):
            contador += 1
            
    print(f"Proceso terminado. Se han guardado {contador} posts nuevos.")

def listar_posts_locales():
    """Muestra los posts que estan guardados en tu PC"""
    posts = obtener_todos_los_posts()
    print(f"\n--- Listando {len(posts)} Posts Locales ---")
    for p in posts:
        print(f"[{p.id}] {p.title[:50]}...")

def crear_post_nuevo(titulo, cuerpo, user_id):
    payload = {"title": titulo, "body": cuerpo, "userId": user_id}
    return cliente.enviar_post(payload)

def modificar_post_existente(id_post, nuevo_titulo):
    payload = {"id": id_post, "title": nuevo_titulo}
    return cliente.actualizar_post(id_post, payload)

def eliminar_post_existente(id_post):
    return cliente.eliminar_post(id_post)