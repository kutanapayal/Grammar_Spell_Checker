from gingerit.gingerit import GingerIt
import uvicorn
from fastapi import FastAPI
import os

app =FastAPI(debug=True)
@app.get("/text_correction/")
async def text_correction(text : str):
    if text:
        parser = GingerIt()
        response = parser.parse(text)
        return {"Text":text,"Result":response['result']}
    return {"text": "is None."}

if __name__ == "__main__":
    host_name=os.environ.get('ENV_HOSTNAME')
    #print(host_name)
    uvicorn.run(app,host=host_name,port=8090)






