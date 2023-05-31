from parliament import Context
from flask import Request
import json
import torch
import numpy
 
def main(context: Context):
    """ 
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """

    # Add your business logic here
    print(f"Received request {context.request.args}")
    x = 3
    y = 3
    try: 	
      x = int(context.request.args["x"]);
      y = int(context.request.args["y"]);
    except (KeyError,ValueError): 
      print (f"using default dimension ({x},{y})")
    
    return torch.rand(x,y).numpy().tolist(), 200
