import requests
from datetime import datetime


def log(message):
    logFile = open("history.log", "a")
    logFile.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] : {message}\n')


def getCustomers(storeDomain, accessToken):
    since_id = 0
    while True:
        response = requests.get(f'https://{storeDomain}.myshopify.com/admin/api/2023-10/customers.json?since_id={since_id}', headers={'X-Shopify-Access-Token': accessToken})
        old_since_id = since_id
        if response.status_code != 200:
            return False
        customers = response.json()['customers']
        for customer in customers:
            customer_id = customer.get('id', '')
            customer_email = customer.get('email', '')
            print(f'{customer_id} -> {customer_email}')
            since_id = customer_id
        if old_since_id == since_id:
            break


def main():
    storeDomain = 'pipetto-4a54'
    accessToken = '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'
    getCustomers(storeDomain, accessToken)


if __name__ == '__main__':
    main()

