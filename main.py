from google import genai

client = genai.Client()

prompt = input("ask...")

def main():
    response = client.models.generate_content(
        model='gemenai-2.5-flash',
        contents=prompt
        
    )
    print(response.text)
