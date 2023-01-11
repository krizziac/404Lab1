'''
Resource used:
Author: Documentation page for "Request" library (no sole author)
Link: https://requests.readthedocs.io/en/latest/user/quickstart/

Resource was mainly used to find the method that prints content of
raw url link 

'''
import requests

#script to print out version of requests library
#print(requests.__version__)

#script to use GET
#print(requests.get("http://google.com/"))

request = requests.get("https://raw.githubusercontent.com/krizziac/404Lab1/main/lab1_scripts.py")

request.text
