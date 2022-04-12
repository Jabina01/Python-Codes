def to_string(n,base):
   convert_String = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if n < base:
      return convert_String[n]
   else:
      return to_string(n//base,base) + convert_String[n % base]

print(to_string(2835,16))
