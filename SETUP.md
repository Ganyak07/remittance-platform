# Remittance Platform Setup Guide

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git
- Bitcoin Core (for Bitcoin integration)
- LND (for Lightning Network integration)
- Stacks node (for Stacks blockchain integration)

## Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/ganyak07/remittance-platform.git
   cd remittance-platform
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following variables:
   ```
   BITCOIN_RPC_USER=your_bitcoin_rpc_username
   BITCOIN_RPC_PASSWORD=your_bitcoin_rpc_password
   BITCOIN_RPC_HOST=localhost
   BITCOIN_RPC_PORT=18332
   LIGHTNING_RPC_PATH=/path/to/lightning-rpc
   STACKS_CONTRACT_ADDRESS=ST1PQHQKV0RJXZFY1DGX8MNSNYVE3VGZJSRTPGZGM
   STACKS_CONTRACT_NAME=remittance
   DATABASE_URI=sqlite:///remittance.db
   API_SECRET_KEY=your_secret_key
   ```

5. Initialize the database:
   ```
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```

6. Run the application:
   ```
   python run.py
   ```

## Running Tests
To run the unit tests:
```
python -m unittest discover tests
```

## Deployment
For production deployment, consider using a WSGI server like Gunicorn:
```
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## Troubleshooting
- If you encounter issues with Bitcoin RPC connection, ensure Bitcoin Core is running and the RPC credentials are correct.
- For Lightning Network issues, check that LND is properly configured and running.
- If you face problems with Stacks integration, verify that your Stacks node is operational and accessible.

For more detailed troubleshooting, refer to the respective documentation of Bitcoin Core, LND, and Stacks.



## License
This project is licensed under the MIT License - see the LICENSE.md file for details.