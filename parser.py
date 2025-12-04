from llama_parse import LlamaParse
import os
from dotenv import load_dotenv

load_dotenv()

parser = LlamaParse(
    api_key= os.environ.get("LLAMA_CLOUD_API_KEY"),
    result_type="markdown",
    is_formatting_instruction=False,
)

result = parser.parse("documents/Request-For-tender.pdf")

markdown_documents = result.get_markdown_documents(split_by_page=True)

for page in result.pages:
    print(page.md)