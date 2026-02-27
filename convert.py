import requests, json
import FreeSimpleGUI as sg

key = "41fbc09ec63832a7ac810d4d"
GC = "USD" #Given Currency
WRC = "NOK" # Wanted Returned Currency
amount = 40

def ValidCheck(Value1, Value2, Value3):
    print(f"\n[TERMINAL][CHECK] Testing...")
    print(f"[TERMINAL][CHECK] Recived {Value1 = } {Value2 = } {Value3 = }")
    Valid1 = False
    Valid2 = False
    Valid3 = False

    for i in CurrencyList:
        if Value1 == i:
            Valid1 = True
        if Value2 == i:
            Valid2 = True  
    
    try:
        Value3 = float(Value3)
        Valid3 = True
    
    except:
        Valid3 = False 
    

    print(f"[TERMINAL][CHECK] Done! Returning: {Valid1, Valid2}")
    return Valid1, Valid2, Valid3, Value3
        
    

def MakeList():
    print(f"[\nTERMINAL][MAKE_LIST] Starting...")

    url = f"https://v6.exchangerate-api.com/v6/{key}/latest/AED"

    response = requests.get(url) 
    data = response.json() 

    if data["result"]:  
        print(f"[TERMINAL][MAKE_LIST] Status: Success")  
    else:
        print(f"[TERMINAL][MAKE_LIST] Status: Failure") 

    countries = data['conversion_rates'] 

    CurrencyList = []

    for x in countries:
        CurrencyList.append(x) 
    
    print(f"[TERMINAL][MAKE_LIST] Done! Returning: {CurrencyList}")
    return CurrencyList


def GetValue(key, GC, WRC, amount):
    print(f"\n[TERMINAL][GET_VALUE] Starting...")

    url = f"https://v6.exchangerate-api.com/v6/{key}/latest/{GC}"

    response = requests.get(url) 
    data = response.json() 
    if data["result"]:  
        print(f"[TERMINAL][GET_VALUE] Status: Success")  
    else:
        print(f"[TERMINAL][GET_VALUE] Status: Failure") 
    
    GCV = amount * data["conversion_rates"][GC] #Given Currency Value
    print(f"[TERMINAL][GET_VALUE] {GC} = {GCV}")

    WRCV = amount * data["conversion_rates"][WRC] #Wanted Returned Currency Value
    print(f"[TERMINAL][GET_VALUE] {WRC} = {WRCV}")

    print(f"[TERMINAL][GET_VALUE]] Done! Returning: {GCV, WRCV}")
    return GCV, WRCV

CurrencyList = MakeList()

#CurrencyList = ['USD', 'NOK', 'GBP']

event = None

layout1 = [
        [sg.Text("Which currency would you like to convert from:", key='-Disp1-')],
        [sg.Combo(CurrencyList, default_value='NOK', key='-Cur1-', readonly = True)],
        [sg.Text("Which currency would you like to convert to:", key='-Disp2-')],
        [sg.Combo(CurrencyList, default_value='USD', key='-Cur2-', readonly = True)],
        [sg.Text("What should the base currency be:", key='-Text3-')],
        [sg.Input(key='-Amount-')],
        [sg.Text("your answer will be displayed here", key='-Output-')],
        [sg.OK("Finish", key='-Finish-'), sg.OK("End", key='-End-')]
        ]

window = sg.Window('Currency_Converter', layout1)


while event != "-End-":
    
    print(f"\n[TERMINAL][WINDOW] Starting new loop")
    event, values = window.read()
    print(f"[\nTERMINAL][WINDOW] {event = }")
    print(f"[TERMINAL][WINDOW] {values = }")

    if event == "-Finish-":
        Valid1, Valid2, Valid3, Value3 = ValidCheck(values["-Cur1-"], values["-Cur2-"], values["-Amount-"])

        if Valid1 == False:
            window["-Disp1-"].update("Which currency would you like to convert from (Must be a valid answer picked from the box):")
        else:
            window["-Disp1-"].update("Which currency would you like to convert from:")
        
        if Valid2 == False:
            window["-Disp2-"].update("Which currency would you like to convert to (Must be a valid answer picked from the box):")
        else:
            window["-Disp2-"].update("Which currency would you like to convert to:")
        
        if Valid3 == False:
            window["-Text3-"].update("What should the base amount be (Must be a valid number):")
        else:
            window["-Text3-"].update("What should the base amount be:")

        if Valid1 and Valid2 and Valid3:
            GCV, WRCV = GetValue(key, values["-Cur1-"], values["-Cur2-"], Value3)
            window["-Output-"].update(f"{GCV} {values["-Cur1-"]} is {WRCV} in {values["-Cur2-"]} ")



            
        

        
    
    
window.close()
