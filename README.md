Le défi: DIY et Objets connectés !
Introduction au Projet de Photobooth DIY avec Objets de Récupération
À l'ère de la créativité durable, la transformation d'objets de récupération en projets innovants prend tout son sens. Notre projet de photobooth DIY représente une fusion passionnante entre recyclage et divertissement, offrant une expérience photographique unique. En utilisant des composants récupérés tels que des écrans anciens, des caméras délaissées, et divers objets du quotidien, nous créerons un photobooth interactif qui ajoutera une touche d'originalité à n'importe quel événement.
Au cours de cette aventure, nous allons explorer la réutilisation créative de matériaux, intégrer des éléments technologiques tels que des caméras Raspberry Pi, et concevoir une interface conviviale pour guider les utilisateurs tout au long du processus de prise de photo. Le projet couvrira également des aspects pratiques, du développement d'un script de contrôle à la personnalisation du boîtier, pour vous permettre de créer un photobooth unique et fonctionnel.
Rejoignez-nous dans cette exploration où l'innovation écologique et le plaisir visuel se rencontrent pour donner une seconde vie à des objets autrement oubliés. Transformez votre vision créative en une expérience interactive et mémorable avec notre photobooth DIY à partir d'objets de récupération.
Contribution à l'Association Action Climat :
Sensibilisation Environnementale :
Le photobooth se positionne comme un outil puissant de sensibilisation aux enjeux environnementaux. Lors des événements où il est déployé, les participants interagissent avec une technologie créative construite à partir d'objets recyclés, soulignant ainsi l'importance de la réutilisation. Cette expérience visuelle et pratique incite à la réflexion sur les choix quotidiens impactant l'environnement et renforce la compréhension des défis climatiques.
Contenu Visuel Impactant pour la Sensibilisation :
Les photos capturées par le photobooth deviennent des outils visuels puissants pour les campagnes de sensibilisation en ligne. Les images reflètent l'engagement des participants envers la cause climatique, générant un contenu visuel impactant à partager sur les médias sociaux. Cela étend la portée de la sensibilisation au-delà des événements physiques, amplifiant ainsi le message.
Production Écologique du Photobooth :
La réalisation du photobooth repose sur des principes écologiques, en utilisant des matériaux récupérés pour la construction du boîtier. Cette approche respectueuse de l'environnement aligne la production du photobooth avec les valeurs de durabilité, créant ainsi une harmonie entre le message que véhicule le projet et la manière dont il est réalisé.
Le code du projet :
Ce script Python utilise plusieurs bibliothèques pour réaliser une application qui capture des images à partir d'une caméra, les affiche, les imprime et superpose une image de cadre sur la photo avant de l'imprimer. Je vais vous expliquer chaque partie du code.
Bibliothèques utilisées :
subprocess: Utilisé pour exécuter des commandes externes.
time: Utilisé pour introduire des délais dans le programme.
cv2: OpenCV, une bibliothèque pour la vision par ordinateur.
pygame: Utilisé pour afficher des images.
cups: Utilisé pour l'impression.
PIL (Pillow): Utilisé pour manipuler des images.
gpiozero: Utilisé pour interagir avec les broches GPIO du Raspberry Pi.
Fonctions principales :
superimpose_images: Prend deux chemins d'images en entrée, superpose l'une sur l'autre avec une transparence spécifiée, puis enregistre l'image résultante.
print_image: Imprime une image spécifiée sur une imprimante sélectionnée avec des options de configuration.
capture_and_display: Capture une photo à partir de la caméra, l'affiche à l'aide de Pygame, puis superpose une image de cadre sur la photo avant de l'imprimer.
start_libcamera_preview: Démarre ou arrête l'affichage de la caméra en continu en fonction de l'état actuel.
toggle_camera_display: Bascule l'état de l'affichage de la caméra lorsque le bouton est pressé.
toggle_image_print: Bascule l'état de l'impression de l'image lorsque le bouton est pressé.
handle_error: Gère les erreurs en affichant un message d'erreur.
main: Fonction principale du programme. Elle initialise l'affichage de la caméra et reste dans une boucle infinie pour basculer l'affichage de la caméra en fonction du bouton pressé.
Logique générale :
Lorsque le programme démarre, il initialise l'affichage de la caméra.
Ensuite, il entre dans une boucle infinie où il attend que le bouton soit pressé pour basculer l'affichage de la caméra.
Lorsque le bouton est pressé, la caméra prend une photo, l'affiche à l'aide de Pygame, superpose une image de cadre, imprime la photo et revient à la boucle principale.
Le programme peut être arrêté en appuyant sur Ctrl+C, ce qui termine proprement le processus de la caméra.
