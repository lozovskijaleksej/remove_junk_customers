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
        junkEmails.update({email.split()[0]:True})
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
            try:
                junkEmails[customer_email]
                response = requests.delete(f'https://{storeDomain}.myshopify.com/admin/api/2023-10/customers/{customer_id}.json', headers={'X-Shopify-Access-Token': accessToken})
                if response.status_code == 200:
                    log(f'{customer_email} : True : True')
                else:
                    log(f'{customer_email} : True : False')
            except:
                log(f'{customer_email} : False')
            since_id = customer_id
        if old_since_id == since_id:
            break


def main():
    storeDomain = 'pipetto-4a54'
    accessToken = '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'
    getCustomers(storeDomain, accessToken)


if __name__ == '__main__':
    main()

