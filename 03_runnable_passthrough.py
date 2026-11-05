from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnablePassthrough
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
    input_variables=["feedback"],
    template="""
    Summarize this customer feedback in a few sentences:
    {feedback}
    """
)

prompt2 = PromptTemplate(
    input_variables=["summary"],
    template="""
    Based on this customer feedback summary,
    suggest two practical improvements for the business:
    {summary}
    """
)

summary_chain = RunnableSequence(prompt1, model, parser)

final_chain = RunnableSequence(
    summary_chain,
    RunnableParallel({
        "original_summary": RunnablePassthrough(),
        "suggestions": RunnableSequence(prompt2, model, parser)
    })
)

response = final_chain.invoke({
    "feedback": """
    The application is easy to use, but it takes too long
    to load. Some features also stop working occasionally.
    """
})

console.print(Markdown("### Customer Feedback Summary"))
console.print(Markdown(response["original_summary"]))

console.print(Markdown("### Suggested Improvements"))
console.print(Markdown(response["suggestions"]))