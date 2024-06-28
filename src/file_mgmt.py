# Externals.
import os

# Locals.
from docx_to_pdf import DocxToPdf


class FileMgmt:
  def __init__(self, fpath, fdocx, fpdf):
      self.file_path = fpath
      self.file_name_docx = fdocx
      self.file_name_pdf = fpdf


  def delete_old_file(self):
    """
    Deletes old versions of a file.
    """
    try:
      print("Deleting File " + self.file_path + self.file_name_pdf)
      
      if os.path.exists(self.file_path + self.file_name_pdf):
        os.remove(self.file_path + self.file_name_pdf)
        print("Deleted File " + self.file_path + self.file_name_pdf)
      else:
        print("File does not exist " + self.file_path + self.file_name_pdf)

    except IOError:
        print("Error: could not create file " + self.file_path + self.file_name_pdf)
  

  def create_new_file(self):
    """
    Converts a docx file to a pdf file using the DocxToPdf class.
    """
    docx_to_pdf = DocxToPdf()
    docx_to_pdf.convert_file(self.file_path, self.file_name_docx, self.file_name_pdf)

