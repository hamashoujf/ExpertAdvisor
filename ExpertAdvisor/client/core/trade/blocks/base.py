from abc import ABC, abstractmethod
import pandas as pd

class AbstractBlock(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def schema(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def update(self) -> None:
        pass
