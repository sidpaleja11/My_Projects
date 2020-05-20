word = input("Enter a word")
y = len(word)
x = word[0:y]
z = word[::-1]

if x==z:
  print("Word = Palindrome")
  print (x + " is the same as "+z)
else:
  print("Word != Palindrome")
  print(x+ " is not the same as "+z)
