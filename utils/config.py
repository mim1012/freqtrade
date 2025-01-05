import json
from typing import Dict

class Config:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> Dict:
        with open(self.config_path, 'r') as f:
            return json.load(f)

    def get_exchange_config(self, exchange_name: str) -> Dict:
        return self.config['exchanges'][exchange_name] 