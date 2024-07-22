import requests

# URL and endpoint
url = "https://gemini.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate?bl=boq_assistant-bard-web-server_20240717.08_p4&f.sid=5044628581015328532&hl=en&_reqid=1410701&rt=c"

# Headers defined in your request
headers = {
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "accept": "*/*",
    "origin": "https://gemini.google.com",
    "referer": "https://gemini.google.com/",
    # Add more headers like cookies as needed
    "cookie": "_gcl_au=$GCL_AU; _ga=$GA; AEC=$AEC; ... (include other cookies as needed)"
}

# Body of the request with the new prompt for olives, assuming similar structure as asiatic lions
data = {
    "f.req": "[null, \"[[\\\"Tell me about olives\\\",0,null,null,null,null,0],[\\\"en\\\"]]\"]",
    "at": "Your_At_Token_Here"  # Replace 'Your_At_Token_Here' with the actual 'at' token value if it is required to be dynamic or fetched from elsewhere
}

# Making the POST request
response = requests.post(url, headers=headers, data=data)

# Printing the response from the server
print(response.status_code)
print(response.text)