from mem0 import Memory
from openai import OpenAI
import json

client = OpenAI()

config={
    "version":"v1.1",
    "embedder": {
        "provider":"openai",
        "config":{
            "api_key":"", "model":"text-embedding-3-small"
        },
        "llm":{
            "provider":"openai",
        "config":{
            "api_key":"", "model":"text-embedding-3-small"
        },
        },
        "vector_store":{
            "provider":"qdrant",
            "config":{
                "host":"localhost",
                "port":6379
            }
        }
    }
}


memory_client = Memory.from_config(config)

user_query = input("ask..")

search_memory = memory_client.search(query=user_query, user_id="radhey")

memories = [
    f"ID: {mem.get("id")}\n Memory : { mem.get("memory")}"for mem in search_memory.get("result")
]

SYSTEM_PROMPT = f""""
here is the context about the user :
{json.dumps(memories)}
"""

response = client.chat.completions.create(
    model="gpt-3",
    messages=[
        { "role":"system", "content": SYSTEM_PROMPT},
        {"role":"user", "content": user_query},
    ]
)

ai_response = response.choices[0].message.content

memory_client.add(
    user_id="radhey",
    messages=[
        {
        
            "role":"user", "content":user_query,
        },
        {
            "role":"assestent", "content":ai_response
        }
    ]
)

print("done")
