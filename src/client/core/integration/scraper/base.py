from abc import ABC, abstractmethod
import pandas as pd

class AbstractScraper(ABC):
    @abstractmethod
    def fetch(self) -> str:
        pass

    @abstractmethod
    def parse(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def scrape(self) -> pd.DataFrame:
        pass
