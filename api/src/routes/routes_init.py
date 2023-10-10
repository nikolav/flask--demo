
from .index      import index      as route_index
from .docs_list  import docs_list  as route__docs_list


def routes_init(app):
  
  @app.route("/")
  def home():
    return route_index()
  
  @app.route("/docs", methods=["POST"])
  def docs():
    return route__docs_list()

