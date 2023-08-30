from ..base import AbstractBlock

import pandas as pd
from abc import ABC, abstractmethod

class AbstractRuleBlock(AbstractBlock):
    @abstractmethod
    def validate(self, context: pd.DataFrame) -> None:
        raise NotImplementedError
