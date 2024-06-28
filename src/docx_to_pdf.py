from dotenv import load_dotenv
import os
import requests
import logging

class DocxToPdf:
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv("/home/j/pypractice/.venv/.env")

        self.base_url = "https://api.apyhub.com/convert/word-file/pdf-file"
        self.api_token = os.getenv("APYHUB_TOKEN")
        print(f"TOKEN: {self.api_token}")
        # self.session = requests.Session()

    def convert_file(self, file_path, file_name_docx, file_name_pdf):
        """
        Converts the DOCX file to PDF via 3rd-party API.

        Args:
            file_path (str): The file's path and name.

        Returns:
            dict: A dictionary containing the project details.
        """
        try:
            import http.client as http_client
        except ImportError:
            # Python 2
            import httplib2 as http_client
        http_client.HTTPConnection.debuglevel = 1

        try:
            self.file_path = file_path
            self.file_name_docx = file_name_docx
            self.file_name_pdf = file_name_pdf

            # Initialize logging.
            # logging.basicConfig()
            # logging.getLogger().setLevel(logging.DEBUG)
            # requests_log = logging.getLogger("requests.packages.urllib3")
            # requests_log.setLevel(logging.DEBUG)
            # requests_log.propagate = True

            headers = {"apy-token": self.api_token,}
            # headers = {"apy-token": self.api_token, "content-type": "multipart/form-data",}
            params = {"output": self.file_name_pdf,"landscape": False,}
            # params = {"output": self.file_path + self.file_name_pdf,"landscape": False,}
            files = {'file': open(self.file_path + self.file_name_docx, 'rb'),}
            # files = {'file': '(None, ' + open(self.file_path + self.file_name_docx, 'rb') + ')'}
            print(f"REQUEST: {self.base_url}  params={params}, headers={headers}")
            response = requests.post(self.base_url, params=params, headers=headers, files=files)
            print(f"RESPONSE_CODE: {response.status_code}")
            return response.json()
        except:
            return 1
            # return "Error while calling \"APYHUB\" API: {response.status_code}"
        # if response.status_code == 200:
        #     return response.json()
        # else:
        #     return "Error while calling \"APYHUB\" API: {response.status_code}"