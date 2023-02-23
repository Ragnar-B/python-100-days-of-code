alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
output = []

def encrypt(text, shift):
  for letter in text:
    shifted = alphabet.index(letter) + shift
    if shifted > 25:
      shifted -= 26
    output.append(alphabet[shifted])
  print(f"The encoded text is {''.join(output)}")

def decrypt(text, shift):
  for letter in text:
    shifted = alphabet.index(letter) - shift
    if shifted < 0:
      shifted += 26
    output.append(alphabet[shifted])
  print(f"The decoded text is {''.join(output)}")

if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
   print("You haven't entered encode or decode.\nPlease try again.")
