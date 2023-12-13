import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import helper

junkFile = open('emails.txt', 'r')
try:
    client = MailchimpMarketing.Client()
    client.set_config({
    "api_key": "a798797295e3c50a41ab43ec77a81f6c-us7",
    "server": "us7"
    })
    response = client.lists.get_all_lists()
    while True:
        email = junkFile.readline()
        if not email:
            break
        junkEmail = email.split()[0]
        for audience in response['lists']:
            audience_id = audience.get('id', '')
            try:
                client.lists.delete_list_member_permanent(audience_id, helper.get_subscriber_hash(junkEmail))
                helper.log(f"Success: {junkEmail}")
            except ApiClientError as error:
                helper.log(f"Failed: {junkEmail}")

except ApiClientError as error:
    helper.log("Error: {}".format(error.text))
