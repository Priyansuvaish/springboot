import requests
import zipfile
import yaml
import os

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool
@CrewBase
class SpringBootAgent:
    def __init__(self):
        self.base_url = "https://start.spring.io/starter.zip"
        self.state = {}
        with open("E:/projecttest/code-generation-using-agents/springboot/src/springboot/config/agents.yaml", "r") as agents_file:
            self.agents_config = yaml.safe_load(agents_file)
        
        with open("E:/projecttest/code-generation-using-agents/springboot/src/springboot/config/tasks.yaml", "r") as tasks_file:
            self.tasks_config = yaml.safe_load(tasks_file)

        # Debugging: Print loaded configurations
        print("Loaded Agents Config:", self.agents_config)
        print("Loaded Tasks Config:", self.tasks_config)

    @agent
    def tech_lead(self) -> Agent:
        if 'tech_lead' not in self.agents_config:
            raise KeyError("Missing configuration for 'tech_lead' in agents_config.")
        return Agent(
            config=self.agents_config['tech_lead'],
            allow_delegation=True,
            verbose=True,
            tools=[FileReadTool(file_path='E:/projecttest/code-generation-using-agents/springboot/openapi.yaml')],
            memory=False
        )
    @task
    def parse_api_contract(self) -> Task:
        if 'parse_api_contract' not in self.tasks_config:
            raise KeyError("Missing configuration for 'parse_api_contract' in tasks_config.")
        return Task(
            config=self.tasks_config['parse_api_contract'],
            agent=self.tech_lead()
        )
    def generate_spring_boot_project(self, project_name, package_name, dependencies, java_version='11', language='java', build_type='maven'):
        params = {
            'type': f'{build_type}-project',
            'language': language,
            'javaVersion': java_version,
            'dependencies': ','.join(dependencies),
            'artifactId': project_name,
            'groupId': package_name,
        }

        print(params)
        response = requests.get(self.base_url, params=params)
        # print("Response Status Code:", response.status_code)
        # print("Response Content:", response.text)

        if response.status_code == 200:
            zip_file_path = f'{project_name}.zip'
            with open(f'{project_name}.zip', 'wb') as file:
                file.write(response.content)
            self.unzip_file(zip_file_path, project_name)
            return f"Spring Boot project {project_name} created successfully!"
        else:
            return "Failed to create Spring Boot project. Please check your inputs."
    
    def unzip_file(self, zip_file_path, extract_folder):
        # Create the folder where the contents will be extracted
        if not os.path.exists(extract_folder):
            os.makedirs(extract_folder)

        # Unzip the file into the specified folder
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        
        # Remove the original ZIP file after extracting
        os.remove(zip_file_path)
        print(f"Unzipped the project to: {extract_folder}")
        self.state[zip_file_path]=extract_folder
    @crew
    def crew(self) -> Crew:
        """Creates the LatestAiDevelopment crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
        
