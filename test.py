import torch
from langchain_ollama import OllamaLLM
print("Hello from Kino!")
print("CUDA available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")

llm = OllamaLLM(model="mistral")
print(llm.invoke("What is LangChain?"))
