from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import (load_tools,
                              initialize_agent,
                              AgentType
                              )

from dotenv import load_dotenv

load_dotenv()


def generative_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = name_chain({"animal_type": animal_type, "pet_color": pet_color})

    return response


def langchain_agent():
    llm  = OpenAI(temperature=0.5)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )

    return result

if __name__ == '__main__':
    # print(generative_pet_name("cat", "red"))
    print(langchain_agent())
