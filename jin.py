import requests
from bs4 import BeautifulSoup
import json

def urlvoid():
    page = requests.get('https://www.urlvoid.com/scan/cooltechtube.com/')
    soup = BeautifulSoup(page.content, 'html.parser')
    tag = soup.find(class_="label")
    return tag.text
def zulu():
    page = requests.get('https://zulu.zscaler.com/')
    soup = BeautifulSoup(page.content, 'html.parser')
    tag = soup.find(attrs={"name": "csrf_token"})
    cookies = page.cookies.get_dict()
    csrf_token = tag["value"]
    print(1)
    data = {'url': 'Cooltechtube.com', 
            'csrf_token': csrf_token}
    # cookie = "_zulu_session=x6MFCIjf8gNTwGgRk7C0Y2VWoS6zGTxqK8IM392S8p-ZW4KY8FPinTPvrcsoK3mbzIT85UfKArc08RoLRSe-coAElUkAAAAAAAAASk3Lu2BHQdgu8f14c9p9lIwHX2NzcmZ0X5SMKGFjNzI1ZTZmOGQxOTZlMjNiYzczMWIyNTI5MWZjNjZmZGU2YzU2ZjKUc4eULg;"
    page = requests.post("https://zulu.zscaler.com/", data=data, cookies=cookies)
    print(2)
    soup = BeautifulSoup(page.content, 'html.parser')
    tag = soup.find(class_="result")
    print(tag.prettify())
def whois(domain):
    url = "https://hostadvice.com/marketshare.php?sentFrom=https%3A%2F%2Fhostadvice.com%2Ftools%2Fwhois%2F%23" + domain + "&action=getWhoisQueue&q=" + domain + "&recaptcha_response="
    page = requests.get(url)
    response = json.loads(page.content)
    print(1)
    url = "https://hostadvice.com/marketshare.php?action=getWhoisQueueStatus&queue_id=" + str(response["queue_id"])
    while(1):
        page = requests.get(url)
        response = json.loads(page.content)
        if(response["status"] == "complete"):
            return response["ip"]
        elif(response["status"] == "pending"):
            continue
        else:
            print("error")
            break
def virustotal(domain):
    url = "https://www.virustotal.com/ui/search?limit=20&relationships%5Bcomment%5D=author%2Citem&query="+domain
    url = "https://www.virustotal.com/ui/search?limit=20&relationships%5Bcomment%5D=author%2Citem&query=samsung-updates.cc"
    page = requests.get(url)
    print(page)
    response = json.loads(page.content)
    return response["data"][0]["attributes"]["last_analysis_stats"]["malicious"]

def rest(domain):
    url = "https://www.whois.com/whois/healthcautions.com"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tag = soup.find(class_='df-row')
    return tag.prettify()
print(rest("Cooltechtube.com"))