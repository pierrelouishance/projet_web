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
async def listes_notes(
    request: Request,
    # user: UserSchema = Depends(login_manager.optional),
):
    notes = service_note.get_all_notes()
   
    return templates.TemplateResponse(
        request,
        "liste_notes.html",{"notes":notes}
    )
@app.route('/accueil')
def accueil():
    return render_template('acceuil.html')

@router.get("/create")
def create_note_form(request: Request):
    return templates.TemplateResponse("create_notes.html", {"request": request})

@router.post("/create")
def create_note(request: Request, titre: str = Form(...), categorie: str = Form(...), texte: str = Form(...), db: Session = Depends(get_db)):
    if not titre or not categorie or not texte:
        raise HTTPException(status_code=400, detail="All fields are required")
    
    add_note(db, titre, categorie, texte, "auteur_id_placeholder")  # Remplacez "auteur_id_placeholder" par l'ID de l'utilisateur authentifié
    return RedirectResponse(url="/notes/all", status_code=303)
