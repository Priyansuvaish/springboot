from springboot.crew import SpringBootAgent  # Import the custom agent from crew.py
from dotenv import load_dotenv
import os
import sys

def run():
    # Initialize the SpringBootAgent
    agent = SpringBootAgent()

    # Example usage: Get user input for the project creation
    project_name = input("Enter the project name: ")
    package_name = input("Enter the package name (e.g., com.example): ")
    dependencies = input("Enter the dependencies (comma separated, e.g., web,jpa): ").split(',')
    java_version = input("Enter Java version (default 11): ") or '11'
    language = input("Enter language (java/kotlin, default java): ") or 'java'

    # Generate the Spring Boot project
    result = agent.generate_spring_boot_project(project_name, package_name, dependencies, java_version, language)
    print(result)
    
    load_dotenv()

    # Get the API contract path from the .env file
    api_contract_path = os.getenv('API_CONTRACT_PATH')
    print(api_contract_path)
    print(f"Resolved API contract path: {api_contract_path}")
    
    if not api_contract_path:
        print("Error: The environment variable 'API_CONTRACT_PATH' is not set in the .env file.")
        sys.exit(1)
    
    # Validate the file exists
    if not os.path.isfile(api_contract_path):
        print(f"Error: The file at path '{api_contract_path}' does not exist.")
        sys.exit(1)
    
    # Define inputs for the crew
    inputs = {
        'api_contract_path': api_contract_path
    }
    agent.crew().kickoff(inputs)
    

if __name__ == "__main__":
    run()
