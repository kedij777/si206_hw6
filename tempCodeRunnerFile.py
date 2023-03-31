response = requests.get(url, params)
    if response != None:
        data = response.text
        in_dict = json.loads(data)
        return in_dict
    else :
        print("Exception")
        return None
