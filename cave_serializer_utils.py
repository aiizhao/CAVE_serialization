def infer_prop_type(prop_entry):
    if "type" in prop_entry:
        return prop_entry["type"]
    elif "value" not in prop_entry:
        return "head"
    elif isinstance(prop_entry["value"], str):
        return "text"
    elif isinstance(prop_entry["value"], bool):
        return "toggle"
    elif isinstance(prop_entry["value"], dict):
        return "selector"
    return "num"


def pixel_value_to_num(string):
    return float(string[:-2])
