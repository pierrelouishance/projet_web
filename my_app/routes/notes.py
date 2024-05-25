from typing import Annotated, Optional

from uuid import uuid4

from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

# from my_app.schemas import TaskSchema, NewTaskSchema, UserSchema
# from my_app.login_manager import login_manager
# import my_app.services.tasks as service


router = APIRouter(prefix="/notes", tags=["Notes"])
templates = Jinja2Templates(directory="templates")

# by PL
@router.get('/all')
def get_all_notes(
    request: Request,
    # user: UserSchema = Depends(login_manager.optional),
):
   
    return templates.TemplateResponse(
        request,
        "liste_notes.html"
    )

