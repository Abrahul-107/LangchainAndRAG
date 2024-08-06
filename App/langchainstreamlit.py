import streamlit as st
from langchain_together import ChatTogether
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Check if the API_KEY is loaded
if API_KEY is None:
    st.error("API_KEY not found. Please set it in the .env file.")
else:
    # Initialize the ChatTogether LLM
    chat = ChatTogether(
        together_api_key=API_KEY,
        model="meta-llama/Llama-3-70b-chat-hf",
    )

    # Define the prompt templates and chains
    prompt_template_name = PromptTemplate(
        input_variables=['recipe'],
        template='I want to open a restaurant for {recipe} food. Give me only two fancy names in a single word.'
    )

    chain = LLMChain(
        llm=chat,
        prompt=prompt_template_name,
        output_key='restaurant_name'
    )

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template='Suggest some menu items for {restaurant_name}. Return it as a comma-separated list in two lines with the restaurant name.'
    )

    food_item_chain = LLMChain(
        llm=chat,
        prompt=prompt_template_items,
        output_key='menu_items'
    )

    seq_chain = SequentialChain(
        chains=[chain, food_item_chain],
        input_variables=['recipe'],
        output_variables=['restaurant_name', 'menu_items']
    )

    # Streamlit app
    st.title("Restaurant Name and Menu Generator")

    recipe = st.text_input("Enter a recipe:", "dal")

    if st.button("Generate"):
        if recipe:
            try:
                result = seq_chain.invoke({'recipe': recipe})
                st.subheader("Generated Restaurant Name:")
                st.write(result.get('restaurant_name', "No name generated"))
                st.subheader("Suggested Menu Items:")
                st.write(result.get('menu_items', "No menu items generated"))
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please enter a recipe.")
