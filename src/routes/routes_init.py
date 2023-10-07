from .index    import index    as route_index
from .sum2nums import sum2nums as route_sum2nums

def routes_init(app):
  
  @app.route("/")
  def home():
    return route_index()

  @app.route("/sum2nums", methods=["POST"])
  def sum2nums():
    return route_sum2nums()

