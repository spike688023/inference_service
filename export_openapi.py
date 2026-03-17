import yaml
import json
from main import app
from fastapi.openapi.utils import get_openapi

def save_openapi_yaml():
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    )
    with open("openapi.yml", "w") as f:
        yaml.dump(openapi_schema, f, sort_keys=False)
    print("Successfully exported openapi.yml")

if __name__ == "__main__":
    save_openapi_yaml()
