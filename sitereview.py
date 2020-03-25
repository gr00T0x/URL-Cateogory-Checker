import requests
import re



website = input('Enter a website url: ')

url = "https://fortiguard.com/webfilter?q=" + (website)

test = requests.get(url, verify=False)  # Disable SSL due to errors with the root SSL Cert internally

text = (test.text)

regex = (re.findall(r"\"(Category.*?)\"", text)[0])  # Strip out html to find the proxy category

if regex == 'Category: Newly Observed Domain':  # Fixing issue with unresolved domains
    print('This domain is uncategorised or does not exist.')

else:
    print(regex)
