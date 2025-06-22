"""
Simple example demonstrating Google Cloud SDK integration.
"""

from google.adk.agents import LlmAgent


from google.adk.tools.application_integration_tool.application_integration_toolset import ApplicationIntegrationToolset

connector_tool = ApplicationIntegrationToolset(
    project="attguesser", # TODO: replace with GCP project of the connection
    location="us-central1", #TODO: replace with location of the connection
    connection="bga",
    entity_operations={"ahr": ["LIST"]},
)

# Example: Adding instructions
test_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="testing_agent",
    description="Answer to the user to maintain a talk.",
    instruction="""You are an agent of testing, just answer to the user to maintain a talk.
    You are a helpful assistant. Your task is to engage in a conversation with the user,
""",
    tools=[connector_tool],
)


root_agent = test_agent