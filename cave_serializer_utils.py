def infer_prop_type(prop_entry):
    if "value" not in prop_entry:
        return "head"
    elif isinstance(prop_entry["value"], str):
        return "text"
    elif isinstance(prop_entry["value"], bool):
        return "toggle"
    elif isinstance(prop_entry["value"], dict):
        return "selector"
    return "num"
