from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fasthx import Jinja
from pydantic import BaseModel


# Pydantic model of the data the example API is using.
class User(BaseModel):
    first_name: str
    last_name: str


# Create the app.
app = FastAPI()
app.mount("/static", StaticFiles(directory="htmx/static"), name="static")
# Create a FastAPI Jinja2Templates instance and use it to create a
# FastHX Jinja instance that will serve as your decorator.
jinja = Jinja(Jinja2Templates("htmx/templates"))


@app.get("/")
@jinja.page("index.jinja")
def index() -> None:
    ...


@app.get("/user-list")
@jinja.hx("user-list.jinja")
async def htmx_or_data() -> list[User]:
    return [
        User(first_name="John", last_name="Lennon"),
        User(first_name="Paul", last_name="McCartney"),
        User(first_name="George", last_name="Harrison"),
        User(first_name="Ringo", last_name="Starr"),
    ]


@app.get("/admin-list")
@jinja.hx("user-list.jinja")
def htmx_only() -> list[User]:
    return [User(first_name="Billy", last_name="Shears")]


@app.get("/tailwind")
@jinja.page("tailwind-test.jinja")
def tailwind_test() -> None:
    ...
