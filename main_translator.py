#@title
import random
select = input("encrypt or decrypt? ")



#-----------------------------------------------ENCRYPTION------------------------------------------------------
if select == ("e"):
  encrypt_input = input("enter text: ").lower() #takes user imput to be encrypted
  
#                                             WORD TO MORSE

  morse_version = []
  for i in range(len(encrypt_input)):


    if encrypt_input[i] == "a":  # does the letter "a"
       morse_version.append(".-")

    elif encrypt_input[i] == "b":  # does the letter "b"
      morse_version.append("-...")

    elif encrypt_input[i] == "c":  # does the letter "c"
      morse_version.append("-.-.")

    elif encrypt_input[i] == "d":  # does the letter "d"
      morse_version.append("-..")

    elif encrypt_input[i] == "e":  # does the letter "e"
      morse_version.append(".")

    elif encrypt_input[i] == "f":  # does the letter "f"
      morse_version.append("..-.")

    elif encrypt_input[i] == "g":  # does the letter "g"
      morse_version.append("--.")

    elif encrypt_input[i] == "h":  # does the letter "h"
      morse_version.append("....")

    elif encrypt_input[i] == "i":  # does the letter "i"
      morse_version.append("..")

    elif encrypt_input[i] == "j":  # does the letter "j"
      morse_version.append(".---")

    elif encrypt_input[i] == "k":  # does the letter "k"
      morse_version.append("-.-")

    elif encrypt_input[i] == "l":  # does the letter "l"
      morse_version.append(".-..")

    elif encrypt_input[i] == "m":  # does the letter "m"
      morse_version.append("--")

    elif encrypt_input[i] == "n":  # does the letter "n"
      morse_version.append("-.")

    elif encrypt_input[i] == "o":  # does the letter "o"
      morse_version.append("---")

    elif encrypt_input[i] == "p":  # does the letter "p"
      morse_version.append(".--.")

    elif encrypt_input[i] == "q":  # does the letter "q"
      morse_version.append("--.-")

    elif encrypt_input[i] == "r":  # does the letter "r"
      morse_version.append(".-.")

    elif encrypt_input[i] == "s":  # does the letter "s"
      morse_version.append("...")

    elif encrypt_input[i] == "t":  # does the letter "t"
      morse_version.append("-")

    elif encrypt_input[i] == "u":  # does the letter "u"
      morse_version.append("..-")

    elif encrypt_input[i] == "v":  # does the letter "v"
      morse_version.append("...-")

    elif encrypt_input[i] == "w":  # does the letter "w"
      morse_version.append(".--")

    elif encrypt_input[i] == "x":  # does the letter "x"
      morse_version.append("-..-")

    elif encrypt_input[i] == "y":  # does the letter "y"
      morse_version.append("-.--")

    elif encrypt_input[i] == "z":  # does the letter "z"
      morse_version.append("--..")
    
    elif encrypt_input[i] == " ":  # does the space bar
      morse_version.append("/")

    elif encrypt_input[i] == "1":  # does the number "1"
      morse_version.append(".----")

    elif encrypt_input[i] == "2":  # does the number "2"
      morse_version.append("..---")
    
    elif encrypt_input[i] == "3":  # does the number "3"
      morse_version.append("...--")
    
    elif encrypt_input[i] == "4":  # does the number "4"
      morse_version.append("....-")
    
    elif encrypt_input[i] == "5":  # does the number "5"
      morse_version.append(".....")

    elif encrypt_input[i] == "6":  # does the number "6"
      morse_version.append("-....")

    elif encrypt_input[i] == "7":  # does the number "7"
      morse_version.append("--...")
    
    elif encrypt_input[i] == "8":  # does the number "8"
      morse_version.append("---..")
    
    elif encrypt_input[i] == "9":  # does the number "9"
      morse_version.append("----.")
    
    elif encrypt_input[i] == "0":  # does the number "0"
      morse_version.append("-----")

  print(*morse_version)


#                                            MORSE TO NUMBER

  number_version = []
  for i in range(len(' '.join(morse_version))):


    if (' '.join(morse_version)[i]) == ".":  # does the dots (even)
      even_randomizer = [2,4,6,8] #establishes set of numbers that can be pulled if the character is a dot
      number_version.append(random.choice(even_randomizer)) #adds a possible draw from the set of numbers into the final output

    elif (' '.join(morse_version)[i]) == "-":  # does the dashes (odd)
      odd_randomizer = [1,3,5,7] #establishes set of numbers that can be pulled if the character is a dash
      number_version.append(random.choice(odd_randomizer)) #adds a possible draw from the set of numbers into the final output

    elif (' '.join(morse_version)[i]) == "/":  # does the spaces (zero)
      number_version.append(0)

    elif (' '.join(morse_version)[i]) == " ":  # does the breaks between letters (nine)
      number_version.append(9)


  print(*number_version, sep="") # yayyy final product



