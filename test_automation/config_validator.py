REQUIRED_FIELDS = ["host", "port", "timeout"]

def validate_config(config):
    for field in REQUIRED_FIELDS:
        if field not in config:
            return False

    if not isinstance(config["host"], str):
        return False

    if not isinstance(config["port"], int):
        return False

    if not 1 <= config["port"] <= 65535:
        return False

    if not isinstance(config["timeout"], (int, float)):
        return False

    if config["timeout"] <= 0:
        return False

    return True