from fastapi import APIRouter

from ..dependencies import SessionDep

router = APIRouter()


@router.get("/heroes/")
def get_heroes(session: SessionDep):
    return {}
