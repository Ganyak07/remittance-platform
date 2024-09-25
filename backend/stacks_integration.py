# backend/stacks_integration.py

from stacks_transactions import (
    ContractCallOptions,
    PostConditionMode,
    make_contract_call,
)
from .config import Config
from .errors import StacksError
import logging

logger = logging.getLogger(__name__)

class StacksIntegration:
    def __init__(self):
        self.contract_address = Config.STACKS_CONTRACT_ADDRESS
        self.contract_name = Config.STACKS_CONTRACT_NAME

    def call_contract_function(self, function_name, function_args, sender_key):
        try:
            options = ContractCallOptions(
                contract_address=self.contract_address,
                contract_name=self.contract_name,
                function_name=function_name,
                function_args=function_args,
                sender_key=sender_key,
                post_condition_mode=PostConditionMode.ALLOW,
            )
            transaction = make_contract_call(options)
            # Here you would broadcast the transaction to the Stacks network
            # This step depends on how you're connecting to the Stacks network
            logger.info(f"Called Stacks contract function: {function_name}")
            return transaction
        except Exception as e:
            logger.error(f"Failed to call Stacks contract function: {str(e)}")
            raise StacksError(f"Failed to call Stacks contract function: {str(e)}")