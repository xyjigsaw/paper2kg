# pip install fastapi
# pip install uvicorn


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# uvicorn test:app --reload


"""
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

document = 'BHK'
sentences = nltk.sent_tokenize(document)
for sent in sentences:
    print('---------------------------------------------')
    print(sent)
    for item in nltk.pos_tag(nltk.word_tokenize(sent)):
        print(item)
"""