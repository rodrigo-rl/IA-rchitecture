from fastapi import FastAPI
from router import Styles, model, image

app=FastAPI()

app.include_router(Styles.router)
app.include_router(model.router)
app.include_router(image.router)
#app.include_router(players.router)
#app.include_router(equipos.router)
#app.include_router(goals.router)

@app.get("/")
def raiz():
    return {"message":"Bienvenido a mi api"}
