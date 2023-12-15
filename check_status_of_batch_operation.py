import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import helper

batch_id = ''

client = MailchimpMarketing.Client()
client.set_config({
"api_key": "",
"server": ""
})

response = client.batches.status(batch_id)
helper.log(response)
