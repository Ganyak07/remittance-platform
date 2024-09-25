from bitcoin_integration import BitcoinIntegration
   from lightning_integration import LightningIntegration

   class RemittanceWallet:
       def __init__(self):
           self.bitcoin = BitcoinIntegration()
           self.lightning = LightningIntegration()

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

   # Usage example
   if __name__ == "__main__":
       wallet = RemittanceWallet()
       btc_address = wallet.get_bitcoin_address()
       btc_balance = wallet.get_bitcoin_balance()
       print(f"Bitcoin address: {btc_address}")
       print(f"Bitcoin balance: {btc_balance} BTC")