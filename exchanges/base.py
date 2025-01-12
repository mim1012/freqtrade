from abc import ABC, abstractmethod


class BaseExchange(ABC):
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    @abstractmethod
    async def get_balance(self) -> dict:
        pass

    @abstractmethod
    async def get_ticker(self, symbol: str) -> dict:
        pass

    @abstractmethod
    async def create_order(self, symbol: str, order_type: str, side: str, amount: float, price: float = None) -> dict:
        pass

    @abstractmethod
    async def cancel_order(self, symbol: str, order_id: str) -> bool:
        pass
