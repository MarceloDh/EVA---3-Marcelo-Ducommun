import requests

class ClienteAPI:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def obtener_posts(self):
        """
        GET: Obtiene los posts desde la API.
        Requisito: 'Solicitar la obtención de datos desde la API'
        """
        try:
            url = f"{self.base_url}/posts"
            print(f"Consultando GET {url}...")
            
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                datos = respuesta.json()
                print(f"¡Éxito! Se obtuvieron {len(datos)} posts.")
                return datos
            else:
                print(f"Error en la solicitud GET. Código: {respuesta.status_code}")
                return []
        except requests.exceptions.RequestException as e:
            print(f"Error grave de conexión: {e}")
            return []

    def enviar_post(self, post_data):
        """
        POST: Envía datos para 'crear' un recurso.
        Requisito: 'Debe retornar una respuesta 200/201'
        """
        try:
            url = f"{self.base_url}/posts"
            print(f"Enviando POST a {url} con datos: {post_data}")
            
            respuesta = requests.post(url, json=post_data)
            
            if respuesta.status_code in [200, 201]:
                print("¡POST exitoso!")
                return respuesta.status_code, respuesta.json()
            else:
                print(f"Fallo en POST. Código: {respuesta.status_code}")
                return respuesta.status_code, {}
        except Exception as e:
            print(f"Error al enviar POST: {e}")
            return 500, {}

    def actualizar_post(self, id_post, nuevos_datos):
        """
        PUT: Actualiza un recurso existente.
        Requisito: 'Esta haciendo agregado el ID del objeto a la URL'
        """
        try:
            url = f"{self.base_url}/posts/{id_post}"
            print(f"Enviando PUT a {url}...")
            
            respuesta = requests.put(url, json=nuevos_datos)
            
            if respuesta.status_code == 200:
                print(f"¡PUT exitoso para el ID {id_post}!")
                return True
            else:
                print(f"Fallo en PUT. Código: {respuesta.status_code}")
                return False
        except Exception as e:
            print(f"Error al enviar PUT: {e}")
            return False

    def eliminar_post(self, id_post):
        """
        DELETE: Elimina un recurso.
        Requisito: 'Ingresar el ID del objeto a eliminar y agregarlo a la URL'
        """
        try:
            url = f"{self.base_url}/posts/{id_post}"
            print(f"Enviando DELETE a {url}...")
            
            respuesta = requests.delete(url)
            
            if respuesta.status_code == 200:
                print(f"¡DELETE exitoso para el ID {id_post}!")
                return True
            else:
                print(f"Fallo en DELETE. Código: {respuesta.status_code}")
                return False
        except Exception as e:
            print(f"Error al enviar DELETE: {e}")
            return False