from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableSequence
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
    input_variables=["topic"],
    template="""
    Write a detailed report about {topic}.
    Include important points and practical examples.
    """
)

prompt2 = PromptTemplate(
    input_variables=["text"],
    template="""
    Summarize the following report.
    Keep only the most important information:
    {text}
    """
)

report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (
        lambda x: len(x.split()) > 250,
        RunnableSequence(prompt2, model, parser)
    ),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_chain, branch_chain)

response = final_chain.invoke({
    "topic": "Artificial Intelligence in Healthcare"
})

console.print(Markdown("### Final Report"))
console.print(Markdown(response))