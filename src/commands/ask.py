import os
import json
import wolframalpha


wolfram_api_key = os.getenv('wolfram_api_key')
client = wolframalpha.Client(wolfram_api_key)

def main(msg):
    response = search(msg)
    return response

def search(msg):
    response = client.query(msg)

    #Wolfram cannot solve the given question
    if response['@success'] == 'false':
        return ('This question cannot be resolved')
    else:
        result = ''
        pod0 = response['pod'][0]  # This is the question asked
        pod1 = response['pod'][1]  # This pod might contain the answer
        #print(json.dumps(pod0, indent=4))
        #print(json.dumps(pod1, indent=4))
        result = [pod0['subpod']['img']['@src'], pod1['subpod']['img']['@src']]
        return(result)
