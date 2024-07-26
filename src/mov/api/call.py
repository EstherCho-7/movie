def req(dt="20120101"):
    base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key="b721f4d7ddcc1435fabb6c21e6522bd9"

    url=f"{base_url}?key={key}&targetDt={dt}"
    print(url)

