from llama_index import SimpleDirectoryReader
import utils

import os
import openai


openai.api_key = utils.get_openai_api_key()
print(openai.api_key)
documents = SimpleDirectoryReader(
    input_files=["./eBook-How-to-Build-a-Career-in-AI.pdf"]
).load_data()