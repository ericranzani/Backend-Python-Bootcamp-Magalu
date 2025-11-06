from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get('/posts/{framework}')
def read_root(framework: str):
    return {
        "posts": [
            {'title': f'Criando uma aplicação com {framework}', 'date': datetime.now(timezone.utc)}, 
            {'title': f'Internacionalizando uma app {framework}', 'date': datetime.now(timezone.utc)},
        ]
    }
