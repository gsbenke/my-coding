import requests
from currency_symbols import CurrencySymbols
from fastapi import FastAPI

app = FastAPI(docs_url="/")

# input_cur = input("Choose your input currency: ")
# target_cur = input(f"Choose a currency code to display: ")

@app.get("/currency")
def get_quote(input_cur, target_cur):
    response = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{input_cur}/{target_cur}.json")
    response_json = response.json()
    amount = response_json[target_cur]
    return f"1 {input_cur} equals to {CurrencySymbols.get_symbol(target_cur.upper())}{amount}"

# print(f"1 {input_cur} equals to {CurrencySymbols.get_symbol(target_cur.upper())}{amount}")


## TODO -> https://github.com/arshadkazmi42/currency-symbols/
## https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/nzd/vnd.json

