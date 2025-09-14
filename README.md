# cf-ddns.py
Very basic CloudFlare Dynamic DNS Updater written with Python
I was fed up with my ISP changing my IP address daily so I developed this script. It's very basic. Checks my IP address, updates a DNS record in CloudFlare. If I want to access my home infrastructure, I can basically use that DNS record.

# Configuration
You need a CloudFlare account and a domain tied to it. At the top side of this script you'll find variables like dnsName, dnsTtl and proxy. You can use these params to define which DNS record you want to be updated.
authEmail, authKey, CfZoneId and CfDnsRecordId variables are related to CloudFlare API authorization. authEmail does not need any clarification but for authKey you need to go to My Profile >> API Tokens >> Global API Key.
For some reason I couldn't be able to get regular API Tokens working so I used Global API Tokens instead.
cfZoneId and CfDnsRecordId can be found either by using CloudFlare API (List DNS Records) or by using DevTools when loading CloudFlare Dashboard.
After this, you'll be able to execute this script and have that record updated. Script adds a little comment each time it updates a record to make tracking updates easier.

# Automation
On Linux you can use Crontabs. I have a Windows running small laptop so I used Task Scheduler to schedule this script to run every 5 minutes. You can find the exported task in XML format inside the repo with name cfddns-task.xml.
