from typing import Dict

from agents.civilization_shaper.agent import root_agent as civilization_shaper_agent

def call_civilization_shaper_agent_tool(instruction_for_civilization_shaper: str) -> Dict:
    """
    Invoca al Agente Forjador de Civilizaciones para crear o modificar
    una civilización de fantasía. Actúa como un puente hacia
    el agente especializado.

    Args:
        instruction_for_civilization_shaper (str): La instrucción detallada
            para el Agente Forjador de Civilizaciones.

    Returns:
        Dict: Un diccionario con el estado y la respuesta del Agente Forjador de Civilizaciones.
    """
    if not civilization_shaper_agent:
        return {"status": "error", "message": "El Agente Forjador de Civilizaciones no está disponible."}

    if not instruction_for_civilization_shaper:
        return {"status": "error", "message": "Se necesita una instrucción para el Agente Forjador de Civilizaciones."}

    try:
        print(f"\n>>> Orquestador: Enviando tarea al Forjador de Civilizaciones -> '{instruction_for_civilization_shaper}'")
        # Aquí es donde el orquestador llama al otro agente
        response = civilization_shaper_agent(instruction=instruction_for_civilization_shaper) # <-- PRUEBA ESTE
        print(f"<<< Forjador de Civilizaciones: Tarea completada.")
        return {
            "status": "success",
            "message": "Agente Forjador de Civilizaciones ejecutado con éxito.",
            "historian_response": response
            }

    except Exception as e:
        print(f"!!! Error al llamar al Agente Forjador de Civilizaciones: {e}")
        return {
            "status": "error",
            "message": f"Ocurrió un error al ejecutar el Agente Forjador de Civilizaciones: {e}"
            }