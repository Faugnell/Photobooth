import subprocess
import time
import cv2
import pygame
import cups
from PIL import Image
from pygame.locals import *
from gpiozero import Button
from datetime import datetime
import os

# Configuration du bouton (connecté entre la broche GPIO 17 et la masse)
button = Button(17)

# Configuration du bouton (connecté entre la broche GPIO 25 et la masse)
button2 = Button(25)

camera_process = None  # Pour stocker le processus de la caméra

def superimpose_images(background_path, overlay_path, output_path, position=(0, 0), transparency=0):
     # Ouvrir les images
    background = Image.open(background_path)
    overlay = Image.open(overlay_path)

    # Assurez-vous que les images sont en mode RGBA (avec canal alpha pour la transparence)
    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    # Redimensionner l'image d'incrustation si nécessaire
    overlay = overlay.resize(background.size)

    # Superposer les images
    combined = Image.alpha_composite(background, overlay)

    # Enregistrer l'image résultante
    combined.save(output_path, "PNG")


def print_image(image_path):
    # Open the image with Pillow (PIL)
    image = Image.open(image_path)

    # Create a connection to CUPS
    conn = cups.Connection()

    # Get the list of available printers
    printers = conn.getPrinters()

    # Select a printer (change the key according to your needs)
    printer_name = list(printers.keys())[0]

    # Configure printing options for paper size 10x15 cm
    options = {
        'PageSize': '10x15cm',  # Paper size
        'scaling': '100',       # Image scaling
        'page-top': '0',        # Marge supérieure
        'page-bottom': '0',     # Marge inférieure
        'page-left': '0',       # Marge gauche
        'page-right': '0',      # Marge droite
    }

    # Print the image
    job_id = conn.printFile(printer_name, image_path, "Print Job", options=options)
    
    
def naming_file():
    # Obtenir la date et l'heure actuelles
    now = datetime.now()

    # Formater la date et l'heure en une chaîne de caractères
    formatted_string = now.strftime("%Y%m%d%H%M%S")
    return (formatted_string)
    
def capture_and_display():
   
    try:
        photo_name = naming_file() 
        road_photo_original = "photobooth/original/" + photo_name + ".jpg"
        road_photo_retouched = "photobooth/retouched/" + photo_name + ".png"
        subprocess.run(["libcamera-still", "-o", road_photo_original, "--quality", "95"], check=True)
    except subprocess.CalledProcessError as e:
        handle_error(f"Error toggling camera display: {e}")
        return

    # Charger l'image et la redimensionner
    original_image = pygame.image.load(road_photo_original)
    resized_image = pygame.transform.scale(original_image, (1920, 1080))  # Ajustez les dimensions selon vos besoins

    # Affichage de l'image redimensionnée
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))  # Taille de la fenêtre
    pygame.display.set_caption(photo_name)
    
    # Ajoutez ces lignes pour remplir l'arrière-plan avec une couleur blanche
    screen.fill((255, 255, 255))  # Blanc
    pygame.display.flip()

    # Afficher l'image
    screen.blit(resized_image, (0, 0))
    pygame.display.flip()

    # Attendre que l'utilisateur ferme la fenêtre
    running = True
    printed = False
    
    while running:
        if button.is_pressed:
            printed = True
            running = False
        if button2.is_pressed:
            printed = False
            running = False
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
    pygame.quit()
    
    if printed :
        background_image_path = road_photo_original
        overlay_image_path = "photobooth/cadre/cadre_ndi_2023.png"
        output_image_path = road_photo_retouched

        # Appeler la fonction pour superposer les images
        superimpose_images(background_image_path, overlay_image_path, output_image_path, position=(0, 0), transparency=0)
        
        #print_image(road_photo_retouched)
        # Ajouter une pause pour éviter les basculements rapides si le bouton est maintenu enfoncé
        time.sleep(0.5)
        
    else:
        chemin_absolu_image = os.path.abspath(road_photo_original)

        # Suppression du fichier
        try:
            os.remove(chemin_absolu_image)
            print(f"L'image {chemin_relatif_image} a été supprimée avec succès.")
        except FileNotFoundError:
            print(f"Le fichier {chemin_relatif_image} n'existe pas.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la suppression de l'image : {e}")
            
    # Once printing is complete, reset camera_process to None
    global camera_process
    camera_process = None
    main()
    

def start_libcamera_preview():
    """Démarre ou arrête l'affichage de la caméra en fonction de l'état actuel."""
    global camera_process

    try:
        if camera_process is None:
            # Démarrer le flux vidéo en continu
            camera_process = subprocess.Popen(["libcamera-vid", "-t", "0"])
            print("Camera display turned on.")
        else:
            # Si le processus de la caméra existe, le terminer
            camera_process.terminate()
            camera_process.wait()
            print("Camera display turned off.")
            capture_and_display()
            
    except subprocess.CalledProcessError as e:
        handle_error(f"Error toggling camera display: {e}")

def toggle_camera_display():
    """Bascule l'état de l'affichage de la caméra lorsque le bouton est pressé."""
    global camera_process
    if button.is_pressed:
        start_libcamera_preview()
        # Ajouter une pause pour éviter les basculements rapides si le bouton est maintenu enfoncé
        time.sleep(0.5)
        

def handle_error(error_message):
    """Gère les erreurs en affichant un message d'erreur."""
    print(f"Error: {error_message}")

def stop_program():
    """Arrête proprement le programme."""
    global camera_process
    if camera_process is not None:
        camera_process.terminate()
        camera_process.wait()
    print("Program terminated.")
    pygame.quit()
    exit()

def main():
    try:
        start_libcamera_preview()

        while True:
            # Bascule l'état de l'affichage de la caméra lorsque le bouton est pressé
            toggle_camera_display()

            # Arrête le programme si le bouton2 est pressé
            #if button2.is_pressed:
                #stop_program()

    except KeyboardInterrupt:
        stop_program()

if __name__ == "__main__":
    main()
