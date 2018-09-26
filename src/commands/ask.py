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
        png_result = []
        result = []
        pods = []
        try:
            pod0 = response['pod'][0]  # This is the question asked
            pods.append(pod0)
            pod1 = response['pod'][1]  # This pod might contain the answer
            pods.append(pod1)
            pod2 = response['pod'][2]  # This pod might contain the answer
            pods.append(pod2)
            print(json.dumps(pod0, indent=4))
            print(json.dumps(pod1, indent=4))
            print(json.dumps(pod2, indent=4))
        except IndexError:
            pass

        try:
            result = [resolve_ls_or_dict(pod) for pod in pods ]
            print(result)
            for r in result:
                png_result.append(r.replace('/gif','/png'))
            return(png_result)
        except TypeError as e:
            return('JSON indice error. Report this!\n.James needs to check log reports.\nConsole output: %s'%e )

def resolve_ls_or_dict(pod):
    if isinstance(pod['subpod'], list):
        return pod['subpod'][0]['img']['@src']
    else:
        return pod['subpod']['img']['@src']
