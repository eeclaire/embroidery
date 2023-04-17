import pdf_reader
from settings import PATTERNS_FOLDER_PATH

# file_path = f"{PATTERNS_FOLDER_PATH}/PAT1633.pdf"
# file_path = f"{PATTERNS_FOLDER_PATH}/PAT1708.pdf"
file_path = f"{PATTERNS_FOLDER_PATH}/PAT1761.pdf"


raw_df = pdf_reader.read_pdf(file_path)

floss_requirements = pdf_reader.parse_pdf_contents(raw_df)
