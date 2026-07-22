from __future__ import annotations

import uuid
from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_session
from app.models.note import Note

router = APIRouter(prefix="/api/notes", tags=["notes"])

SessionDep = Annotated[Session, Depends(get_session)]


class NoteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    text: str
    created_at: datetime


class NoteIn(BaseModel):
    text: str = Field(min_length=1, max_length=500)


@router.get("", response_model=list[NoteOut])
def list_notes(session: SessionDep) -> list[Note]:
    stmt = select(Note).order_by(Note.created_at.desc()).limit(100)
    return list(session.scalars(stmt).all())


@router.post("", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(body: NoteIn, session: SessionDep) -> Note:
    note = Note(text=body.text.strip())
    session.add(note)
    session.commit()
    session.refresh(note)
    return note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: uuid.UUID, session: SessionDep) -> None:
    note = session.get(Note, note_id)
    if note is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "note not found")
    session.delete(note)
    session.commit()
