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

"""
Responses 200
1. /paper2kg/ & /post_paper2kg
message: success
time: analysis time for XML file
data: KG data
    index of KG triple
        source: head entity
        target: tail entity
        rela: relation
        confidence: confidence for NRE in this triple
        ext_info: external information
            type: triple type
            section_id: text position
"""


@app.get("/paper2kg/")
async def paper2kg(paperID: str, confidence: float, fine_grain: bool):
    """
    :param paperID: paper path
    :param confidence: confidence for NRE, 0.6 recommended
    :param fine_grain: grain for NRE, False recommended
    :return:
    :example:
    http://127.0.0.1:8000/paper2kg?paperID=8.xml&confidence=0.6&fine_grain=false
    """
    start = time.time()
    paper = PaperXML(paperID)
    api_data = paper.paper2kg_api(confidence=confidence, max_entity_len=4, fine_grain=fine_grain)
    print(time.time() - start)
    return {"message": "success", 'time': time.time() - start, 'data': api_data}


class PostItem4Text2Kg(BaseModel):
    paperID: str = None
    confidence: float = None
    fine_grain: bool = None


@app.post('/post_paper2kg')
async def post_paper2kg(request: PostItem4Text2Kg):
    """
    :param request:
    :return:
    :example:
    {"paperID": "8.xml", "confidence": 0.1, "fine_grain": "False"}
    """
    start = time.time()
    paperID = request.paperID
    confidence = float(request.confidence)
    fine_grain = bool(request.fine_grain)
    paper = PaperXML(paperID)
    api_data = paper.paper2kg_api(confidence=confidence, max_entity_len=4, fine_grain=fine_grain)
    print(time.time() - start)
    return {"message": "success", 'time': time.time() - start, 'data': api_data}


if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8000, workers=1)

# uvicorn paperAPI:app --reload
