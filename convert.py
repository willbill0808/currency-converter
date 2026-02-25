import requests, json

key = "41fbc09ec63832a7ac810d4d"
GC = "USD" #Given Currency
WRC = "NOK" # Wanted Returned Currency
amount = 40




def API_request(key, GC, WRC, amount):
    url = f"https://v6.exchangerate-api.com/v6/{key}/latest/{GC}"

    response = requests.get(url) 
    data = response.json() 
    if data["result"]:  
        print(f"[TERMINAL] Status: Success")  
    else:
        print(f"[TERMINAL] Status: Failure") 
    
    GCV = amount * data["conversion_rates"][GC] #Given Currency Value
    print(f"[TERMINAL] {GC} = {GCV}")

    WRCV = amount * data["conversion_rates"][WRC] #Wanted Returned Currency Value
    print(f"[TERMINAL] {WRC} = {WRCV}")

API_request(key, GC, WRC, amount)
