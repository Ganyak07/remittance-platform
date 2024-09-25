# backend/main.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .wallet import RemittanceWallet
from .config import Config
from .model import db, User, Wallet, Transaction
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RemittancePlatform:
    def __init__(self):
        self.wallet = RemittanceWallet()

    def create_bitcoin_address(self):
        address = self.wallet.get_bitcoin_address()
        logger.info(f"Created new Bitcoin address: {address}")
        return address

    def send_bitcoin(self, address, amount):
        try:
            txid = self.wallet.send_bitcoin(address, amount)
            logger.info(f"Sent {amount} BTC to {address}. Transaction ID: {txid}")
            return txid
        except Exception as e:
            logger.error(f"Failed to send Bitcoin: {str(e)}")
            raise

    def create_lightning_invoice(self, amount_msat, label, description):
        try:
            invoice = self.wallet.create_lightning_invoice(amount_msat, label, description)
            logger.info(f"Created Lightning invoice: {invoice['bolt11']}")
            return invoice
        except Exception as e:
            logger.error(f"Failed to create Lightning invoice: {str(e)}")
            raise

    def pay_lightning_invoice(self, bolt11):
        try:
            payment = self.wallet.pay_lightning_invoice(bolt11)
            logger.info(f"Paid Lightning invoice: {bolt11}")
            return payment
        except Exception as e:
            logger.error(f"Failed to pay Lightning invoice: {str(e)}")
            raise

    def execute_stacks_transfer(self, recipient, amount, sender_key):
        try:
            result = self.wallet.execute_stacks_transfer(recipient, amount, sender_key)
            logger.info(f"Executed Stacks transfer. Transaction: {result}")
            return result
        except Exception as e:
            logger.error(f"Failed to execute Stacks transfer: {str(e)}")
            raise

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Create RemittancePlatform instance
    platform = RemittancePlatform()

    @app.route('/')
    def hello():
        return "Welcome to the Remittance Platform API"

    @app.route('/create_bitcoin_address')
    def api_create_bitcoin_address():
        address = platform.create_bitcoin_address()
        return {"address": address}

    # Add more routes for other RemittancePlatform methods as needed

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)