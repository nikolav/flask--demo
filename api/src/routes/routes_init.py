from .index import index as route_index


def routes_init(app):
  
  @app.route("/")
  def home():
    return route_index()
