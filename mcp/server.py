import functools
import inspect
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import create_model
from typing import Any, Callable, Dict, List, Optional, Type

class Resource:
    def __init__(self, func: Callable, name: str = None):
        self.func = func
        self.name = name or func.__name__

class Tool:
    def __init__(self, func: Callable, name: str = None):
        self.func = func
        self.name = name or func.__name__

class Server:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.resources = {}
        self.tools = {}
        self.app = FastAPI(title=name, description=description)
        
        # Initialize routes
        self._setup_routes()
    
    def _setup_routes(self):
        @self.app.get("/health")
        async def health_check():
            return {"status": "healthy"}
        
        @self.app.get("/info")
        async def get_info():
            return {
                "name": self.name,
                "description": self.description,
                "resources": list(self.resources.keys()),
                "tools": list(self.tools.keys())
            }
    
    def resource(self, name: str = None):
        def decorator(func):
            resource_name = name or func.__name__
            self.resources[resource_name] = Resource(func, resource_name)
            
            # Create route for this resource
            parameters = self._get_function_parameters(func)
            dynamic_model = self._create_pydantic_model(parameters)
            
            @functools.wraps(func)
            async def wrapper(request_data: dynamic_model):
                try:
                    result = await func(**request_data.dict())
                    return result
                except Exception as e:
                    raise HTTPException(status_code=500, detail=str(e))
            
            self.app.post(f"/resources/{resource_name}", response_model=None)(wrapper)
            return func
        return decorator

    def tool(self, name: str = None):
        def decorator(func):
            tool_name = name or func.__name__
            self.tools[tool_name] = Tool(func, tool_name)
            
            # Create route for this tool
            parameters = self._get_function_parameters(func)
            dynamic_model = self._create_pydantic_model(parameters)
            
            @functools.wraps(func)
            async def wrapper(request_data: dynamic_model):
                try:
                    result = await func(**request_data.dict())
                    return result
                except Exception as e:
                    raise HTTPException(status_code=500, detail=str(e))
            
            self.app.post(f"/tools/{tool_name}", response_model=None)(wrapper)
            return func
        return decorator
    
    def _get_function_parameters(self, func):
        signature = inspect.signature(func)
        return {
            name: (param.annotation if param.annotation is not inspect.Parameter.empty else Any,
                param.default if param.default is not inspect.Parameter.empty else ...)
            for name, param in signature.parameters.items()
        }
    
    def _create_pydantic_model(self, parameters):
        return create_model('DynamicModel', **parameters)
    
    def run(self, host: str = "0.0.0.0", port: int = 8000):
        uvicorn.run(self.app, host=host, port=port)