from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
 

class Hero(BaseModel):
    id: int
    position: int
    name: str

repo = []

#Получаем васех героев
@app.get("/all_heros", response_model=List[Hero])
def get_heros():
    return repo

# Получить героя по ID
@app.get("/heroes{hero_id}", response_model=Hero)
def get_heroes(hero_id: int):
    hero = next((hero for hero in repo if hero.id == hero_id), None)
    if hero is None:
        raise HTTPException(status_code=404, detail="Герой не найден")
    return hero

@app.post("/new_hero", response_model=Hero)
def create_heroes(hero: Hero):
    repo.append(hero)
    return hero
