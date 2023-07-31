import inspect

def get_parameters(callable_obj):
    parameters = inspect.signature(callable_obj).parameters
    
    result = []
    
    for param_name, param in parameters.items():
        kind = str(param.kind)
        
        if param.default != inspect.Parameter.empty:
            result.append(str(param))
        elif kind == "POSITIONAL_ONLY":
            result.append(f"{param_name}")
        elif kind == "VAR_POSITIONAL":
            result.append(str(param))
        elif kind == "VAR_KEYWORD":
            result.append(str(param))
        else:
            result.append(param_name)
    
    return ", ".join(result)


def get_info(obj):
    data = {}
    
    if inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isbuiltin(obj):
        if obj.__module__:
            data["name"] = f"{obj.__module__}.{obj.__name__}({get_parameters(obj)})"
        else:
            data["name"] = f"{obj.__self__}.{obj.__name__}({get_parameters(obj)})"
    else:
        if hasattr(obj, "__name__"):
            data["name"] = obj.__name__
        elif type(obj).__module__ != "builtins":
            data["name"] = type(obj).__name__
    
    data["type"] = f"{type(obj).__module__}.{type(obj).__name__}({get_parameters(type(obj).__init__)})"
    
    if hasattr(obj, "__repr__"):
        data["string_form"] = repr(obj)
    elif hasattr(obj, "__str__"):
        data["string_form"] = str(obj)
    else:
        data["string_form"] = "(Unavailable)"
    
    doc = inspect.getdoc(obj)
    if doc:
        data["document"] = doc
    
    if inspect.isfunction(obj) or inspect.ismethod(obj):
        data["parameters"] = get_parameters(obj)
    
    if inspect.isclass(obj):
        data["attributes"] = dir(obj)
    elif hasattr(obj, "__module__"):
        data["attributes"] = dir(type(obj))
    
    return data

