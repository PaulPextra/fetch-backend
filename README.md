# Fetch Backend Internship Challenge

## Setup

1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the Flask app using `python app.py`.

## API Endpoints

### Add Points
- **Route**: `/add`
- **Method**: POST
- **Request Body**:
  ```json
  {
      "payer": "DANNON",
      "points": 300,
      "timestamp": "2022-10-31T10:00:00Z"
  }```

### Spend Points
- **Route**: `/spend`
- **Method**: POST
- **Request Body**:
- **Request Body**:
  ```json
  {
    "points": 5000
  }
  ```

### Get Balance
- **Route**: `/balance`
- **Method**: GET
- **Response Body**:
  ```json
  {
    "DANNON": 1000,
    "UNILEVER": 0,
    "MILLER COORS": 5300
  }
  ```