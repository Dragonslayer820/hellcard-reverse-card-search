import mageCards
import warriorCards
import rogueCards
import testCards
from card import Card

cardName = ''
card = Card.cardDictionary
print('Last updated (8/6/23)')
print('''
###################################################
#   _____  ______          _____  __  __ ______   #
#  |  __ \|  ____|   /\   |  __ \|  \/  |  ____|  #
#  | |__) | |__     /  \  | |  | | \  / | |__     #
#  |  _  /|  __|   / /\ \ | |  | | |\/| |  __|    #
#  | | \ \| |____ / ____ \| |__| | |  | | |____   #
#  |_|  \_\______/_/    \_\_____/|_|  |_|______|  #
#                                                 #
###################################################
''')
print('Due to limitations (or lack of skill on my end) (Plus I didn\'t really care enough to make it better)')
print('Card names are slightly modified from original, and require capitals. Rules are below')
print()
print('1: Capitals are NOT OPTIONAL. If it is capital in the card name, it must be capital when you type it')
print('2: Replace \'&\' with \'and\' (No apostrophes)')
print('3: Do not include apostophes (This thing) ======> [ \' ]')
print('4: Any special characters are replaced with their closest counterpart [¡No Pasarán!] becomes [No Pasaran]')
print('5: Do not include exclamation points [¡No Pasarán!] becomes [No Pasaran]')
print()
print('If Hellcard Devs want to use or adopt some of this code, credit me draco_malus')
print('If I missed any card, do let me know on Discord(draco_malus)')
print()
print('###################################################')
print()
while True:
	print('\nEnter card name to find what it\'s built from')
	print('Type q to exit')
	cardName = input('Card Name: ')
	if cardName == 'q':
		break
	try:
		card[cardName].recPrintBuildPath()
		print()
		print('###################################################')
	except KeyError:
		print()
		print('Card not in system')
		print()
		print('###################################################')
	except:
		print('Something has gone wrong, please try again')
		print('###################################################')


input('Exiting...')
exit()