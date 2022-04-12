# dic = {"name":"raju","marks":56}
# def is_key_present(x):
#   if x in dic:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# is_key_present("name")
# is_key_present("class")



dic={"name":"raju","marks":56}
def is_key_present():
    key=input("enter the key")
    if key in dic:
      print('Key is present in the dictionary')
    else:
      print('Key is not present in the dictionary')
is_key_present()