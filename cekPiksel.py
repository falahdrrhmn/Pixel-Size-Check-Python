import cv2

def get_image_size(image_path):
    image = cv2.imread(image_path)
    if image is None: 
        raise ValueError(f"Gak ada image di {image_path}")
    return image.shape[1], image.shape[0]

image_path = "contoh_citra.jpg"
width, height = get_image_size(image_path)
print(f"Lebar citra: {width} piksel")
print(f"Tinggi citra: {height} piksel")
