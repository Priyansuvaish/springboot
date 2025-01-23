import zipfile
import os

def extract_zip(zip_path, extract_to):
    """
    Extracts the Spring Boot project ZIP file to the specified location.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return f"Project extracted to {extract_to}"
    except Exception as e:
        return f"Error extracting ZIP file: {e}"

def clean_up(zip_path):
    """
    Clean up the ZIP file after extraction.
    """
    try:
        if os.path.exists(zip_path):
            os.remove(zip_path)
        return f"Cleaned up file: {zip_path}"
    except Exception as e:
        return f"Error cleaning up file: {e}"
