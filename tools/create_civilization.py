from typing import Optional, Dict, List

def create_fantasy_civilization(
    world_setting: Optional[str] = None,
    seed_idea: Optional[str] = None,
    originality_level: int = 4, # Nivel de 1 (Clásico) a 5 (Muy Original)
    avoid_tropes: Optional[List[str]] = None,
) -> Dict:
    """
    Construye el prompt para generar una civilización de fantasía y lo devuelve.

    Args:
        world_setting (Optional[str]): Descripción del mundo para contexto.
        seed_idea (Optional[str]): Idea inicial o palabra clave.
        originality_level (int): Nivel de originalidad deseado.
        avoid_tropes (Optional[List[str]]): Lista de clichés a evitar.

    Returns:
        Dict: Un diccionario con el estado y el prompt generado.
    """

    # --- Construcción del Prompt ---
    prompt_lines = []

    # 1. Establecer el Rol y Objetivo Principal
    prompt_lines.append(
        "Eres Aethelgard, el Forjador de Pueblos, un experto historiador y creador "
        "de mundos de fantasía. Tu tarea es generar la descripción detallada y "
        "VIBRANTE de una civilización o pueblo único para un mundo de fantasía."
    )

    # 2. Instrucciones sobre Originalidad
    originality_map = {
        1: "Puedes basarte bastante en tropos clásicos, pero dales un toque distintivo.",
        2: "Busca una mezcla equilibrada entre lo familiar y lo nuevo.",
        3: "Intenta desviarte significativamente de los clichés habituales.",
        4: "Prioriza la originalidad. Si usas un tropo, subviértelo o combínalo de forma inesperada.",
        5: "Busca la máxima originalidad. Explora conceptos extraños, abstractos o radicalmente diferentes."
    }
    prompt_lines.append(
        f"Nivel de Originalidad Deseado ({originality_level}/5): "
        f"{originality_map.get(originality_level, originality_map[4])}"
    )

    # 3. Incorporar Contexto del Mundo (si existe)
    if world_setting:
        prompt_lines.append(
            f"\nCONTEXTO DEL MUNDO (Tenlo muy en cuenta): {world_setting}"
        )

    # 4. Incorporar Idea Semilla (si existe)
    if seed_idea:
        prompt_lines.append(
            f"\nIDEA SEMILLA (Úsala como inspiración principal): {seed_idea}"
        )

    # 5. Incorporar Tropos a Evitar (si existen)
    if avoid_tropes:
        tropes_str = ", ".join(avoid_tropes)
        prompt_lines.append(
            f"\nEVITA ESTRICTAMENTE (o subvierte radicalmente) los siguientes "
            f"clichés: {tropes_str}"
        )

    # 6. Definir la Estructura de Salida Obligatoria
    prompt_lines.append(
        "\nESTRUCTURA OBLIGATORIA en formato markdown de salida (Cubre todos estos puntos con detalle):"
        "\n- **Nombre:** (Nombre propio y cómo los llaman otros)"
        "\n- **Concepto Central:** (La 'idea gancho' en 1-2 frases)"
        "\n- **Entorno y Hogar:** (Dónde viven y cómo les afecta)"
        "\n- **Apariencia/Biología:** (Si son distintos o tienen rasgos comunes)"
        "\n- **Estructura Social y Política:** (Jerarquía, gobierno, familia)"
        "\n- **Cultura y Creencias:** (Valores, mitos, religión, arte, costumbres)"
        "\n- **Tecnología y Magia:** (Nivel, uso, relación entre ambas)"
        "\n- **Economía:** (Recursos, subsistencia, comercio)"
        "\n- **Capacidad Militar/Defensa:** (Cómo se protegen o atacan)"
        "\n- **Relaciones Exteriores:** (Cómo interactúan con otros)"
        "\n- **El Giro Original:** (Resume qué los hace *realmente* únicos y diferentes)"
    )

    # 7. Instrucción Final
    prompt_lines.append(
        "\nSé creativo, evocador y asegúrate de que todos los aspectos de la "
        "civilización estén interconectados de forma lógica (dentro de la fantasía). "
        "¡Sorpréndeme con tu creación!"
    )

    final_prompt = "\n".join(prompt_lines)

    # --- Fin de la Construcción ---

    return {
        "status": "success",
        "prompt": final_prompt,
        "message": "Prompt generado con éxito. Listo para la generación."
    }