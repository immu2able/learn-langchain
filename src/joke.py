from langchain_community.llms import Ollama

llm = Ollama(model="llama2")

joke = llm.invoke("Tell me a joke")

print(joke)