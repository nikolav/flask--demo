from flask import request

def sum2nums():
  data = request.get_json()  
  sum = data["x1"] + data["x2"]
  res = { "sum": sum }
  return res

