from datetime import datetime
import hashlib


def log(message):
    logFile = open("history.log", "a")
    logFile.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] : {message}\n')


def get_subscriber_hash(email):
    email = email.lower()
    md5_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
    return md5_hash