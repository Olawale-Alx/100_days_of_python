# Encrypting and Decrypting

from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!']

print(logo)

start = True

while start:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

  def caesar(plain_text, shift_amount, direction):
    if direction == 'encode':
      cipher_text = ""
      for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
      print(f"The encoded text is {cipher_text}")

    if direction == 'decode':
      cipher_text = ""
      for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        cipher_text += alphabet[new_position]
      print(f"The decoded text is {cipher_text}")

  caesar(plain_text=text, shift_amount=shift, direction=direction)

  restart = input('Type yes to restart, no to exit:\n')

  if restart == 'yes':
    start = True
  
  else:
    start = False
    print('Goodbye!!!')
