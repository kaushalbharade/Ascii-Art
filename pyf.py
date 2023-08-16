# import pyfiglet as pyf
# import sys
# ARGUMENTS = sys.argv
# with open ("all-fonts.txt","w"):
#     for i in pyf.FigletFont.getFonts():
#         print(i)
        
'''
Task that we have to do =>
make a program which will take a string via command line arguments and prints the ascii format of it. It should take the fonts too from command line arguments (CLA). The syntax should be

python ascii-art.py [--text or -t] "text_to_be_converted" [--font or -f] "font_to_be_used"

YOu can google to get the fonts of pyfiglet library. pyfiglet will make the conversion easy with lot of fonts. Search for pyfiglet
'''
import pyfiglet as pyf
import sys

#To takethe system argumets
ARGUMENTS = sys.argv

#Checking the length of CLA if it is less than three the print the help
if len(ARGUMENTS) < 3:
  print("HELP")
else:
  #IF ARGUMENTS[1] i.e. second CLA is "-t" flag or "--text" flag
  if ARGUMENTS[1] in ["-t", "--text"]:
    TEXT = ARGUMENTS[2]
  #We have checked below condition to check whether "-f" or "--font" flag is specified, as it is optional so we have to continue the program whether or not flag is specified
  if len(ARGUMENTS) > 4:
    #Whether ARGUMENTS[3] is "-f" flag or "--font" flag
    if ARGUMENTS[3] in ["-f", "--font"]:
      FONT = ARGUMENTS[4]
      banner = pyf.figlet_format(text=TEXT, font=FONT)
  #IF -f or --font is not specified then use default font
  else:
    banner = pyf.figlet_format(text=TEXT)

#Print the banner
print(banner)
