
from .index    import index    as route__index
from .docs_ls  import docs_ls  as route__docs_ls
from .docs_rm  import docs_rm  as route__docs_rm
from .docs_put import docs_put as route__docs_put


def routes_init(app):
  
  @app.get("/")
  def home():
    return route__index()
  
  @app.get("/docs")
  def docs_ls():
    return route__docs_ls()

  @app.delete("/docs")
  def docs_rm():
    return route__docs_rm()
  
  @app.post("/docs")
  def docs_put():
    return route__docs_put()
