from config.config import app
from api.routes.health import health_route

app.include_router(health_route)
