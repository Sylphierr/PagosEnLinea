#Primer modulo de python, pagos en linea
from fastapi import FastAPI
from pydantic  import BaseModel #Para validar los datos de entrada
import uvicorn #Ayncronus server Gateway

app = FastAPI()

class PedidoPrueba(BaseModel):
    producto: str
    cantidad: int
    notas_cliente:str | None = None #Campo opcional

@app.get("/")
def read_root():
    return{"message":"Mi primer modulo de python, pagos en linea"}

#Endpoint para recibir un pedido (se utiliza el metodo POST para recibir datos con FastAPI)
@app.post("/recibir-pedido/")
def recibir_pedido(pedido: PedidoPrueba):
    return{
        "estatus: "Recibido con éxito",
        "datos_recibidos": pedido,
        "mensaje":f"Anotado: {pedido.cantidad} x {pedido.producto}. Preparando envio..."
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)