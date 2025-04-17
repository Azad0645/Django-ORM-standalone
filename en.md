# Bank security console

Project description:
- The security console is an internal repository for bank employees, allowing to track their passes. 

## How to install 

Create .env file in the project root folder and fill it with the following environment variables:
- DB_ENGINE=Backend for connecting to the database
- DB_HOST=Database server address
- DB_PORT=Port for connecting to the database
- DB_NAME=Database name
- DB_USER=Username
- DB_PASSWORD=User password 
- SECRET_KEY=Secret key

Installing dependencies:
- Python 3 must already be installed.

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python main.py
```

## Project goal

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org).