#-----------------------------------------------DECRYPTION------------------------------------------------------ 
elif select == ("d"):
  decrypt_input = input("enter encypted message: ") #takes user imput to be decrypted

#                                            NUMBER TO MORSE

  morse_version = []
  for i in range(len(''.join(decrypt_input))):
 
      
    if (''.join(decrypt_input)[i]) == "2": #checks for 2
      morse_version.append(".") #adds a dot to output

    elif (''.join(decrypt_input)[i]) == "4": #checks for 4
      morse_version.append(".") #adds a dot to output

    elif (''.join(decrypt_input)[i]) == "6": #checks for 6
      morse_version.append(".") #adds a dot to output

    elif (''.join(decrypt_input)[i]) == "8": #checks for 8
      morse_version.append(".") #adds a dot to output

    elif (''.join(decrypt_input)[i]) == "1": #checks for 1
      morse_version.append("-") #adds a dash to output

    elif (''.join(decrypt_input)[i]) == "3": #checks for 7
      morse_version.append("-") #adds a dash to output

    elif (''.join(decrypt_input)[i]) == "5": #checks for 5
      morse_version.append("-") #adds a dash to output 

    elif (''.join(decrypt_input)[i]) == "7": #checks for 7
      morse_version.append("-") #adds a dash to output  

    elif (''.join(decrypt_input)[i]) == "0": #checks for zeros
      morse_version.append("/") #adds a / to output

    elif (''.join(decrypt_input)[i]) == "9": #checks for breaks between letters
      morse_version.append(" ") #adds a space


  morse_version.append("/")
  print(*morse_version, sep="") #tests to make sure numbers are translated into morse properly. also is quality of life since it acts as translater


  #                                          MORSE TO LETTER

  letter_version = []
  current_letter = []
  for i in range(len(''.join(morse_version))):
    

    if ((''.join(morse_version)[i]) == " " or "") or (i+1 == len(''.join(morse_version))):

      if (''.join(current_letter)) == ".-": #does the letter .-
         letter_version.append("a")

      elif (''.join(current_letter)) == "-...": #does the letter -...
         letter_version.append("b")

      elif (''.join(current_letter)) == "-.-.": #does the letter -.-.
         letter_version.append("c")

      elif (''.join(current_letter)) == "-..": #does the letter -..
         letter_version.append("d")

      elif (''.join(current_letter)) == ".": #does the letter .
         letter_version.append("e")

      elif (''.join(current_letter)) == "..-.": #does the letter ..-.
         letter_version.append("f")

      elif (''.join(current_letter)) == "--.": #does the letter --.
         letter_version.append("g")

      elif (''.join(current_letter)) == "....": #does the letter ....
         letter_version.append("h")

      elif (''.join(current_letter)) == "..": #does the letter ..
         letter_version.append("i")

      elif (''.join(current_letter)) == ".---": #does the letter .---
         letter_version.append("j")

      elif (''.join(current_letter)) == "-.-": #does the letter -.-
         letter_version.append("k")

      elif (''.join(current_letter)) == ".-..": #does the letter .-..
         letter_version.append("l")

      elif (''.join(current_letter)) == "--": #does the letter --..
         letter_version.append("m")

      elif (''.join(current_letter)) == "-.": #does the letter -.
         letter_version.append("n")

      elif (''.join(current_letter)) == "---": #does the letter ---
         letter_version.append("o")

      elif (''.join(current_letter)) == ".--.": #does the letter .--.
         letter_version.append("p")

      elif (''.join(current_letter)) == "--.-": #does the letter --.-
         letter_version.append("q")

      elif (''.join(current_letter)) == ".-.": #does the letter .-.
         letter_version.append("r")

      elif (''.join(current_letter)) == "...": #does the letter ...
         letter_version.append("s")

      elif (''.join(current_letter)) == "-": #does the letter -
         letter_version.append("t")

      elif (''.join(current_letter)) == "..-": #does the letter ..-
         letter_version.append("u")

      elif (''.join(current_letter)) == "...-": #does the letter ...-
         letter_version.append("v")

      elif (''.join(current_letter)) == ".--": #does the letter .--
         letter_version.append("w")

      elif (''.join(current_letter)) == "-..-": #does the letter -..-
         letter_version.append("x")

      elif (''.join(current_letter)) == "-.--": #does the letter -.--
         letter_version.append("y")

      elif (''.join(current_letter)) == "--..": #does the letter --..
         letter_version.append("z")

      elif (''.join(current_letter)) == "/": #does the space bar
         letter_version.append(" ")
      
      current_letter = []


    else:
      if morse_version[i] == ".":
        current_letter.append(".")

      elif morse_version[i] == "-":
        current_letter.append("-")

      elif morse_version[i] == "/":
        current_letter.append("/")



  print(''.join(letter_version),  sep="") # yayyy final product
