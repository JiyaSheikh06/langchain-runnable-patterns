from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel
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
    Write an engaging Instagram caption for: {product}
    Include relevant hashtags.
    """
)

prompt2 = PromptTemplate(
    input_variables=["product"],
    template="""
    Write a professional LinkedIn product announcement for: {product}
    Focus on its value and benefits.
    """
)

marketing_chain = RunnableParallel({
    "Instagram": RunnableSequence(prompt1, model, parser),
    "LinkedIn": RunnableSequence(prompt2, model, parser)
})

response = marketing_chain.invoke({
    "product": "An AI-powered personal finance app that helps users track expenses and manage budgets."
})

console.print(Markdown("### Instagram Caption"))
console.print(Markdown(response["Instagram"]))

console.print(Markdown("### LinkedIn Post"))
console.print(Markdown(response["LinkedIn"]))