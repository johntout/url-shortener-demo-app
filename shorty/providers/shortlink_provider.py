from abc import ABC, abstractmethod

class ShortlinkProvider(ABC):
    @abstractmethod
    def __init__(self, url: str):
        pass

    @abstractmethod
    def shortenUrl() -> str:
        pass