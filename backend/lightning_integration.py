# backend/lightning_integration.py

import json
import socket
from .config import Config
from .errors import LightningError
import logging

logger = logging.getLogger(__name__)

class LightningRpc:
    def __init__(self, socket_path):
        self.socket_path = socket_path

    def _call(self, method, params):
        try:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            s.connect(self.socket_path)
            request = json.dumps({"method": method, "params": params, "id": 0})
            s.sendall(request.encode())
            response = b""
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                response += chunk
            s.close()
            return json.loads(response.decode())["result"]
        except (socket.error, json.JSONDecodeError) as e:
            logger.error(f"Lightning RPC call failed: {str(e)}")
            raise LightningError(f"Lightning RPC call failed: {str(e)}")

class LightningIntegration:
    def __init__(self):
        self.rpc = LightningRpc(Config.LIGHTNING_RPC_PATH)

    def create_invoice(self, amount_msat, label, description):
        try:
            invoice = self.rpc._call("invoice", [amount_msat, label, description])
            logger.info(f"Created Lightning invoice: {invoice['bolt11']}")
            return invoice
        except LightningError as e:
            logger.error(f"Failed to create Lightning invoice: {str(e)}")
            raise

    def pay_invoice(self, bolt11):
        try:
            payment = self.rpc._call("pay", [bolt11])
            logger.info(f"Paid Lightning invoice: {bolt11}")
            return payment
        except LightningError as e:
            logger.error(f"Failed to pay Lightning invoice: {str(e)}")
            raise

    def get_balance(self):
        try:
            balance = self.rpc._call("listfunds", [])['channels']
            logger.info(f"Retrieved Lightning balance: {balance}")
            return balance
        except LightningError as e:
            logger.error(f"Failed to retrieve Lightning balance: {str(e)}")
            raise