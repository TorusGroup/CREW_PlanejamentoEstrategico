import os
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks

# Set up environment variables
os.environ["OPENAI_API_KEY"] = "sk-proj-7XuthSfnz2BgolGAc7A9T3BlbkFJF4kPfNT1fkvmCZbPNUxJ"

class BusinessAutomationCrew:
    def __init__(self, business_type):
        self.business_type = business_type
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
            "consultor_estrutura": self.agents.create_agent("Consultor de Estrutura")
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
            verbose=False
        )

        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Business Automation Crew Setup")
    print("------------------------------------------------")
    business_type = input("What business do you seek to build today? ").strip()

    automation_crew = BusinessAutomationCrew(business_type)
    business_plan = automation_crew.run()

    print("\n\n########################")
    print("## Here are the results of your business automation project:")
    print("########################\n")
    print(business_plan)
