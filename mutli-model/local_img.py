def encoding (image_path):
    with open(image_path, "rb") as image_file:
        return base64, 64encode(
            image_file.read()
        )
        decode("utf-8")

image_path = "image_path.jpg"


base64_image = encode_image(image_path)


response = client.chat.completions.create(
    model = "",
    messages=[
        "role":"user", "content":[
            {"type":"text", "text":"tt"},
            {"type":"image_url", "image_url":{
                "url":"data_image/jpg;basa64,{base64_image}"
            }}
        ]
    ]
)