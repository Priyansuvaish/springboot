import requests
import zipfile
import os

class SpringBootAgent:
    def __init__(self):
        self.base_url = "https://start.spring.io/starter.zip"

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
        print("Response Status Code:", response.status_code)
        print("Response Content:", response.text)

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
