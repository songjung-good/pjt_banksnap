import requests
import json

TMDB_API_KEY = "96e8505fc0db43a660620030238b74d9"

def get_product_data():
    with open("fin_product_data.json", "w", encoding="utf-8") as w:
        pass

    total_data = []

    for i in range(1, 11):
        request_url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={TMDB_API_KEY}&topFinGrpNo=020000&pageNo={i}"
        products = requests.get(request_url).json()

        for product in products['result']['baseList']:
            if product.get('fin_prdt_cd', ''):
                fields = {
                    'fin_prdt_cd': product['fin_prdt_cd'],
                    'kor_co_nm': product.get('kor_co_nm', ''),
                    'fin_prdt_nm': product.get('fin_prdt_nm', ''),
                    'etc_note': product.get('etc_note', ''),
                    'join_deny': product.get('join_deny', ''),
                    'join_member': product.get('join_member', ''),
                    'join_way': product.get('join_way', ''),
                    'spcl_cnd': product.get('spcl_cnd', ''),
                    # 'deposit_type': product.get('deposit_type', '') //
                }

                data = {
                    "model": "products.product",
                    "fields": fields
                }

                total_data.append(data)

    with open("fin_product_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)


get_product_data()