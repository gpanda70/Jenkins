import os
import json
import wolframalpha
from src.error import meme_error

wolfram_api_key = os.getenv('wolfram_api_key')
client = wolframalpha.Client(wolfram_api_key)

def main(msg):
    response = search(msg)
    return response

def search(msg):
    """This function sends a question to the WolframAlpha api and returns a response"""

    response = client.query(msg)

    # Wolfram cannot solve the given question
    if response['@success'] == 'false':
        return ('This question cannot be resolved\n\n%s' %(meme_error))
    else:
        png_result = []
        result = []
        pods = []

        # If there is no secondary response(pod2) it will catch an IndexError
        try:
            pod0 = response['pod'][0]  # This is the question asked
            pods.append(pod0)
            pod1 = response['pod'][1]  # This pod might contain the answer
            pods.append(pod1)
            pod2 = response['pod'][2]  # This pod might contain the answer
            pods.append(pod2)
            #print(json.dumps(pod0, indent=4))
            #print(json.dumps(pod1, indent=4))
            #print(json.dumps(pod2, indent=4))
        except IndexError:
            pass

        # Checks if JSON object has some sort of IndiceError based on
        # if it contains a JSON Array or not.
        try:
            result = [resolve_ls_or_dict(pod) for pod in pods ]
            print(result)
            for r in result:
                png_result.append(r.replace('/gif','/png'))
            return(png_result)
        except TypeError as e:
            return('JSON indice error. Report this!\n.James needs to check log reports.\nConsole output: %s'%e )

def resolve_ls_or_dict(pod):
    """Checks to make sure if the pod is a JSON Object(Dict) or JSON Array(ls)"""

    if isinstance(pod['subpod'], list):
        return pod['subpod'][0]['img']['@src']
    else:
        return pod['subpod']['img']['@src']
