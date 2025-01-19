from deepface import DeepFace

def retrieve(img):
    demography = DeepFace.analyze(img)
    emotions = demography[0]["emotion"]
    top_emotion = demography[0]["dominant_emotion"]

    return emotions, top_emotion