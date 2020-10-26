import requests
payload={'key':'v1','key2':'v2'}
r = requests.post('https://mypage.groovecoaster.jp/sp/login/auth_con.php',data=payload)
print(r.text)

