from crewai import Agent
from langchain_openai import ChatOpenAI, ScrapeWebsiteTool

class CustomAgents:
    def __init__(self):
        self.gpt_model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

    def create_agent(self, role):
        descriptions = {
            "Analista de Negócios": "Compreender o negócio da empresa, incluindo localização, posicionamento de marca, produtos e serviços, perfil de cliente ideal.",
            "Analista de Mercado": "Realizar análise de mercado, incluindo busca de concorrentes, estimativa do tamanho do mercado, análise SWOT, análise PESTEL.",
            "Consultor de Inovação": "Criar uma lista de ideias inovadoras e viáveis para lidar com a concorrência.",
            "Estratégia Financeira": "Desenvolver o eixo financeiro do mapa estratégico com objetivos fornecidos.",
            "Especialista em Clientes": "Definir segmentos de clientes, calcular ticket médio, volume necessário, listar problemas e soluções, definir atributos necessários.",
            "Analista de Processos": "Mapear departamentos e processos internos necessários.",
            "Consultor de Estrutura": "Determinar a estrutura física, equipamentos, conhecimento e tecnologia necessários.",
            "Diretor da Consultoria": "Supervisionar todo o processo de planejamento estratégico e validar os resultados de cada agente para garantir a qualidade."
        }

        return Agent(
            role=role,
            backstory=descriptions[role],
            goal=f"Supervisionar e validar os resultados como {role}.",
            verbose=True,
            llm=self.gpt_model
        )

# Exemplos de uso
if __name__ == "__main__":
    custom_agents = CustomAgents()
    analista_negocios = custom_agents.create_agent("Analista de Negócios")
    analista_mercado = custom_agents.create_agent("Analista de Mercado")
    consultor_inovacao = custom_agents.create_agent("Consultor de Inovação")
    estrategia_financeira = custom_agents.create_agent("Estratégia Financeira")
    especialista_clientes = custom_agents.create_agent("Especialista em Clientes")
    analista_processos = custom_agents.create_agent("Analista de Processos")
    consultor_estrutura = custom_agents.create_agent("Consultor de Estrutura")
    diretor_consultoria = custom_agents.create_agent("Diretor da Consultoria")

    # Exemplos de agentes criados
    print(analista_negocios)
    print(analista_mercado)
    print(consultor_inovacao)
    print(estrategia_financeira)
    print(especialista_clientes)
    print(analista_processos)
    print(consultor_estrutura)
    print(diretor_consultoria)
