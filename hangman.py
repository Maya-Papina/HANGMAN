import random

print("H A N G M A N")

def menu():
  while True:
    usr_input = str(input('Type "play" to play the game, "exit" to quit:'))
    if usr_input == 'play':
      print()
      game()
    elif usr_input == 'exit':
      return 




def game():
  game_list = ['python', 'java', 'kotlin', 'javascript']
  secret_word = random.choice(game_list)
  hyphen_list = ['-' for i in range(len(secret_word))]
  print(''.join(hyphen_list))
  tries = 8
  wrong_guessed_list = []
  while tries > 0: 

    let = input("Input a letter:")
    res = ''.join(hyphen_list)
    if len(let) > 1:
      #wrong_guessed_list.append(let[0])
      print('You should input a single letter')
      print()
      print(res)
    elif let.isupper():
      print('Please enter a lowercase English letter')
      print()
      print(res)
    elif len(let) > 1:
      #wrong_guessed_list.append(let[0])
      print('You should input a single letter')
      print()
      print(res)
    elif not let.isalpha():
      print('Please enter a lowercase English letter')
      print()
      print(res)
      
      
    elif let in wrong_guessed_list:
      print("You've already guessed this letter")
      print()
      print(res)

    elif let in secret_word:
      if let in hyphen_list:
        print("You've already guessed this letter")
        print()
        print(res)
      else: 
        for i in range(len(secret_word)):
          if secret_word[i] == let:
            hyphen_list.insert(i,let)
            hyphen_list.pop(i+1)
        res = ''.join(hyphen_list)
        print('\n',res)
        if ''.join(hyphen_list) == secret_word:
          print(f"You guessed the word {secret_word}!\n","You survived!")
          break
    else:
      if tries > 1:
        print("That letter doesn't appear in the word")
        print()
        print(res)
        wrong_guessed_list.append(let)
        tries -= 1
      else:
        print("That letter doesn't appear in the word")
        print('You lost!')
        print()
        return 

menu()
