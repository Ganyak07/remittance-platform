# backend/wallet.py

from .bitcoin_integration import BitcoinIntegration
from .lightning_integration import LightningIntegration
from .stacks_integration import StacksIntegration
from .errors import WalletError, BitcoinError, LightningError, StacksError
import logging

logger = logging.getLogger(__name__)

class RemittanceWallet:
    def __init__(self):
        self.bitcoin = BitcoinIntegration()
        self.lightning = LightningIntegration()
        self.stacks = StacksIntegration()

    def get_bitcoin_address(self):
        try:
            address = self.bitcoin.create_address()
            logger.info(f"Generated new Bitcoin address: {address}")
            return address
        except BitcoinError as e:
            logger.error(f"Failed to generate Bitcoin address: {str(e)}")
            raise WalletError(f"Failed to generate Bitcoin address: {str(e)}")

    def get_bitcoin_balance(self):
        try:
            balance = self.bitcoin.get_balance()
            logger.info(f"Retrieved Bitcoin balance: {balance}")
            return balance
        except BitcoinError as e:
            logger.error(f"Failed to retrieve Bitcoin balance: {str(e)}")
            raise WalletError(f"Failed to retrieve Bitcoin balance: {str(e)}")

    def send_bitcoin(self, address, amount):
        try:
            txid = self.bitcoin.send_bitcoin(address, amount)
            logger.info(f"Sent {amount} BTC to {address}. Transaction ID: {txid}")
            return txid
        except BitcoinError as e:
            logger.error(f"Failed to send Bitcoin: {str(e)}")
            raise WalletError(f"Failed to send Bitcoin: {str(e)}")

    def create_lightning_invoice(self, amount_msat, label, description):
        try:
            invoice = self.lightning.create_invoice(amount_msat, label, description)
            logger.info(f"Created Lightning invoice: {invoice['bolt11']}")
            return invoice
        except LightningError as e:
            logger.error(f"Failed to create Lightning invoice: {str(e)}")
            raise WalletError(f"Failed to create Lightning invoice: {str(e)}")

    def pay_lightning_invoice(self, bolt11):
        try:
            payment = self.lightning.pay_invoice(bolt11)
            logger.info(f"Paid Lightning invoice: {bolt11}")
            return payment
        except LightningError as e:
            logger.error(f"Failed to pay Lightning invoice: {str(e)}")
            raise WalletError(f"Failed to pay Lightning invoice: {str(e)}")

    def get_lightning_balance(self):
        try:
            balance = self.lightning.get_balance()
            logger.info(f"Retrieved Lightning balance: {balance}")
            return balance
        except LightningError as e:
            logger.error(f"Failed to retrieve Lightning balance: {str(e)}")
            raise WalletError(f"Failed to retrieve Lightning balance: {str(e)}")

    def execute_stacks_transfer(self, recipient, amount, sender_key):
        try:
            transaction = self.stacks.call_contract_function("transfer", [recipient, amount], sender_key)
            logger.info(f"Executed Stacks transfer to {recipient}")
            return transaction
        except StacksError as e:
            logger.error(f"Failed to execute Stacks transfer: {str(e)}")
            raise WalletError(f"Failed to execute Stacks transfer: {str(e)}")