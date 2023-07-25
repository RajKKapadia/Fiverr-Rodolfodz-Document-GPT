from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
import pinecone

from config import config

def create_conversation(query: str, chat_history: list) -> tuple:
    try:
        pinecone.init(
            api_key=config.PINECONE_API_KEY,
            environment=config.PINECONE_ENVIRONMENT,
        )
        embeddings = OpenAIEmbeddings(
            openai_api_key=config.OPENAI_API_KEY
        )
        db = Pinecone.from_existing_index(
            index_name=config.PINECONE_INDEX_NAME,
            embedding=embeddings
        )
        memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=False
        )
        cqa = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=0.0,
                           openai_api_key=config.OPENAI_API_KEY),
            retriever=db.as_retriever(),
            memory=memory,
            get_chat_history=lambda h: h,
        )
        result = cqa({'question': query, 'chat_history': chat_history})
        return result['answer']
    except Exception as e:
        
        return config.ERROR_MESSAGE

def create_conversation_gradio(query: str, chat_history: list) -> tuple:
    try:
        pinecone.init(
            api_key=config.PINECONE_API_KEY,
            environment=config.PINECONE_ENVIRONMENT,
        )
        embeddings = OpenAIEmbeddings(
            openai_api_key=config.OPENAI_API_KEY
        )
        db = Pinecone.from_existing_index(
            index_name=config.PINECONE_INDEX_NAME,
            embedding=embeddings
        )
        memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=False
        )
        cqa = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=0.0,
                           openai_api_key=config.OPENAI_API_KEY),
            retriever=db.as_retriever(),
            memory=memory,
            get_chat_history=lambda h: h,
        )
        result = cqa({'question': query, 'chat_history': chat_history})
        chat_history.append((query, result['answer']))
        return '', chat_history
    except Exception as e:
        chat_history.append((query, e))
        return '', chat_history
    