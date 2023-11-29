# langchain-beginner-journey

## Introduction

LangChain is a framework designed to make LLM (Large Language Model) application easier.

It is able to integrate with various API sources of AI model related to LLM.


Three main concepts in LangChain:
1. Component
    - LLM Wrappers
    - Prompt Templates
    - Indexes for information retrieval

    Generally, it handles the input for LLM Agents.

2. Chains (tools)
    - Assembles components (functions) to solve a specific task
3. Agents
    - Enable the LLM model to interact with the environment 


## Process Flow
Generally, process flow in LangChain Agent as following:
- **Question**: input from user's prompt 
- **Thought**: what agent think about what to do
- **Action**: the action to take, should be on of tools.
- **Action Input**: the input to the action
- **Observation**: the result of the action
- **Final Answer**: The answer send to the environment.


## reference:
- Great tutorial  from freeCodoeCamp.org [LangChain Crash Course for Beginner](https://www.youtube.com/watch?v=lG7Uxts9SXs)