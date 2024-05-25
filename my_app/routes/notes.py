from typing import Annotated, Optional

from uuid import uuid4

from fastapi import APIRouter, HTTPException, status, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from my_app.schemas.notes import NoteSchema
# from my_app.login_manager import login_manager
import my_app.services.notes as service_note


router = APIRouter(prefix="/notes", tags=["Notes"])
templates = Jinja2Templates(directory="my_app/templates")

# by PL
@router.get('/all')
def listes_notes(
    request: Request,
    # user: UserSchema = Depends(login_manager.optional),
):
    notes = service_note.get_all_notes()
   
    return templates.TemplateResponse(
        request,
        "liste_notes.html",{"notes":notes}
    )

