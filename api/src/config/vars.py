
IS_PRODUCTION = False
# IS_PRODUCTION = True

_DB_URI_PRODUCTION = "postgres://app:app@pg/app"
_DB_URI_DEVELOPMENT = "postgres://app:app@70.34.223.252:5544/app"

DB_URI = _DB_URI_PRODUCTION if True == IS_PRODUCTION else _DB_URI_DEVELOPMENT
