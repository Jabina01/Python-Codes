def main():
    dic = {
    'Alex': ['subj1', 'subj2', 'subj3'], 

   'David': ['subj1', 'subj2']}
    count = 0
    for key, value in dic.items():
        if isinstance(value, list):
              count += len(value)
    print(count)
      
main()






 


