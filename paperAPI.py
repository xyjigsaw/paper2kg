# Name: paperAPI
# Author: Reacubeth
# Time: 2020/5/1 9:34
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from readXML import PaperXML
from text2kg import text2kg_api
import time
from toolkit.pdf_parser import Parser

app = FastAPI()

"""
Responses 200

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

# paper2KG


@app.get("/paper2kg/")
async def paper2kg(paperID: str, confidence: float, fine_grain: bool):
    """
    :param paperID: paper path
    :param confidence: confidence for NRE, 0.6 recommended
    :param fine_grain: grain for NRE, False recommended
    :return:
    :example:
    http://127.0.0.1:8000/paper2kg?paperID=ELG.pdf&confidence=0.6&fine_grain=false
    """
    start = time.time()
    parser = Parser('cermine')
    parser.parse('text', paperID, 'output', 50)
    paper = PaperXML('output/' + paperID[:-3] + 'cermine.xml')
    api_data = paper.paper2kg_api(confidence=confidence, max_entity_len=4, fine_grain=fine_grain)
    # print(time.time() - start)
    return {"message": "success", 'time': time.time() - start, 'data': api_data}


class PostItem4Paper2Kg(BaseModel):
    paperID: str = None
    confidence: float = None
    fine_grain: bool = None


@app.post('/post_paper2kg')
async def post_paper2kg(request: PostItem4Paper2Kg):
    """
    :example:
    {"paperID": "ELG.pdf", "confidence": 0.1, "fine_grain": "False"}
    """
    start = time.time()
    paperID = request.paperID
    confidence = float(request.confidence)
    fine_grain = bool(request.fine_grain)
    parser = Parser('cermine')
    parser.parse('text', paperID, 'output', 50)
    paper = PaperXML('output/' + paperID[:-3] + 'cermine.xml')
    api_data = paper.paper2kg_api(confidence=confidence, max_entity_len=4, fine_grain=fine_grain)
    # print(time.time() - start)
    return {"message": "success", 'time': time.time() - start, 'data': api_data}


# text2KG


@app.get("/text2kg/")
async def text2kg(text: str, confidence: float, fine_grain: bool):
    """
    :param text: input text
    :param confidence: confidence for NRE, 0.6 recommended
    :param fine_grain: grain for NRE, False recommended
    :return:
    :example:
    http://127.0.0.1:8000/text2kg/?text=AceMap%20is%20based%20on%20MAG.&confidence=0.1&fine_grain=true
    """
    start = time.time()
    api_data = text2kg_api(text=text, confidence=confidence, max_entity_len=4, fine_grain=fine_grain)
    # print(time.time() - start)
    return {"message": "success", 'time': time.time() - start, 'data': api_data}


class PostItem4Text2Kg(BaseModel):
    text: str = None
    confidence: float = None
    fine_grain: bool = None


@app.post('/post_text2kg')
async def post_text2kg(request: PostItem4Text2Kg):
    """
    :example:
    {"text": "AceMap is based on MAG.", "confidence": 0.1, "fine_grain": "False"}
    """
    start = time.time()
    text = request.text
    confidence = float(request.confidence)
    fine_grain = bool(request.fine_grain)
    api_data = text2kg_api(text=text, confidence=confidence, max_entity_len=4, fine_grain=fine_grain)
    # print(time.time() - start)
    return {"message": "success", 'time': time.time() - start, 'data': api_data}


if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8000, workers=1)

# uvicorn paperAPI:app --reload --port 7000 --host 127.0.0.1
