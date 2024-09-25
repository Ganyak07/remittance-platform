# Remittance Platform API Documentation

## Base URL
`http://api.yourremittanceplatform.com/v1`

## Authentication
All API requests require a valid API key to be included in the header:
```
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### 1. Create Bitcoin Address
- **URL**: `/bitcoin/address`
- **Method**: `GET`
- **Description**: Creates a new Bitcoin address for receiving funds.
- **Response**:
  ```json
  {
    "address": "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"
  }
  ```

### 2. Send Bitcoin
- **URL**: `/bitcoin/send`
- **Method**: `POST`
- **Description**: Sends Bitcoin to a specified address.
- **Body**:
  ```json
  {
    "address": "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2",
    "amount": 0.001
  }
  ```
- **Response**:
  ```json
  {
    "txid": "7b

c21ddb53dec190b5ae43ded0687d4255

e0a856d8a1490

a0e0b80d3e1a1

52e8"
  }
  ```

### 3. Create Lightning Invoice
- **URL**: `/lightning/invoice`
- **Method**: `POST`
- **Description**: Creates a new Lightning Network invoice.
- **Body**:
  ```json
  {
    "amount_msat": 100000,
    "label": "test",
    "description": "Test payment"
  }
  ```
- **Response**:
  ```json
  {
    "bolt11": "lnbc1

...long

string..."
  }
  ```

### 4. Pay Lightning Invoice
- **URL**: `/lightning/pay`
- **Method**: `POST`
- **Description**: Pays a Lightning Network invoice.
- **Body**:
  ```json
  {
    "bolt11": "lnbc1...long string..."
  }
  ```
- **Response**:
  ```json
  {
    "payment_hash": "

e9c1

95f

82b9

f26e

957b

2

c54

f41de

5a

9390

b3

ff9

d73

f01d

33

e36"
  }
  ```

### 5. Execute Stacks Transfer
- **URL**: `/stacks/transfer`
- **Method**: `POST`
- **Description**: Executes a transfer on the Stacks blockchain.
- **Body**:
  ```json
  {
    "recipient": "ST1

PQHQKV0RJXZFY1DGX8MNSNYVE3VGZJSRTPGZGM",
    "amount": 1000000,
    "sender_key": "your_private_key_here"
  }
  ```
- **Response**:
  ```json
  {
    "txid": "

0x1234...

"
  }
  ```

## Error Handling
All endpoints

 may return the following error responses:

- **400 Bad Request**: Invalid input parameters
- **401 Unauthorized**: Invalid or missing API key
- **500 Internal Server Error**: Server-side error

Error response format:
```json
{
  "error": "Error message describing the issue"
}
```

## Rate Limiting
API requests are limited to 100 requests per minute per API key. If you exceed this limit, you'll receive a 429 Too Many Requests response.