# backend/wallet.py

from .bitcoin_integration import BitcoinIntegration
from .lightning_integration import LightningIntegration
from .stacks_integration import StacksIntegration

class RemittanceWallet:
    def __init__(self):
        self.bitcoin = BitcoinIntegration()
        self.lightning = LightningIntegration()
        self.stacks = StacksIntegration()

    def get_bitcoin_address(self):
        return self.bitcoin.create_address()

    def get_bitcoin_balance(self):
        return self.bitcoin.get_balance()

    def send_bitcoin(self, address, amount):
        return self.bitcoin.send_bitcoin(address, amount)

    def create_lightning_invoice(self, amount_msat, label, description):
        return self.lightning.create_invoice(amount_msat, label, description)

    def pay_lightning_invoice(self, bolt11):
        return self.lightning.pay_invoice(bolt11)

    def get_lightning_balance(self):
        return self.lightning.get_balance()

    def execute_stacks_transfer(self, recipient, amount, sender_key):
        return self.stacks.call_contract_function("transfer", [recipient, amount], sender_key)