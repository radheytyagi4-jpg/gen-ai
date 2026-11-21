from openai import OpenAI

client = OpenAI

response = client.chat.compleletions.create(
    model = "",
    messages=[
        {"role":"user", "content":[
         {
            "type":"text", "text":"hiii, my name is radhey",
        },
        {
            "type":"image", "image":"url"
        }
        ]
        }
    ]
)

print(response.content[0].choices.message)