import requests, os

URL_EMBAJADA = os.getenv("URL_EMBAJADA")
CEDULA_IDENTIDAD = os.getenv("CEDULA_IDENTIDAD")
WSP_API_URL = os.getenv("WSP_API_URL")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
WSP_API_KEY = os.getenv("WSP_API_KEY")
headers_req_embajada = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
, "content-type": "application/x-www-form-urlencoded", 
"accept-language": "en,es-419;q=0.9,es;q=0.8"

}
params_req_embajada ={"cedula": CEDULA_IDENTIDAD, "buscar": "Consultar"}

def lambda_handler(event, context):
    response_req_embajada = requests.post(URL_EMBAJADA,data=params_req_embajada, headers=headers_req_embajada)
    if(response_req_embajada.status_code) >= 400:
        return {"message" : "ERROR: The request to the embassy has failed"}
    for c in response_req_embajada.iter_lines():
        primera_linea_response = str(c)
        break
    mensaje_embajada = primera_linea_response[primera_linea_response.find("(")+1:primera_linea_response.find(")")]
    WSP_API_REQ = f"{WSP_API_URL}?phone={PHONE_NUMBER}&text={mensaje_embajada}&apikey={WSP_API_KEY}"
    wsp_api_response = requests.get(WSP_API_REQ)
    return {"message" : "OK" if (wsp_api_response.status_code) in (200, 201) else "ERROR: The callmebot API has failed" }
