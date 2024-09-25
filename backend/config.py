# backend/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Bitcoin settings
    BITCOIN_RPC_USER = os.getenv('BITCOIN_RPC_USER', 'rpcuser')
    BITCOIN_RPC_PASSWORD = os.getenv('BITCOIN_RPC_PASSWORD', 'rpcpassword')
    BITCOIN_RPC_HOST = os.getenv('BITCOIN_RPC_HOST', 'localhost')
    BITCOIN_RPC_PORT = os.getenv('BITCOIN_RPC_PORT', '18332')  # Testnet port

    # Lightning settings
    LIGHTNING_RPC_PATH = os.getenv('LIGHTNING_RPC_PATH', '/path/to/lightning-rpc')

    # Stacks settings
    STACKS_CONTRACT_ADDRESS = os.getenv('STACKS_CONTRACT_ADDRESS', 'ST1PQHQKV0RJXZFY1DGX8MNSNYVE3VGZJSRTPGZGM')
    STACKS_CONTRACT_NAME = os.getenv('STACKS_CONTRACT_NAME', 'remittance')

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///remittance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API settings
    SECRET_KEY = os.getenv('API_SECRET_KEY', 'your-secret-key')