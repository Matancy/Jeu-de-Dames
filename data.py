#
# Fichier regroupant des variables utiles au fonctionnement du jeu
#


partie = 1 # Défini la partie comme en cours
joueur = False # Défini quel joueur est en train de jouer (1 croix / 0 Rond)
esp = "\t" # Variable de tabulation

# Variable regroupant les informations du damier
damier = [
          ['','O','','O','','O','','O','','O'],
          ['O','','O','','O','','O','','O',''],
          ['','O','','O','','O','','O','','O'],
          ['O','','O','','O','','O','','O',''],
          ['','-','','-','','-','','-','','-'],
          ['-','','-','','-','','-','','-',''],
          ['','X','','X','','X','','X','','X'],
          ['X','','X','','X','','X','','X',''],
          ['','X','','X','','X','','X','','X'],
          ['X','','X','','X','','X','','X','']
        ]
        
# Fonction pour afficher des couleurs
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'