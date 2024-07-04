from fastapi import FastAPI
from routing.users import router as users_routing

app = FastAPI(title='LikeAPI')

app.include_router(users_routing)

if __name__ == "__main__":
    import uvicorn # Official recommendation is to start Uvicorn Main: app --host = 127.0.0.1 --port = 8010 - BRELOAD
    uvicorn.run(app='main:app', host="127.0.0.1", port=8010, reload=True)
