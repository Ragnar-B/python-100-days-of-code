from art import logo

def caesar(text, shift, direction):
  output = []
  for letter in text:
    if letter not in alphabet:
      output.append(letter)
    else: 
      if direction == "encode":
        shifted = alphabet.index(letter) + shift
      elif direction == "decode":
        shifted = alphabet.index(letter) - shift
      if shifted > 25:
        shifted -= 26
      elif shifted < 0:
        shifted += 26
      output.append(alphabet[shifted])
  if direction == "encode":
    print(f"The encoded text is {''.join(output)}")
  elif direction == "decode":
    print(f"The decoded text is {''.join(output)}")
  else:
    print("You haven't entered encode or decode.\nPlease try again.")
     
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

running = "yes"
while running == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift %=  26
  caesar(text, shift, direction)
  running = input("Would you like to continue? Type yes or no.")