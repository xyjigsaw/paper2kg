# Name: paperAPI
# Author: Reacubeth
# Time: 2020/5/1 9:34
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

import uvicorn
from fastapi import FastAPI
from readXML import PaperXML
from pydantic import BaseModel
import time

app = FastAPI()


@app.get("/text2kg")
async def text2kg():
    start = time.time()
    paper = PaperXML('8.xml')
    api_data = paper.text2kg_api(0.6, 4)
    print(time.time() - start)
    return {"message": "success", 'time': time.time() - start, 'data': api_data}


class PostItem4Text2Kg(BaseModel):
    paperID: str = None
    confidence: float = None
    fine_grain: bool = None


@app.post('/post_text2kg')
async def post_text2kg(request: PostItem4Text2Kg):
    """
        {"paperID": "8.xml", "confidence": 0.1, "fine_grain": "False"}
    """
    start = time.time()
    paperID = request.paperID
    confidence = float(request.confidence)
    fine_grain = bool(request.fine_grain)
    paper = PaperXML(paperID)
    api_data = paper.text2kg_api(confidence=confidence, max_entity_len=4, fine_grain=fine_grain)
    print(time.time() - start)
    return {"message": "success", 'time': time.time() - start, 'data': api_data}


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8000, workers=1)

# uvicorn paperAPI:app --reload
