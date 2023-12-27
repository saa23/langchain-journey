# langchain-journey

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


## References:
- Great tutorial from freeCodeCamp [LangChain Crash Course for Beginner](https://www.youtube.com/watch?v=lG7Uxts9SXs)
- Awesome articles from Ivan Reznikov [LangChain 101 Course](https://medium.com/@ivanreznikov/langchain-101-course-updated-668f7b41d6cb) 
    - [CheatSheet](https://pub.towardsai.net/langchain-cheatsheet-all-secrets-on-a-single-page-8be26b721cde)
    - [Building Simple App](https://pub.towardsai.net/langchain-101-part-1-building-simple-q-a-app-90d9c4e815f3)
    - [Large Language Model](https://pub.towardsai.net/langchain-101-part-2ab-all-you-need-to-know-about-large-language-models-3512ae41dfc3)
    - [Fine-tuning LLMs](https://pub.towardsai.net/langchain-101-part-2c-fine-tuning-llms-with-peft-lora-and-rl-5c9890ed0766)

*Will also check other tutorials:*
- *Writing from Ankit Yadav [Top 5 Resources to Learn LangChain](https://medium.com/@ankity09/top-5-resources-to-learn-langchain-e2bdbbd11702)*
- *Youtube playlist from Greg Kamradt [LangChain Playlist](https://www.youtube.com/playlist?list=PLqZXAkvF1bPNQER9mLmDbntNfSpzdDIU5)*
