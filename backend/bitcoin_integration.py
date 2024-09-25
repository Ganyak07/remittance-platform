# backend/bitcoin_integration.py

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import Decimal
from .config import Config

class BitcoinIntegration:
    def __init__(self):
        rpc_user = Config.BITCOIN_RPC_USER
        rpc_password = Config.BITCOIN_RPC_PASSWORD
        rpc_host = Config.BITCOIN_RPC_HOST
        rpc_port = Config.BITCOIN_RPC_PORT
        self.rpc_connection = AuthServiceProxy(f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}')

    def create_address(self):
        try:
            return self.rpc_connection.getnewaddress()
        except JSONRPCException as e:
            print(f"An error occurred: {e}")
            return None

    def get_balance(self):
        try:
            return Decimal(self.rpc_connection.getbalance())
        except JSONRPCException as e:
            print(f"An error occurred: {e}")
            return Decimal('0')

    def send_bitcoin(self, address, amount):
        try:
            amount = float(amount)  # Convert to float for Bitcoin Core RPC
            txid = self.rpc_connection.sendtoaddress(address, amount)
            return txid
        except JSONRPCException as e:
            print(f"An error occurred: {e}")
            return None