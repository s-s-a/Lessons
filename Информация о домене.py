import whois

def is_registered(domain_name):
  try:
    w = whois.query(domain_name)
  except Exception:
    return False
  else:
    return bool(w)

domain_name = 'italika.ru'
if is_registered(domain_name):
  whois_info = whois.query(domain_name)
  print(whois_info)
  # print(whois_info.registrar)
  # print(whois_info.whois_server)
  # print(whois_info.org)
else:
  print('Домен не зарегистрирован.')