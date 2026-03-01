from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

data_dir = Path(__file__).parent / "data"
pdf_files = [data_dir / "study_text1.pdf", data_dir / "study_text2.pdf"]

articles = []
for pdf_path in pdf_files:
    loader = PyPDFLoader(str(pdf_path))
    pages = loader.load()
    text = "\n".join(page.page_content for page in pages)
    articles.append(text)
        
# for i, article in enumerate(articles):
#     print(f"Article {i+1}:\n{article[:300]}\n")
    
template = """
Please write a 3-4 sentences summary of the following text:
{article}
"""

prompt = PromptTemplate(
    input_variables=["article"],
    template=template,
)

for article in articles:
    summary_prmpt = prompt.format(article=article)
    
    num_tokens = llm.get_num_tokens(summary_prmpt)
    print(f"Number of tokens in the prompt and article: {num_tokens}")

    response = llm.invoke(summary_prmpt)
    summary = response.text

    print(f"Summary:\n{summary.strip()}\n")
    print("\n")
