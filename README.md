# paper2kg

![](https://img.shields.io/badge/Status-Developing-brightgreen.svg)

Generate Knowledge Graph for Paper

## Files

- 8.xml: paper XML example
- paperAPI.py: api entry
- d3.html: visualization demo (You need to replace the 'links' value [line 8, d3.html].)
 
## Requirements (python packages)

- uvicorn
- fastapi
- pydantic
- xml
- nltk

Before using NLTK, you may need to add the following code to the top of readxml.py and text2kg.py

```
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```

Once the download is successful, these two lines of code must be removed.

## Run

```bash
python paperAPI.py
```

- API docs: http://127.0.0.1:8000/docs
