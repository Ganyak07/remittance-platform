# backend/lightning_integration.py

import json
import socket
from .config import Config

class LightningRpc:
    def __init__(self, socket_path):
        self.socket_path = socket_path

    def _call(self, method, params):
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

class LightningIntegration:
    def __init__(self):
        self.rpc = LightningRpc(Config.LIGHTNING_RPC_PATH)

    def create_invoice(self, amount_msat, label, description):
        return self.rpc._call("invoice", [amount_msat, label, description])

    def pay_invoice(self, bolt11):
        return self.rpc._call("pay", [bolt11])

    def get_balance(self):
        return self.rpc._call("listfunds", [])['channels']