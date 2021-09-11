import requests

url = "https://linguatools-sentence-generating.p.rapidapi.com/realise"

querystring = {"object":"thief","subject":"police","verb":"arrest"}

headers = {
    'x-rapidapi-host': "linguatools-sentence-generating.p.rapidapi.com",
    'x-rapidapi-key': "19f9a261f5mshdaaf092fcd12168p11148cjsna15442d10392"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)