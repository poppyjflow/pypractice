# Externals.
import os

# Locals.
from file_mgmt import FileMgmt
from web_nav import web_nav

# Hard-coded vals for ease-of-use.
file_path = "/home/j/pypractice/docs/"
file_name_docx = "checklist.docx"
file_name_pdf = "checklist.pdf"
# file_name_pdf = "/home/j/pypractice/docs/checklist.pdf"


def main():
  print("Hello World!")
  # fileMgmt = FileMgmt(file_path, file_name_docx, file_name_pdf)

  # Step 1: Delete old file versions.
  # fileMgmt.delete_old_file()

  # Step 2: Create new file from DOCX using 3rd-party apyhub.com API 
  # fileMgmt.create_new_file()

  # Step 3: Same thing but using Selenium browser nav.
  web_nav()

  # print(f"Project Name: {project_details['name']}")
  print("Goodbye World!")


if __name__ == "__main__":
  main()

