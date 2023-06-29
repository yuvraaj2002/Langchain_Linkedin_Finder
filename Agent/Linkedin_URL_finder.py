from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.agents import initialize_agent, Tool, AgentExecutor,AgentType

# This method will take in the name as input and returns its linkedin profile URL
def find_url(name:str)->str:

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
    Given the name of the {person} give me the linkedin profile URL
    of this person. Your answer should contain only a URL
    """

    # let's define the tools of agent
    tools_for_agent = [
        Tool(
            name="Crawl Google for lnikedin profile page",
            func=get_profile_url, # This is method that will use SERPAPI
            description="Useful when you need to get the Linkedin profile URL",
        )
    ]

    # Let's now initialize the agent
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Let's now create a prompt template
    prompt_template = PromptTemplate.from_template(template = template)

    linkedin_profile_url = ""
    return linkedin_profile_url





