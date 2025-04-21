from pydantic import BaseModel, Field
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

class WikiInputs(BaseModel):
    """Inputs for the Wikipedia tool."""
    query: str = Field(
        description="query to look up in Wikipedia, should be 3 or less words"
    )

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)

tool = WikipediaQueryRun(
    name = "wiki-tool",
    description = "look up things in wikipedia",
    args_schema = WikiInputs,
    api_wrapper = api_wrapper,
    return_direct = True
)

# print(tool.description)
# print(tool.input_schema)
# print(tool.output_schema)
# print(tool.args)
# print(tool.name)
# print(tool.return_direct)

res = tool.run({"query": "who is Dr. Yunus?"})
print(res)