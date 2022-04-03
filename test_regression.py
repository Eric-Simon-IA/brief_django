"""
Test de non régression de la détection de visages.
"""
import os
import cv2
import face_recognition
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid


def detection_original(image_path):
    print("Détection de visages originale :", image_path)

    # load the image with faces
    image = cv2.imread(image_path)

    # load the pre-trained model - Haar cascade
    classifier = cv2.CascadeClassifier("original_detection/haarcascade_frontalface_default.xml")

    # Process the image to perform face detection
    bboxes = classifier.detectMultiScale(image)

    # Display bounding box for each detected face
    for box in bboxes:
        # extract
        x, y, width, height = box
        x2, y2 = x + width, y + height
        # Draw a rectangle over the image to display the face area
        cv2.rectangle(image, (x, y), (x2, y2), (0, 0, 255), 3)
        RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return RGB_img


def detection_modifiee(image_path):
    print("Détection de visages modifiée :", image_path)
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=1, model='cnn')

    pil_image = Image.fromarray(image)
    # Create a Pillow ImageDraw Draw instance to draw with
    draw = ImageDraw.Draw(pil_image)

    for (top, right, bottom, left) in face_locations:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255), width=3)

    # Remove the drawing library from memory as per the Pillow docs
    del draw

    return pil_image


if __name__ == '__main__':
    image_folder = 'media/test_images/'

    for img_path in os.listdir(image_folder):
        lst_out = []
        lst_out.append(detection_original(image_folder + img_path))
        lst_out.append(detection_modifiee(image_folder + img_path))

        fig = plt.figure(figsize=(20, 20))
        grid = ImageGrid(fig, 111,  # similar to subplot(111)
                         nrows_ncols=(1, 2),  # creates 2x2 grid of axes
                         axes_pad=0.1,  # pad between axes in inch.
                         )

        for ax, im in zip(grid, lst_out):
            # Iterating over the grid returns the Axes.
            ax.imshow(im)

        plt.tight_layout()
        plt.show()
