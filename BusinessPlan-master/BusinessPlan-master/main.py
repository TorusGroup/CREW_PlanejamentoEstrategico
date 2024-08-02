import os
from crewai import Crew, Process, Task
from agents import CustomAgents
from tasks import CustomTasks

# Configurar variáveis de ambiente
os.environ["OPENAI_API_KEY"] = "sk-proj-7XuthSfnz2BgolGAc7A9T3BlbkFJF4kPfNT1fkvmCZbPNUxJ"

class BusinessAutomationCrew:
    def __init__(self, business_type, site_url, current_revenue, financial_goal):
        self.business_type = business_type
        self.site_url = site_url
        self.current_revenue = current_revenue
        self.financial_goal = financial_goal
        self.agents = CustomAgents()
        self.tasks = CustomTasks()

    def run(self):
        agents = {
            "analista_negocios": self.agents.create_agent("Analista de Negócios"),
            "analista_mercado": self.agents.create_agent("Analista de Mercado"),
            "consultor_inovacao": self.agents.create_agent("Consultor de Inovação"),
            "estrategia_financeira": self.agents.create_agent("Estratégia Financeira"),
            "especialista_clientes": self.agents.create_agent("Especialista em Clientes"),
            "analista_processos": self.agents.create_agent("Analista de Processos"),
            "consultor_estrutura": self.agents.create_agent("Consultor de Estrutura"),
            "diretor_consultoria": self.agents.create_agent("Diretor da Consultoria")
        }

        tasks = {
            "compreensao_negocio": self.tasks.create_task(agents["analista_negocios"], self.business_type, "compreensao_negocio"),
            "analise_mercado": self.tasks.create_task(agents["analista_mercado"], self.business_type, "analise_mercado"),
            "ideias_inovadoras": self.tasks.create_task(agents["consultor_inovacao"], self.business_type, "ideias_inovadoras"),
            "desenvolvimento_financeiro": self.tasks.create_task(agents["estrategia_financeira"], self.business_type, "desenvolvimento_financeiro"),
            "desenvolvimento_clientes": self.tasks.create_task(agents["especialista_clientes"], self.business_type, "desenvolvimento_clientes"),
            "mapeamento_processos": self.tasks.create_task(agents["analista_processos"], self.business_type, "mapeamento_processos"),
            "desenvolvimento_estrutura": self.tasks.create_task(agents["consultor_estrutura"], self.business_type, "desenvolvimento_estrutura"),
            "desenvolvimento_projetos": self.tasks.create_task(agents["consultor_inovacao"], self.business_type, "desenvolvimento_projetos")
        }

        crew = Crew(
            agents=list(agents.values()),
            tasks=list(tasks.values()),
            process=Process.sequential,
            verbose=False
        )

        # Adiciona lógica de validação após cada tarefa
        results = crew.kickoff()

        for task_name, result in results.items():
            agent = tasks[task_name].agent
            director = agents["diretor_consultoria"]
            print(f"{director.role} está validando a tarefa '{task_name}' realizada por {agent.role}")
            # Aqui você pode adicionar lógica para feedback ou correções

        return results

if __name__ == "__main__":
    print("Bem-vindo à Configuração da Equipe de Automação Empresarial")
    print("------------------------------------------------")
    business_type = input("Qual é o tipo de negócio da empresa? ").strip()
    site_url = input("Qual é o site da empresa? ").strip()
    current_revenue = input("Qual é o faturamento atual da empresa? ").strip()
    financial_goal = input("Qual é o objetivo financeiro da empresa? ").strip()

    automation_crew = BusinessAutomationCrew(business_type, site_url, current_revenue, financial_goal)
    business_plan = automation_crew.run()

    print("\n\n########################")
    print("## Aqui estão os resultados do seu projeto de automação empresarial:")
    print("########################\n")
    print(business_plan)
