from langchain_together import ChatTogether
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

# choose from our 50+ models here: https://docs.together.ai/docs/inference-models
chat = ChatTogether(
    together_api_key=API_KEY,
    model="meta-llama/Llama-3-70b-chat-hf",
)

# Define the first prompt template for generating restaurant names
prompt_template_name = PromptTemplate(
    input_variables=['recipe'],
    template='I want to open a restaurant for {recipe} food. Give me only two fancy names in a single word.'
)

# Create the LLMChain for generating restaurant names
chain = LLMChain(
    llm=chat,  
    prompt=prompt_template_name,
    output_key='restaurant_name'
)

# Define the second prompt template for generating menu items
prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template='Suggest some menu items for {restaurant_name}. Return it as a comma-separated list in two lines with the restaurant name.'
)

# Create the LLMChain for generating menu items
food_item_chain = LLMChain(
    llm=chat,  
    prompt=prompt_template_items,
    output_key='menu_items'
)

# Assuming `chain` and `food_item_chain` are predefined chains
seq_chain = SequentialChain(
    chains=[chain, food_item_chain],
    input_variables=['recipe'],
    output_variables=['restaurant_name', 'menu_items']
)

# Run the SequentialChain with the given input
result = seq_chain.invoke({'recipe': 'dal'})

print(result)
