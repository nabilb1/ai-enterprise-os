from fastapi import FastAPI
from pydantic import BaseModel

from agents.ceo_agent import CEOAgent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


ceo_agent = CEOAgent()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
async def root():
    return {"message": "AI Enterprise OS"}


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = ceo_agent.run(request.message)

        return {
            "response": response
        }

    except Exception as e:
        import traceback

        print("==== ERREUR CHAT ====")
        print(str(e))
        traceback.print_exc()

        return {
            "response": f"ERREUR: {str(e)}"
        }


@app.get("/test")
async def test():
    return {
        "cors": "OK"
    }

@app.post("/chat")
async def chat(request: ChatRequest):

    print("REQUETE RECUE")

    response = ceo_agent.run(request.message)

    return {
        "response": response
    }