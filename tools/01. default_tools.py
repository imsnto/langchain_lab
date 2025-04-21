"""
Tools are interfaces that an agent, chain, or LLM can use to interact with the world.
They combine a few things:

1. The name of the tool
2. A description of what the tool is
3. JSON schema of what the inputs to the tool are
4. The function to call
5. Whether the result of a tool should be returned directly to the user
"""

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
tool = WikipediaQueryRun(api_wrapper=api_wrapper)

"""
    tool.description
    tool.input_schema
    tool.output_schema
    tool.args -> {}
    tool.name  -> wikipedia
    tool.return_direct -> False
"""
res = tool.run({"query": "who is Dr. Yunus?"})
print(res)