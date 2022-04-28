import sys
import requests
import urllib.parse
import re , os
import random
import uuid
import traceback
from jokes import jokes_arr

dump_file = False

joke_mode = False

def parse_arguments(arr, argument, bool=False):
    for i, val in enumerate(arr):
        if val.replace("-", "") == argument:
            if bool:
                return True
            if i+1 == len(arr):
                print(f":ERROR: No Value Passed for Argument: `{argument}`")
                raise Exception("NoValueForArgument")
            return arr[i+1]
    raise Exception("ArgumentNotFound")

def dump_to_console(s,offset=0):
    for i in s:
        if i == "\n":
            print(i+" " * offset, end = "")
        else:
            print(i , end="")

def get_joke():
    return jokes_arr[random.randint(0,len(jokes_arr)-1)]

def usage(exit_code):
    print(f"\nUsage: python {sys.argv[0]} '<search-query>' [option]")
    print("\nOPTIONS:")
    print("   --save : Save Result to File")
    print("   --joke : Turn Joke mode On/Off")
    print("   --help : Print this help and exit")
    print()
    if exit_code != None:
        sys.exit(exit_code)

def dump_to_file(file_path,s):
    try:
        if os.path.exists(file_path):
            file_name = file_path[:(file_path.rindex("."))]
            file_path = f"{file_name}_{str(uuid.uuid4())[:10]}.txt"
        with open(file_path,'w') as f:
            f.write(s)
        print(f"\nResult Saved in '{file_path}'\n")
    except Exception as e:
        print(e)
        print("\n\n OOPS .. Writing to file failed")

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        usage(1)
    try:
        if parse_arguments(sys.argv , "help", True):
            usage(0)
    except Exception as e:
        pass
    
    try:
        dump_file = parse_arguments(sys.argv , "save" , True)
    except Exception as e:
        pass

    try:
        joke_mode = parse_arguments(sys.argv, "joke" , True)
    except Exception as e:
        pass

    query = sys.argv[1]
    query_url_encoded = urllib.parse.quote_plus(query)

    try:
        print("\n------------------------------------------ ")
        print(f"\n Searching for '{query}' in cheat.sh...")
        print("\n------------------------------------------ ")
        if joke_mode:
            print(f"\n Meanwhile here's a joke while you cheat")
            print("\n------------------------------------------ ")
            dump_to_console(get_joke(),2)
        print("\n------------------------------------------ ")
        print()
        r = requests.get(f"http://cheat.sh/{query_url_encoded}")
        if r.status_code != 200:
            raise("Not200Response")
        print(f"...Fetched Results :::")
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        result = ansi_escape.sub('', str(r.text))
        print("\n------------------------------------------")
        dump_to_console(result)
        print("\n------------------------------------------ ")
        if dump_file:
            dump_to_file(f"query_{query.replace(' ','_')}.txt",result)

    except Exception as e:
        print(e)
        print("""------------------------------------------\n
    {-_-} OOPS \n
        ... ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
        ... ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>
        ... ¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º> \n
    Something Went Fishy...\n
    Meanwhile look for your internet or 
    VPN settings as http request is being 
    sent from this script to URL :
    http://cheat.sh/
    \n------------------------------------------\n""")