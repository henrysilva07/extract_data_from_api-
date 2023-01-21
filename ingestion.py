import requests
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


class MercadoBitCoin():

    def __init__(self, coin: str) -> None:
        self.coin = coin 
        self.endpoint = "https://www.mercadobitcoin.net/api"

    def _get_endpoint(self) -> str:
        return f"{self.endpoint}/{self.coin}/day-summary/2023/1/20/"

    def get_data(self) -> dict:
        endpoint = self._get_endpoint()
        logger.info("Getting data from endpoinr: {endpoint}")
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()


print(MercadoBitCoin("BTC").get_data())



    










