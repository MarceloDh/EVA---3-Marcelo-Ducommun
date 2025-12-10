from datos.conexion import sesion

def insertar_objeto(objeto):
    """Recibe un objeto (Usuario, Post, etc.) y lo guarda en la base de datos"""
    try:
        sesion.add(objeto)
        sesion.commit()
        sesion.refresh(objeto) 
        print(f"Objeto guardado correctamente: {objeto}")
        return objeto.id
    except Exception as error:
        sesion.rollback() 
        print(f"Error al guardar el objeto: {error}")
        return None