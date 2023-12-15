import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import helper

try:
    client = MailchimpMarketing.Client()
    client.set_config({
    "api_key": "",
    "server": ""
    })
    response = client.lists.get_all_lists()
    for audience in response['lists']:
        if audience.get('name', '') == 'Product Registration':
            continue
        junkFile = open('emails.txt', 'r')
        operations = []
        index = 0
        while True:
            email = junkFile.readline()
            if not email:
                break
            junkEmail = email.split()[0]
            index += 1
            operation = {
                "method": "POST",
                "path": f"/lists/{audience.get('id', '')}/members/{helper.get_subscriber_hash(junkEmail)}/actions/delete-permanent",
                "operation_id": f'{index}'
            }
            operations.append(operation)
        payload = {
            "operations": operations
        }

        response = client.batches.start(payload)
        helper.log(response)
        junkFile.close()

except ApiClientError as error:
    helper.log("Error: {}".format(error.text))
