from io import BytesIO
from fastapi import FastAPI
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from fastapi.responses import StreamingResponse
from transformers import pipeline
import torch

app = FastAPI()

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


# e.g., "Landscape of "
@app.get("/chat")
def chat(prompt: str):
    return llm_pipe(prompt)


@app.get("/image")
def get_image(prompt: str):
    bytes_io = BytesIO()
    df_pipe(prompt).images[0].save(bytes_io, format="PNG")
    return StreamingResponse(BytesIO(bytes_io.getvalue()), media_type="image/png")
