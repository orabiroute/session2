"Main Logic of our chatbot"

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers.string import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

def get_response(
        user_query,
        chat_history
):
    llm = ChatOpenAI(
        model="gpt-4o-mini"
    )

    template = """
    You are a helpful assistant. Answer the following questions considering the history of the conversation:

    Chat history: {chat_history}

    User question: {user_question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | llm | StrOutputParser()

    return chain.stream(
        {"chat_history":chat_history,
         "user_question":user_query}
    )