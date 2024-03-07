import json
from pydantic import BaseModel

settings_file = "./settings.json"

class Global_Variables(BaseModel):
    host: str
    port: int
    debug: bool
    drone: bool
    hivemind_ip: str
    drone_ips: list[str]

try:
    with open(settings_file) as f:
        GLOBAL_VARIABLES = Global_Variables.parse_obj(json.load(f))
except Exception as e:
    print(e)
    GLOBAL_VARIABLES = None