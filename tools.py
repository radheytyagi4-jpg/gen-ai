from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun, DuckDuckGoSearchAPIWrapper
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

def save_to_text(data:str, filename:str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    formatted_txt = f"--- Research Output ({timestamp}) ---\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_txt)

        return f"Data saved to {filename} at {timestamp}"

save_to_text_tool = Tool(
    name="save_to_text",
    func=save_to_text,
    description="Saves the research output to a text file. Input should be a string."
)
wrapper = DuckDuckGoSearchAPIWrapper(backend="duckduckgo")
search = DuckDuckGoSearchRun(api_wrapper=wrapper)
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for infomation"
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)