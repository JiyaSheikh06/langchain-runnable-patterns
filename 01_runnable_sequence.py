from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_output_tokens=1000,
)

parser = StrOutputParser()
console = Console()

prompt1 = PromptTemplate(
    input_variables=["product"],
    template="""
    Write a product description for an online store.
    Product: {product}
    """
)

prompt2 = PromptTemplate(
    input_variables=["draft"],
    template="""
    Improve this product description.
    Make it engaging, clear and concise.
    Draft: {draft}
    """
)

product_chain = RunnableSequence(
    prompt1, model, parser,
    prompt2, model, parser
)

response = product_chain.invoke({
    "product": "Wireless Bluetooth Headphones with noise cancellation"
})

console.print(Markdown(response))
