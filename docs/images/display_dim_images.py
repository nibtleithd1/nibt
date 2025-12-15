from PIL import Image
import os

# Définir le répertoire contenant les images
repertoire_images = "C:\\TEXTES\\info\\PYTHON\\NLTK\\QUEST_SPACY_NLTK_INSTAGRAM\\QUEST_FLIPCARDS_TLBX_NIBT\\images"


# Créez une liste pour stocker les dimensions des images
dimensions_images = []

# Parcourez les fichiers du répertoire
for fichier in os.listdir(repertoire_images):
    if fichier.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):  # Excluez les fichiers .svg
        chemin_complet = os.path.join(repertoire_images, fichier)
        image = Image.open(chemin_complet)
        largeur, hauteur = image.size
        dimensions_images.append((largeur, hauteur, fichier))
        image.close()

max_width = 17 * 28.346
max_height = 6.5 * 28.346
# Triez la liste des dimensions par largeur et hauteur
dimensions_images.sort(key=lambda x: (x[0], x[1]))
scale_width = max_width / (largeur / 72)  # 72 points par pouce
scale_height = max_height / hauteur
# Utilisez le facteur d'échelle le plus restrictif
image_scale = min(scale_width, scale_height)
# Affichez les dimensions par ordre croissant de largeur
print("Images triées par largeur croissante:")
for largeur, hauteur, fichier in dimensions_images:
    print(f"{fichier} - Largeur: {largeur}, Hauteur: {hauteur}, scale_width: {scale_width} ")

# Triez la liste des dimensions par hauteur et largeur
dimensions_images.sort(key=lambda x: (x[1], x[0]))

# Affichez les dimensions par ordre croissant de hauteur
print("\nImages triées par hauteur croissante:")
for largeur, hauteur, fichier in dimensions_images:
    print(f"{fichier} - Largeur: {largeur}, Hauteur: {hauteur}, scale_width: {scale_width} ")
