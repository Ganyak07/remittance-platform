# backend/bitcoin_integration.py

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from decimal import Decimal
from .config import Config
from .errors import BitcoinError
import logging

logger = logging.getLogger(__name__)

class BitcoinIntegration:
    def __init__(self):
        rpc_user = Config.BITCOIN_RPC_USER
        rpc_password = Config.BITCOIN_RPC_PASSWORD
        rpc_host = Config.BITCOIN_RPC_HOST
        rpc_port = Config.BITCOIN_RPC_PORT
        self.rpc_connection = AuthServiceProxy(f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}')

    def create_address(self):
        try:
            address = self.rpc_connection.getnewaddress()
            logger.info(f"Created new Bitcoin address: {address}")
            return address
        except JSONRPCException as e:
            logger.error(f"Failed to create new Bitcoin address: {str(e)}")
            raise BitcoinError(f"Failed to create new Bitcoin address: {str(e)}")

    def get_balance(self):
        try:
            balance = Decimal(self.rpc_connection.getbalance())
            logger.info(f"Retrieved Bitcoin balance: {balance}")
            return balance
        except JSONRPCException as e:
            logger.error(f"Failed to retrieve Bitcoin balance: {str(e)}")
            raise BitcoinError(f"Failed to retrieve Bitcoin balance: {str(e)}")

    def send_bitcoin(self, address, amount):
        try:
            amount = float(amount)  # Convert to float for Bitcoin Core RPC
            txid = self.rpc_connection.sendtoaddress(address, amount)
            logger.info(f"Sent {amount} BTC to {address}. Transaction ID: {txid}")
            return txid
        except JSONRPCException as e:
            logger.error(f"Failed to send Bitcoin: {str(e)}")
            raise BitcoinError(f"Failed to send Bitcoin: {str(e)}")