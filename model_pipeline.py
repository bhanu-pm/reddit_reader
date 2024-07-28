import os
from dotenv import load_dotenv

# import torch
# from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


# Loading saved model weights #########################
load_dotenv()
os.getenv("HUGGINGFACEHUB_API_TOKEN")

# model_path = "./weights/"
# model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")
# tokenizer = AutoTokenizer.from_pretrained(model_path)

# Creating a general huggingface pipeline
# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=25)

# Prompt template
user_prompt_template = """
You will be given some text which could contain a few details:
	- a coupon code
	- how much the code is worth
	- locations in which this coupon code will work 

It is your job to understand the text and identify the coupon code along with the other details,
then return the coupon code along with its monetary value.
Here is the text you should understand and parse : {reddit_comment}
"""

# Creating a langchain parse-able prompt template, invoke the prompt(to pass variables into the prompt) store it in final_prompt
prompt_template = PromptTemplate.from_template(user_prompt_template)
reddit_comment = input("Enter the comment : ")
final_prompt = prompt_template.invoke({'reddit_comment': reddit_comment})


# Model.invoke(input prompt)
# print(model.invoke(prompt_template.format(reddit_comment=reddit_comment)))

# hf = HuggingFacePipeline(pipeline=pipe)
# hf(prompt_template.format(reddit_comment=reddit_comment))
