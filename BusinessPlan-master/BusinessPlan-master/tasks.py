from crewai import Task

class CustomTasks:
    def __init__(self):
        pass

    def create_task(self, agent, business_type, task_type):
        task_descriptions = {
            "compreensao_negocio": (
                f"Compreender o negócio da empresa {business_type}, incluindo sua localização, posicionamento de marca, produtos e serviços, "
                f"e perfil de cliente ideal. Analise o site da empresa e outros materiais disponíveis para reunir essas informações."
            ),
            "analise_mercado": (
                f"Realizar uma análise de mercado detalhada para a empresa {business_type}, incluindo a busca de concorrentes, "
                f"estimativa do tamanho do mercado, análise SWOT e análise PESTEL."
            ),
            "ideias_inovadoras": (
                f"Criar uma lista de ideias inovadoras e viáveis para a empresa {business_type}, para lidar com a concorrência e melhorar a posição de mercado."
            ),
            "desenvolvimento_financeiro": (
                f"Desenvolver o eixo financeiro do mapa estratégico para a empresa {business_type}, alinhando os objetivos financeiros com as informações coletadas."
            ),
            "desenvolvimento_clientes": (
                f"Desenvolver o eixo de clientes do mapa estratégico para a empresa {business_type}. Definir segmentos de clientes, calcular ticket médio e volume necessário, "
                f"listar problemas e soluções para cada segmento, e definir os atributos necessários das soluções."
            ),
            "mapeamento_processos": (
                f"Mapear os departamentos e processos internos necessários para a empresa {business_type} funcionar, gerando os atributos que compõem as soluções para os segmentos de clientes."
            ),
            "desenvolvimento_estrutura": (
                f"Desenvolver o eixo de estrutura do mapa estratégico para a empresa {business_type}, determinando a estrutura física, equipamentos, conhecimento e tecnologia necessários para os processos internos."
            ),
            "desenvolvimento_projetos": (
                f"Desenvolver projetos detalhados para a implementação de ideias inovadoras na empresa {business_type}, com pelo menos 10 ações específicas cada."
            )
        }

        expected_outputs = {
            "compreensao_negocio": (
                f"Relatório detalhado sobre o negócio da empresa {business_type}, incluindo localização, posicionamento de marca, produtos e serviços, "
                f"e perfil de cliente ideal."
            ),
            "analise_mercado": (
                f"Relatório detalhado de análise de mercado para a empresa {business_type}, incluindo informações sobre concorrentes, tamanho do mercado, análise SWOT e análise PESTEL."
            ),
            "ideias_inovadoras": (
                f"Lista de ideias inovadoras e viáveis para a empresa {business_type}, com descrição detalhada de cada ideia."
            ),
            "desenvolvimento_financeiro": (
                f"Eixo financeiro do mapa estratégico para a empresa {business_type}, com objetivos financeiros detalhados."
            ),
            "desenvolvimento_clientes": (
                f"Eixo de clientes do mapa estratégico para a empresa {business_type}, incluindo definição de segmentos de clientes, ticket médio e volume necessário, problemas e soluções para cada segmento, e atributos necessários das soluções."
            ),
            "mapeamento_processos": (
                f"Mapa de processos internos da empresa {business_type}, detalhando os departamentos e processos necessários para gerar os atributos das soluções."
            ),
            "desenvolvimento_estrutura": (
                f"Eixo de estrutura do mapa estratégico para a empresa {business_type}, detalhando a estrutura física, equipamentos, conhecimento e tecnologia necessários."
            ),
            "desenvolvimento_projetos": (
                f"Projetos detalhados para a implementação de ideias inovadoras na empresa {business_type}, com pelo menos 10 ações específicas cada."
            )
        }

        return Task(
            description=task_descriptions[task_type],
            agent=agent,
            expected_output=expected_outputs[task_type]
        )
