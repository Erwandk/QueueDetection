#!usr/bin/temp python3
# -*- coding: utf-8 -*-

# Importation des librairies utiles
import os
import matplotlib.pyplot as plt
import cv2


def labellise_photos(path_img, path_label, erase=False):
    """
    Fonction permettant de labelliser les photos d'un répertoire
    - erase : permet d'écraser les labellisations précédentes
    """
    if not os.path.isdir(path_label) or not os.path.isdir(path_img):
        raise NameError("Inputs should be a directory : \npath_img : {} \npath_label : {}".format(path_img,
                                                                                                  path_label))
    for img_file in os.listdir(path_img):
        # Si c'est un dossier, on passe au fichier suivant
        if not os.path.isfile(os.path.join(path_img, img_file)):
            continue
        name, ext = img_file.split(".")
        # Si ce n'est pas une photo, on passe au fichier suivant
        if ext not in ["png", "jpg", "jpeg"]:
            continue
        label_file = str(name) + ".txt"
        # Si la photo est déjà labellisée et qu'on ne veut pas refaire une labellisation
        if label_file in os.listdir(path_label) and not erase:
            continue

        img = cv2.imread(os.path.join(path_img, img_file), cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Sinon on labellise la photo
        while True:
            plt.figure(figsize=(25, 25))
            plt.imshow(img, interpolation='nearest')
            plt.axis('off')
            plt.show()
            label = input("Rentrez le label de la photo :")
            try:
                label = int(label)
                break
            except:
                print("Veuillez rentrer un label entier !")

        with open(os.path.join(path_label, label_file), "w") as file:
            file.write(str(label))

        print("Label saved !")


if __name__ == '__main__':

    path_img = "/home/erwan/Centrale/OSY/DEEPL/Projet/QueueDetection/data/img/test"
    path_label = "/home/erwan/Centrale/OSY/DEEPL/Projet/QueueDetection/data/labels/regression/test"

    labellise_photos(path_img, path_label)
