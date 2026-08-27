from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False