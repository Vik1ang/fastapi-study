import uvicorn
from fastapi import FastAPI

from tutorial import app03, app04

app = FastAPI()

app.include_router(app03, prefix='/chapter03', tags=['Chapter03'])
app.include_router(app04, prefix='/chapter04', tags=['Chapter04'])

if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)
