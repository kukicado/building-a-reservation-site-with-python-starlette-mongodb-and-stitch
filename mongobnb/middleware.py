from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
import pymongo
import ssl

class DatabaseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        client = pymongo.MongoClient("{YOUR-CONNECTION-STRING}", ssl_cert_reqs=ssl.CERT_NONE)
        db = client["sample_airbnb"]
        request.state.db = db
        response = await call_next(request)
        return response

middleware = [
    Middleware(DatabaseMiddleware)
]