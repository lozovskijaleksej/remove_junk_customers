import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import helper

batch_id = 'cojgq8dsmw'

client = MailchimpMarketing.Client()
client.set_config({
"api_key": "83910b2d7916f8275aa94ef881bd4d8f-us7",
"server": "us7"
})

response = client.batches.status(batch_id)
helper.log(response)