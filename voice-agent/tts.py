async_client = AsynOpenAI


async def tts (speech:str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="",
        voice="coral",
        input=speech,
        instructions="",
        response_format="pcm"
    ) as resposne:
        await LocalAudioPlayer().play(resposne)