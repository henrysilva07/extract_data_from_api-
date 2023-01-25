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
        logger.info("Getting data from endpoint: {endpoint}")
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()


class DaySummaryApi(MercadoBitCoin):

    type = "day-summary"

    def _get_endpoint(self, date: datetime.date) -> str:
        return f"{self.endpoint}/{self.coin}/{self.type}/{date.year}/{date.month}/{date.day}"
    


class TradesApi(MercadoBitCoin):

    type = "trades"

    def _get_unix_epoch( self, date: datetime) -> int:
        return int(date.timestamp())


    def _get_endpoint(self, date_from: datetime = None, date_to: datetime = None ) -> str:


        if date_from and not date_to : 
            date_from_unix = self._get_unix_epoch(date_from)

            endpoint = f"{self.endpoint}/{self.coin}/{self.type}/{date_from_unix}"
        elif date_from and date_to:
            date_from_unix = self._get_unix_epoch(date_from)
            date_to_unix = self._get_unix_epoch(date_to)
            endpoint = f"{self.endpoint}/{self.coin}/{self.type}/{date_from_unix}/{date_to_unix}"

        else:
            endpoint = f"{self.endpoint}/{self.coin}/{self.type}"

        return endpoint








    










