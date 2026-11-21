import speech_recogintion as sr


def main():
    r = sr.recogintion()

    with sr.microphone() as source:
        r.adjust_ambient_noise(source)
        r.pause_threholt = 2

        print("speak smtg")

        stt = r.response_google(audio)
        print(stt)

main()