import hashlib

class Encriptador:
    @staticmethod
    def encriptar(texto):
        """Encripta una cadena usando SHA-256"""
        return hashlib.sha256(texto.encode()).hexdigest()

    @staticmethod
    def verificar(texto_plano, hash_guardado):
        """Compara un texto plano con un hash guardado"""
        hash_text = hashlib.sha256(texto_plano.encode()).hexdigest()
        return hash_text == hash_guardado