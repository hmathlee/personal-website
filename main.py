from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")

templates = Jinja2Templates(directory="templates")


@app.get("/test")
def test(request: Request):
    return templates.TemplateResponse(
        request=request, name="test.html", context={}
    )


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={}
    )


@app.get("/portfolio")
def bio(request: Request):
    return templates.TemplateResponse(
        request=request, name="portfolio.html", context={}
    )


@app.get("/resume")
def resume(request: Request):
    return templates.TemplateResponse(
        request=request, name="resume.html", context={}
    )


@app.get("/bio")
def bio(request: Request):
    return templates.TemplateResponse(
        request=request, name="bio.html", context={}
    )
