# backend/errors.py

class RemittanceError(Exception):
    """Base exception class for remittance platform errors"""

class BitcoinError(RemittanceError):
    """Exception raised for Bitcoin-related errors"""

class LightningError(RemittanceError):
    """Exception raised for Lightning Network-related errors"""

class StacksError(RemittanceError):
    """Exception raised for Stacks-related errors"""

class WalletError(RemittanceError):
    """Exception raised for wallet-related errors"""