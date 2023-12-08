import cv2

def get_image_size(image_path):
    image = cv2.imread(image_path)
    if image is None: 
        raise ValueError(f"Gak ada image di {image_path}")
    return image.shape[1], image.shape[0]

image_path_test = "Test\Melanoma\AUG_0_156.jpeg"
width_test, height_test = get_image_size(image_path_test)

image_path_train = "Train\Melanoma\AUG_0_11.jpeg"
width_train, height_train = get_image_size(image_path_train)


print(f"Lebar Citra Test: {width_test} piksel")
print(f"Tinggi Citra Test: {height_test} piksel")

print(f"Lebar Citra Train: {width_train} piksel")
print(f"Tinggi Citra Train: {height_train} piksel")
