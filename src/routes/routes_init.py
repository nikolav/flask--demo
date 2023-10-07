from .index import index as route_index

def routes_init(app):
  
  @app.route("/")
  def home(*args):
    return route_index(*args)


