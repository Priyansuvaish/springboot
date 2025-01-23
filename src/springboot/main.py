from springboot.crew import SpringBootAgent  # Import the custom agent from crew.py

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

if __name__ == "__main__":
    run()
