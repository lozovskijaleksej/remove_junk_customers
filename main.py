import requests
from datetime import datetime


def log(message):
    logFile = open("history.log", "a")
    logFile.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] : {message}\n')


def getCustomers(storeDomain, accessToken):
    junkEmails = {}
    junkFile = open('emails.txt', 'r')
    while True:
        email = junkFile.readline()
        if not email:
            break
        junkEmail = email.split()[0]
        response = requests.get(f'https://{storeDomain}.myshopify.com/admin/api/2023-10/customers/search.json?query=email:{junkEmail}', headers={'X-Shopify-Access-Token': accessToken})
        if response.status_code != 200:
            log(f'False0:{junkEmail}')
            continue
        customers = response.json()['customers']
        for customer in customers:
            customer_id = customer.get('id', '')
            response = requests.delete(f'https://{storeDomain}.myshopify.com/admin/api/2023-10/customers/{customer_id}.json', headers={'X-Shopify-Access-Token': accessToken})
            if response.status_code != 200:
                log(f'False1:{junkEmail}')
            else:
                log(f'success: {junkEmail}')


def main():
    storeDomain = 'pipetto-4a54'
    accessToken = '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'
    getCustomers(storeDomain, accessToken)


if __name__ == '__main__':
    main()

