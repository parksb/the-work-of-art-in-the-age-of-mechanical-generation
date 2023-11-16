from io import BytesIO
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from fastapi.responses import StreamingResponse
from transformers import pipeline
import torch

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm_pipe = pipeline("text-generation", model="Gustavosta/MagicPrompt-Stable-Diffusion")

df_model_id = "stabilityai/stable-diffusion-2-1"
df_scheduler = EulerDiscreteScheduler.from_pretrained(
    df_model_id, subfolder="scheduler"
)
df_pipe = StableDiffusionPipeline.from_pretrained(
    df_model_id, scheduler=df_scheduler, torch_dtype=torch.float16
).to("cuda")


@app.get("/")
def get_version():
    return {"version": "0.1"}


@app.get("/test/chat")
def test_chat(prompt: str):
    return llm_pipe(prompt)


@app.get("/test/image")
def test_image(prompt: str):
    bytes_io = BytesIO()
    df_pipe(prompt).images[0].save(bytes_io, format="PNG")
    return StreamingResponse(BytesIO(bytes_io.getvalue()), media_type="image/png")


@app.get("/prompt")
def prompt(x: str):
    return llm_pipe(x)[0]["generated_text"]


@app.get("/new")
def new(prompt: str):
    df_pipe(prompt).images[0].save("generated_image.png")
    incr_version()
    return True


@app.get("/image")
def image():
    return StreamingResponse(open("generated_image.png", "rb"), media_type="image/png")


@app.get("/image_ready")
def image_ready(x: int):
    f = open("generated_version", "r")
    version = int(f.readline())
    if version > x:
        return True
    return False


def incr_version():
    f = open("generated_version", "r")
    version = int(f.readline())
    f = open("generated_version", "w")
    f.write(str(version + 1))
    f.close()
    return version + 1
