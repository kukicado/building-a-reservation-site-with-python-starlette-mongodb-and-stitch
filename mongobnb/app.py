from starlette.applications import Starlette
from starlette.routing import Route
from middleware import middleware
from routes import homepage, listing, confirmation

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/listing/{id}', listing),
    Route('/confirmation/{id}', confirmation),
], middleware=middleware)