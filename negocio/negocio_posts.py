from modelos.modelos import Post
from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_todos_los_posts
from servicios.api_data import ClienteAPI 

cliente = ClienteAPI()

def sincronizar_posts_api_db():
    print("--- Sincronizando datos con JSONPlaceholder ---")
    lista_json = cliente.obtener_posts()
    
    contador = 0
    if lista_json:
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
    posts = obtener_todos_los_posts()
    print(f"\n--- Listando {len(posts)} Posts Locales ---")
    
    if not posts:
        print("No hay posts guardados en la base de datos local.")
        return

    for p in posts:
        titulo_corto = (p.title[:50] + '..') if len(p.title) > 50 else p.title
        print(f"[{p.id}] {titulo_corto}")

def crear_post_nuevo(titulo, cuerpo, user_id):
    payload = {"title": titulo, "body": cuerpo, "userId": user_id}
    
    codigo, respuesta_api = cliente.enviar_post(payload)
    
    if codigo in [200, 201]:
        print("API respondió correctamente. Guardando respaldo local...")
        
        nuevo_post_local = Post(
            userId=respuesta_api['userId'],
            title=respuesta_api['title'],
            body=respuesta_api['body']
        )
        
        insertar_objeto(nuevo_post_local)
        
    return codigo, respuesta_api

def modificar_post_existente(id_post, nuevo_titulo):
    payload = {"id": id_post, "title": nuevo_titulo}
    return cliente.actualizar_post(id_post, payload)

def eliminar_post_existente(id_post):
    return cliente.eliminar_post(id_post)