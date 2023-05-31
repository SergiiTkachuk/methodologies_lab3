from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    data = {
        "student": "Serhii Tkachuk",
        "age": 19
    }

    return data
