import requests,logging , datetime
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


class MercadoBitCoin(ABC):

    def __init__(self, coin: str) -> None:
        self.coin = coin 
        self.endpoint = "https://www.mercadobitcoin.net/api"

    @abstractmethod
    def _get_endpoint(self,**kwargs) -> str:
        pass 
      

    def get_data(self,**kwargs) -> dict:
        endpoint = self._get_endpoint(**kwargs)
        logger.info("Getting data from endpoinr: {endpoint}")
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()


class DaySummaryApi(MercadoBitCoin):

    type = "day-summary"

    def _get_endpoint(self, date: datetime.date) -> str:
        return f"{self.endpoint}/{self.coin}/{self.type}/{date.year}/{date.month}/{date.day}"
    

print( DaySummaryApi(coin="BTC").get_data(date=datetime.date(2023, 1, 20)))






    










