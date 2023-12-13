import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import helper

junkFile = open('emails.txt', 'r')
try:
    client = MailchimpMarketing.Client()
    client.set_config({
    "api_key": "07134cbb1ea260e7dbbdc7a666e0e93a-us7",
    "server": "us7"
    })

    response = client.automations.list()
    while True:
        email = junkFile.readline()
        if not email:
            break
        junkEmail = email.split()[0]
        for automation in response['automations']:
            automation_id = automation.get('id', '')
            try:
                response = client.automations.remove_workflow_email_subscriber(automation_id, {"email_address": junkEmail})
                if response.status_code == 200:
                    helper.log(f'success: {junkEmail}')
                else:
                    helper.log(f'failed or empty: {junkEmail}')
            except ApiClientError as error:
                helper.log("Error: {}".format(error.text))

except ApiClientError as error:
    helper.log("Error: {}".format(error.text))
