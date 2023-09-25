from io import BytesIO
from fastapi import FastAPI
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from fastapi.responses import StreamingResponse
import torch

app = FastAPI()

model_id = "stabilityai/stable-diffusion-2"
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, scheduler=scheduler, torch_dtype=torch.float16
).to("cuda")


@app.get("/")
def get_version():
    return {"version": "0.1"}


@app.get("/image")
def get_image(prompt: str):
    bytes_io = BytesIO()
    pipe(prompt).images[0].save(bytes_io, format="PNG")
    return StreamingResponse(BytesIO(bytes_io.getvalue()), media_type="image/png")
