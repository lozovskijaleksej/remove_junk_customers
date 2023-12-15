import requests
from datetime import datetime
import helper

def getCustomers(storeDomain, accessToken):
    junkFile = open('emails.txt', 'r')
    while True:
        email = junkFile.readline()
        if not email:
            break
        junkEmail = email.split()[0]
        response = requests.get(f'https://{storeDomain}.myshopify.com/admin/api/2023-10/customers/search.json?query=email:{junkEmail}', headers={'X-Shopify-Access-Token': accessToken})
        if response.status_code != 200:
            helper.log(f'False0:{junkEmail}')
            continue
        customers = response.json()['customers']
        if len(customers) == 0:
            helper.log(f'empty:{junkEmail}')
        for customer in customers:
            customer_id = customer.get('id', '')
            response = requests.delete(f'https://{storeDomain}.myshopify.com/admin/api/2023-10/customers/{customer_id}.json', headers={'X-Shopify-Access-Token': accessToken})
            if response.status_code != 200:
                helper.log(f'False1:{junkEmail}')
            else:
                helper.log(f'success: {junkEmail}')


def main():
    storeDomain = ''
    accessToken = ''
    getCustomers(storeDomain, accessToken)


if __name__ == '__main__':
    main()

