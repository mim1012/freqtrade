import json


class Config:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> dict:
        with open(self.config_path) as f:
            return json.load(f)

    def get_exchange_config(self, exchange_name: str) -> dict:
        return self.config['exchanges'][exchange_name]
