import requests

url = "https://eyme.eyadvisory.cn/timesheet/save"

headers = {
    "Host": "eyme.eyadvisory.cn",
    "AC-Token": "<PLEASE REPLACE WITH YOUR AC-TOKEN>",
    "content-type": "application/json",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x1800282a) NetType/WIFI Language/en",
    "Referer": "https://servicewechat.com/wx3e1fc56fa9f22a80/55/page-frame.html",
}

data = {
    "city": "<PLEASE REPLACE WITH YOUR CITY>",
    "country": "<PLEASE REPLACE WITH YOUR COUNTRY>",
    "dateType": "0",
    "myHealth": "一切正常",
    "district": "<PLEASE REPLACE WITH YOUR DISTRICT>",
    "province": "<PLEASE REPLACE WITH YOUR PROVINCE>",
    "timesheetInfos": [
        {
            "timeType": "Regular time",
            "type": "Chargeable",
            "code": "<PLEASE REPLACE WITH YOUR CHARGE CODE>",
            "activity": "General (0000)",
            "hours": "8.0",
            "description": None,
        }
    ],
}

response = requests.post(url, json=data, headers=headers)

print("Response Status Code:", response.status_code)
print("Response Content:", response.content.decode("utf-8"))
