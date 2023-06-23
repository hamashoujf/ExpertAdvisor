from abc import ABC, abstractmethod
import pandas as pd

class AbstractBlock(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(self) -> pd.DataFrame:
        raise NotImplementedError

    @abstractmethod
    def schema(self) -> pd.DataFrame:
        raise NotImplementedError

    @abstractmethod
    def update(self) -> None:
        raise NotImplementedError
