from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
import pandas as pd


#  Reading the reviews from a CSV file

df= pd.read_csv("reviews.csv")

#

model= OllamaLLM (model="llama3.2")

template = """ You are an expert in answering questions about a pizza resturant
Here are some relevant reviews: {reviews} 

Here is the question to answer: {question}

"""

prompt= ChatPromptTemplate.from_template(template)
chain= prompt | model

while True:
    print("\n\n........................................")
    question= input("Ask your question q for quit: ")
    print("\n\n")
    if question.lower() == "q":
        break
    result =chain.invoke({"reviews":[], "question":question})
    print( result)