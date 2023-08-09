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

def get_name(obj, master=None):
    if inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isbuiltin(obj):
        if obj.__module__:
            name = f"{obj.__module__}.{obj.__name__}({get_parameters(obj)})"
        else:
            try:
                name = f"{obj.__self__.__name__}.{obj.__name__}({get_parameters(obj)})"
            except ValueError:
                name = f"{obj.__self__.__name__}.{obj.__name__}(/)"
    elif inspect.isclass(obj):
        if obj.__module__:
            name = f"{obj.__module__}.{obj.__name__}({get_parameters(obj.__init__)})"
        else:
            try:
                name = f"{obj.__name__}({get_parameters(obj.__init__)})"
            except ValueError:
                name = f"{obj.__name__}(/)"
    else:
        if master:
            if hasattr(obj, "__name__"):
                name = f"{master}.{obj.__name__}(self, /)"
            else:
                name = f"{master}.{type(obj).__name__}(self, /)"
        else:
            if hasattr(obj, "__name__"):
                name = obj.__name__
            else:
                name = type(obj).__name__
    
    return name

def get_info(obj):
    data = {}
    
    data["name"] = get_name(obj)
    
    data["type"] = f"{type(obj).__module__}.{type(obj).__name__}({get_parameters(type(obj).__init__)})"
    
    if hasattr(obj, "__str__"):
        data["string_form"] = str(obj)
    elif hasattr(obj, "__repr__"):
        data["string_form"] = repr(obj)
    else:
        data["string_form"] = "(Unavailable)"

    if len(data["string_form"]) > 20:
        data["string_form"] = data["string_form"][:21] + "..."
    
    doc = inspect.getdoc(obj)
    if doc:
        data["document"] = doc
    
    if inspect.isfunction(obj) or inspect.ismethod(obj):
        data["parameters"] = get_parameters(obj)
    
    cls = None
    
    if inspect.isclass(obj):
        cls = obj
    elif hasattr(obj, "__module__"):
        cls = type(obj)
    
    if cls:
        attrs = []
        for i in dir(cls):
            attr = getattr(cls, i)
            if callable(attr):
                attrs.append(get_name(attr, master=data["name"]))
            else:
                attrs.append(repr(attr))
        
        data["attributes"] = attrs
    
    return data

