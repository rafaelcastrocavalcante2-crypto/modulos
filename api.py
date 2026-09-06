from fastapi import FastAPI
from fastapi import HTTPException
from Tarefas import Tarefa

app = FastAPI()


banco_de_dados = []

@app.get('/tarefas')
def listar_tarefas():
    return banco_de_dados
    #return {'': 'API no ar olá mundo'}
    #raise HTTPException(status_code=404,detail='Tarefa não encontrada')

@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa):
    tarefa_dict = tarefa.model_dump() 
    banco_de_dados.append(tarefa_dict)    
    return {"mensagem": "tarefa criada com sucesso", "dados": tarefa_dict}
