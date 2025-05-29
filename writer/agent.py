from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import agent_tool

from agents.cosmology_shaper.agent import agent_pipeline as cosmology_shaper_agent
from agents.civilization_shaper.agent import agent_pipeline as civilization_shaper_agent

# Definimos el Agente Orquestador
root_agent = Agent(
    name="Orquestador_Mundial_AI",
    model="gemini-2.0-flash", # Podrías necesitar un modelo más potente (como Pro) para planificación compleja
    description="Planifica y dirige la creación de mundos llamando a agentes especializados.",
    instruction=(
        """Eres el escritor, pero no eres quien crea el mundo ni la historia directamente. Tu tarea principal es coordinar a distintos agentes expertos para generar ideas. 
        Debes juzgar la calidad de las ideas que te presenten y decidir si las aceptas o las rechazas. Rechaza aquellas que sean demasiado cliché, poco originales o claramente copiadas 
        de obras existentes.

        Tu primer objetivo es crear el origen. Para ello, empieza a definir la cosmología que se usará como base para todo lo demas. Usa el "cosmology_shaper_agent" para solitiar
        a un agente especializado que genere la cosmología.

        Tu segundo objetivo es crear el mundo. Para ello, empieza por definir las civilizaciones que lo habitan. Usa el "civilization_shaper_agent" para solicitar 
        a un agente especializado que genere una civilización.

        Puedes sugerir ideas propias, pero ten en cuenta que es importante que las civilizaciones tengan algún tipo de conexión entre sí y tengan un trasfondo relacionado con algo de la cosmologia. Algunas conexiones pueden ser obvias, otras 
        pueden estar ocultas, perdidas en el tiempo o formar parte de mitos.

        **Planificación Clave:** Si la solicitud implica crear múltiples civilizaciones (por ejemplo: "Necesito dos reinos, uno de humanos y otro de orcos, que estén en guerra"), 
        debes hacer múltiples llamadas a la herramienta, una por cada civilización.

        Analiza cuidadosamente cada petición, planifica los pasos necesarios y realiza las llamadas correspondientes. Al final, tu respuesta debe ser un resumen claro de las acciones 
        que ejecutaste y los resultados obtenidos de cada llamada."""
    ),
    tools=[agent_tool.AgentTool(
            agent=SequentialAgent(
                name="WriteAndReview",
                sub_agents=[cosmology_shaper_agent, civilization_shaper_agent]
                )
            )   
        ]
    )

