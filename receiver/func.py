from parliament import Context
from flask import Request
import numpy
import json
 
def main(context: Context):
    """ 
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """
    req = context.request
    if req.is_json:
      print(f"Json is {req.json}")
      return {"result":numpy.add.reduce(numpy.array(req.json),(0,1))},200	
    else: 
      return "function requires json", 400


