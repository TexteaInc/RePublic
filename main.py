from pydatafront.decorator import textea_export

def triple(x:int): # this function should NOT be hosted
  return x*3

@textea_export()  # use all default settings
def triple_plus(x:int):  # this function should be hosted at redstone.textea.io/USER_NAME/PROJECT_NAME/FUNCTION_NAME
  return triple(x)+1 


