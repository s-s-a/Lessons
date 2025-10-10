# Код для проверки срока действия SSL-сертификата на Python

# Для проверки SSL-сертификата в коде используется библиотека ssl, для работы с сетевыми соединениями 
# и сокетами используется библиотека socket.

import ssl
import socket
from datetime import datetime, timezone


def check_ssl(hostname, port=443):
    context = ssl.create_default_context()

    try:
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                print(f"Сертификат для: {hostname}")
                print(f"Организация: {cert.get('issuer')}")
                print(f"Выдан: {cert.get('notBefore')}")
                print(f"Действителен до: {cert.get('notAfter')}")

                # Проверка срока действия с timezone-aware объектом
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                not_after = not_after.replace(tzinfo=timezone.utc)
                if not_after < datetime.now(timezone.utc):
                    print("Сертификат просрочен!")
                else:
                    print("Сертификат действителен")
    except Exception as e:
        print(f"Ошибка при проверке SSL: {e}")


if __name__ == "__main__":
    check_ssl("example.com")
