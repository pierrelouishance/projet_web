from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# from my_app.routes.tasks import router as task_router
from my_app.routes.notes import router as note_router
from my_app.database import create_database


app = FastAPI(title="Gestion notes")
app.mount("/static", StaticFiles(directory="static"))
app.include_router(note_router)
# app.include_router(user_router)


@app.on_event("startup")
def on_application_started():
    create_database()