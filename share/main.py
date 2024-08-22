from fastapi.responses import FileResponse  
from fastapi import FastAPI, File, UploadFile
import os
app=FastAPI()
@app.post("/file/upload")
async def upload(file:UploadFile = File(...)):
    try:
        dir="./files/"
        os.makedirs(dir,exist_ok=True)
        filePath=dir + file.filename
        with open(filePath,"wb+") as fileobj:
            fileobj.write(file.file.read())
            return {"code":0}
    except:
        return {"code":1}
@app.get("/file/download/{filename}")
async def download(filename:str):
    dir="./files/" + filename
    if os.path.exists(dir):
        return FileResponse(dir)
    return {"code":1}