
from random import randint

def index():
  res = { 
    "status": "ok",
    "data": randint(1, 100)
  }
  return res
