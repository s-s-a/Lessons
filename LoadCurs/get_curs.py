"""Загрузка курсов валют с сайта ЦБ РФ"""

from datetime import datetime, timedelta

import niquests as requests  ## https://dzen.ru/a/Zfcf99UUziZwqoS_
# import requests
import xmltodict

# """Данные только на сегодня, но по всем валютам"""
# data = requests.get("https://www.cbr-xml-daily.ru/daily_json.js", timeout=5).json()
# print(data["Valute"]["USD"]["Value"])
# print(data["Valute"]["EUR"]["Value"])


FromDate: str = (datetime.now() + timedelta(days=-5)).strftime("%Y-%m-%d")  # "2025-04-09"
ToDate: str   = (datetime.now() + timedelta(days= 1)).strftime("%Y-%m-%d")  # "2024-07-02"

Valutes: dict = {"USD": "R01235", "EUR": "R01239"}

for valuta, code in Valutes.items():
    content = (
        '<?xml version="1.0" encoding="utf-8"?>'
        + "<soap12:Envelope"
        + ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        + ' xmlns:xsd="http://www.w3.org/2001/XMLSchema"'
        + ' xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">'
        + " <soap12:Body>"
        + ' <GetCursDynamicXML xmlns="http://web.cbr.ru/">'
        + f"<FromDate>{FromDate}T00:00:00</FromDate>"
        + f"<ToDate>{ToDate}T00:00:00</ToDate>"
        + f"<ValutaCode>{code}</ValutaCode>"
        + " </GetCursDynamicXML>"
        + " </soap12:Body>"
        + "</soap12:Envelope>"
    )

    header_params: dict[str, str] = {
        "POST": "/DailyInfoWebServ/DailyInfo.asmx HTTP/1.1",
        "Host": "www.cbr.ru",
        "Content-Type": "application/soap+xml; charset=utf-8",
        "Content-Length": f"{len(content)}",
    }

    response = requests.post(
        "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx",
        headers=header_params,
        data=content,
        timeout=5,
    ).text
    body = xmltodict.parse(response)["soap:Envelope"]["soap:Body"][
        "GetCursDynamicXMLResponse"
    ]["GetCursDynamicXMLResult"]["ValuteData"]["ValuteCursDynamic"]

    print(valuta)
    for valute in body:
        print(valute["CursDate"][:10], valute["Vcurs"])
