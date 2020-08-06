import requests

proxies={
    'https':'18.218.173.238:3838',
    'http':'18.218.173.238:3838'
}

url = 'https://httpbin.org/ip'


resp=requests.get(url,proxies=proxies)
print(resp.json())
print(resp.text)

#The code from below is to show your public IP if you want to check thats the program work, you have tu run it in a diferrent file
# import requests
# 
# url = 'https://httpbin.org/ip'
# 
# resp=requests.get(url)
# print(resp.json())
# print(resp.text)
