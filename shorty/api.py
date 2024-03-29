from flask import Blueprint, jsonify, request, json
from shorty.providers.provider_proxy import ProviderProxy
import bleach

api = Blueprint('api', __name__)

@api.route('/shortlinks', methods=['POST'])

def create_shortlink():
    response: dict = {}
    status: int = 200
    
    if __validateRequestIsJson():
        inputIsValidated: dict = __validateInput(request.json)

        if inputIsValidated['success'] != False:
            url = bleach.clean(request.json['url'])
            providerName: str = bleach.clean(request.json['provider'])
            providerProxy  = ProviderProxy(url, providerName)
            response = providerProxy.callProvider()
        else:
            response = inputIsValidated
    else:
        response['success'] = False
        response['message'] = 'Please provide a json object!'

    if "status" in response:
        status = response['status']    

    return jsonify(response) , status

def __validateRequestIsJson():
    try:
        jsonObject = json.dumps(request.json)
        return json.loads(jsonObject) and request.headers.get('content-type') == 'application/json'
    except:
        return False

def __validateInput(data: dict) -> dict:
    response:dict = {'success': True}

    if "url" not in data or "provider" not in data:
        response['success'] = False
        response['message'] = 'Url field and provider fields are required!'
        return response

    if type(data['url']) != str or type(data['provider']) != str:
        response['success'] = False
        response['message'] = 'Url field and provider field must be strings!'  
        return response; 

    if len(data['url']) == 0:
        response['success'] = False
        response['message'] = 'You must provide a url!'

    return response  