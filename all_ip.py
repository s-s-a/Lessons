# Код для получения всех IP-адресов, связанных с хостом на Python
# Для получения всех IP-адресов, связанных с хостом на Python используем метод gethostbyname_ex
import socket

hostname = 'www.italika.ru' # 'www.google.com'
ip_addresses = socket.gethostbyname_ex(hostname)[2]
ip_addresses.sort()

for ip in ip_addresses:
    print(ip)

# Вывод:
# 173.194.221.99
# 173.194.221.106
# 173.194.221.104
# 173.194.221.147
# 173.194.221.103
# 173.194.221.105