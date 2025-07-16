import uvicorn
from pathlib import Path 
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from zyro.core.router import mount_routes 
from zyro.core.parser import laod_yaml_file, get_endpoints, get_active_environment

def create_app(config_path: Path) -> FastAPI:
    app = FastAPI(title="Zyro", description = "Deploy APIs from YAML configs. Instantly.", version="1.0.0")
    
    # Load configuration from the specified YAML file
    config = laod_yaml_file(config_path)
    
    # Extract routes from the configuration
    routes = get_endpoints(config)

    env = get_active_environment(config)

    # Mount static folder
    app.mount("/static", StaticFiles(directory="zyro/static"), name="static")
    
    # Mount the routes to the FastAPI application
    mount_routes(app, routes)
    
    uvicorn.run(
            app, 
            host=config[env].get('host', '0.0.0.0'), 
            port=config[env].get('port', 8000), 
            reload=config[env].get('reload', False)
        )