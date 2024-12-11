import PIL.Image
import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import google.generativeai as genai
import PIL
from io import BytesIO

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.get("/")
def index():
    return "Hello World !!"

@app.post("/upload")
async def sketch_to_code(file: UploadFile):
    try:
        os.mkdir("uploads")
        image_bytes = await file.read()
        image = PIL.Image.open(BytesIO(image_bytes))
        image.save("uploads/" + file.filename)
        response = model.generate_content(["Describe me about this image", image])
        print(response.text)
        os.remove(f"uploads/{file.filename}")
        os.rmdir("uploads")
        return response.text
    except:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error while sending image to LLM for getting code response"
        )
        
@app.post("/upload-image")
async def img_describe(file: UploadFile):
    try:
        os.mkdir("uploads")
        image_bytes = await file.read()
        image = PIL.Image.open(BytesIO(image_bytes))
        image.save("uploads/" + file.filename)
        response = model.generate_content(["Describe me about this image", image])
        print(response.text)
        os.remove(f"uploads/{file.filename}")
        os.rmdir("uploads")
        return response.text
    except:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error while sending image to LLM for getting code response"
        )


if __name__=="__main__":
    uvicorn.run(app)