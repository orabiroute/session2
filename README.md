## Testing Script

```python
prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant having a conversation with a user. Use the context from previous messages to provide relevant and coherent responses.

Previous conversation:
{chat_history}

Current user message: {user_input}

Please respond naturally and helpfully, taking into account the conversation history and context.
""")
```

## App 
```python
    template = """
    You are a helpful assistant. Answer the following questions considering the history of the conversation:

    Chat history: {chat_history}

    User question: {user_question}
    """
```

### Dashbord for Chat together

https://api.together.ai/?_gl=1*zwzu85*_gcl_au*MjExODcwNzI3NS4xNzUyMzMyMjQ5

### Chat together with langchain
https://python.langchain.com/docs/integrations/chat/together/



