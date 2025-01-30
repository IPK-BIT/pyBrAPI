import requests

def __collect_results__(url, headers, params):
    if "pageSize" not in params:
        params["pageSize"] = 1000
    if "page" not in params:
        params["page"] = 0
        
    response = __get_page__(url, headers, params)
    # print(f'collecting page {params["page"]+1}/{response["metadata"]["pagination"]["totalPages"]}')
    if "headerRow" in response["result"]:
        result = response["result"]
        while params["page"] < response["metadata"]["pagination"]["totalPages"]-1:
            params["page"] += 1
            result["data"].extend(__get_page__(url, headers, params)["result"]["data"])
            # print(f'collecting page {params["page"]+1}/{response["metadata"]["pagination"]["totalPages"]}')
    elif "data" in response["result"]:
        result: list = response["result"]["data"]
        while params["page"] < response["metadata"]["pagination"]["totalPages"]-1:
            params["page"] += 1
            result.extend(__get_page__(url, headers, params)["result"]["data"])
    else:
        result = response["result"]    
    return result
                
def __get_page__(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()