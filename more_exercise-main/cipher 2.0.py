def encrypt():

  message=input("enter the message ")
  message = input("Enter the message you want to encrypt")

  ascii_message = [ord(char)+3 for char in message]

  encrypt_message = [ chr(char) for char in ascii_message]  

  print (''.join(encrypt_message))
encrypt()



def decrypt():

  message = input("Enter the message you want to decrypt")

  ascii_message = [ord(char) for char in message]

  decrypt_message = [ chr(char) for char in ascii_message]  

  print (''.join(decrypt_message))
decrypt()

flag = True

while flag == True:
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
    if choice =='e':
      
      encrypt()

    else:
        choice == 'd'

        decrypt()    

  # else:

    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")

    if play_again == 'Y':
      continue

    else:
      play_again == 'N'

      break