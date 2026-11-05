from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough, RunnableLambda
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_output_tokens=1000,
)

parser = StrOutputParser()
console = Console()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    input_variables=["product"],
    template="Write a short product description for {product}.",
)

description_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    "description": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count),
})

final_chain = RunnableSequence(description_chain, parallel_chain)

response = final_chain.invoke({
    "product": "Wireless Bluetooth Headphones"
})

console.print(Markdown("### Product Description:\n" + response["description"]))
console.print(Markdown("### Word Count:\n" + str(response["word_count"])))