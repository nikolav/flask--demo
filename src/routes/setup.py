from .index import index as route_index

def setup(app):
  @app.route("/")
  def home(*args):
    return route_index(*args)
