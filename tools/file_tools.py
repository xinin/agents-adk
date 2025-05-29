import os
from typing import Dict, List

# Define un directorio base para todas las salidas.
BASE_DIRECTORY = "outputs"

# --- Herramientas Genéricas para la Gestión de Entidades ---

def save_entity_file_tool(entity_type: str, filename: str, content: str) -> Dict:
    """
    Guarda el contenido de una entidad en un fichero, dentro de su
    subdirectorio específico (definido por 'entity_type').
    Crea el directorio si no existe y asegura la extensión '.md'.

    Args:
        entity_type (str): El tipo de entidad (ej: 'civilizaciones', 'cosmologia').
        filename (str): El nombre del fichero para la entidad.
        content (str): El contenido a guardar.

    Returns:
        Dict: Estado y mensaje de la operación.
    """
    try:
        if not entity_type:
            return {"status": "error", "message": "Error: Se debe especificar 'entity_type'."}
        if not content:
            return {"status": "error", "message": "Error: No se proporcionó contenido para guardar."}
        if not filename:
            return {"status": "error", "message": "Error: No se proporcionó nombre de fichero."}

        # Asegurar extensión .md
        if not filename.lower().endswith('.md'):
            filename += '.md'

        # Construir directorio de destino
        target_directory = os.path.join(BASE_DIRECTORY, entity_type)
        if not os.path.exists(target_directory):
            print(f"Creando directorio: {target_directory}")
            os.makedirs(target_directory)

        # Construir ruta completa
        full_path = os.path.join(target_directory, filename)

        # Escribir
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return {
            "status": "success",
            "message": f"Entidad '{filename}' guardada exitosamente en '{full_path}'."
        }

    except Exception as e:
        return {"status": "error", "message": f"Ocurrió un error inesperado al guardar: {e}"}

def list_entities_tool(entity_type: str) -> Dict:
    """
    Lista los ficheros existentes para un tipo de entidad específico.

    Args:
        entity_type (str): El tipo de entidad a listar (ej: 'civilizaciones').

    Returns:
        Dict: Estado, mensaje y lista de ficheros ('files').
    """
    try:
        if not entity_type:
            return {"status": "error", "message": "Error: Se debe especificar 'entity_type'."}

        target_directory = os.path.join(BASE_DIRECTORY, entity_type)
        if not os.path.exists(target_directory):
            return {"status": "info", "message": f"El directorio '{target_directory}' no existe.", "files": []}

        files = [
            f for f in os.listdir(target_directory)
            if os.path.isfile(os.path.join(target_directory, f))
            and f.lower().endswith('.md') # Mantenemos .md como estándar
        ]

        if not files:
            return {"status": "info", "message": f"No hay entidades tipo '{entity_type}'.", "files": []}

        return {"status": "success", "message": f"Encontradas {len(files)} entidades '{entity_type}'.", "files": files}

    except Exception as e:
        return {"status": "error", "message": f"Error al listar entidades: {e}", "files": []}

def read_entity_file_tool(entity_type: str, filename: str) -> Dict:
    """
    Lee el contenido de un fichero de entidad específico.

    Args:
        entity_type (str): El tipo de entidad.
        filename (str): El nombre del fichero a leer.

    Returns:
        Dict: Estado, mensaje y contenido ('content').
    """
    try:
        if not entity_type:
            return {"status": "error", "message": "Error: Se debe especificar 'entity_type'."}
        if not filename:
            return {"status": "error", "message": "Error: No se proporcionó nombre de fichero."}

        target_directory = os.path.join(BASE_DIRECTORY, entity_type)
        full_path = os.path.join(target_directory, filename)

        if not os.path.isfile(full_path):
            return {"status": "error", "message": f"Error: '{filename}' no encontrado en '{target_directory}'."}

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        return {"status": "success", "message": f"Contenido de '{filename}' leído.", "content": content}

    except Exception as e:
        return {"status": "error", "message": f"Error al leer '{filename}': {e}", "content": None}

def delete_entity_file_tool(entity_type: str, filename: str) -> Dict:
    """
    Borra un fichero de entidad específico.

    Args:
        entity_type (str): El tipo de entidad.
        filename (str): El nombre del fichero a borrar.

    Returns:
        Dict: Estado y mensaje.
    """
    try:
        if not entity_type:
            return {"status": "error", "message": "Error: Se debe especificar 'entity_type'."}
        if not filename:
            return {"status": "error", "message": "Error: No se proporcionó nombre de fichero."}

        target_directory = os.path.join(BASE_DIRECTORY, entity_type)
        full_path = os.path.join(target_directory, filename)

        if os.path.isfile(full_path):
            os.remove(full_path)
            return {"status": "success", "message": f"'{filename}' borrado de '{target_directory}'."}
        elif os.path.exists(full_path):
            return {"status": "error", "message": f"Error: '{filename}' no es un fichero."}
        else:
            return {"status": "info", "message": f"'{filename}' no encontrado, no se borró nada."}

    except Exception as e:
        return {"status": "error", "message": f"Error al borrar '{filename}': {e}"}

def edit_entity_file_tool(entity_type: str, filename: str, new_content: str) -> Dict:
    """
    Edita (sobrescribe) el contenido de un fichero de entidad existente.

    Args:
        entity_type (str): El tipo de entidad.
        filename (str): El nombre del fichero a editar.
        new_content (str): El nuevo contenido completo.

    Returns:
        Dict: Estado y mensaje.
    """
    try:
        if not entity_type:
            return {"status": "error", "message": "Error: Se debe especificar 'entity_type'."}
        if not filename:
            return {"status": "error", "message": "Error: No se proporcionó nombre de fichero."}
        if not new_content:
            return {"status": "error", "message": "Error: No se proporcionó 'new_content'."}

        target_directory = os.path.join(BASE_DIRECTORY, entity_type)
        full_path = os.path.join(target_directory, filename)

        if not os.path.isfile(full_path):
            return {"status": "error", "message": f"Error: '{filename}' no existe en '{target_directory}'. No se puede editar."}

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return {"status": "success", "message": f"'{filename}' editado exitosamente en '{target_directory}'."}

    except Exception as e:
        return {"status": "error", "message": f"Ocurrió un error al editar '{filename}': {e}"}