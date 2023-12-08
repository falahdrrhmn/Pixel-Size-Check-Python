import os
import cv2

# cek ukuran seluruh gambar
def get_image_size(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Gak ada image di {image_path}")
    return image.shape[1], image.shape[0]

def process_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):  # Filter hanya file gambar
            image_path = os.path.join(folder_path, filename)
            width, height = get_image_size(image_path)
            print(f"Lebar Citra {filename}: {width} piksel")
            print(f"Tinggi Citra {filename}: {height} piksel")
            print()

if __name__ == "__main__":
    test_folder_path = "Test/Melanoma"
    train_folder_path = "Train/Melanoma"

    print("Ukuran Citra di Folder Test:")
    process_images_in_folder(test_folder_path)

    print("\nUkuran Citra di Folder Train:")
    process_images_in_folder(train_folder_path)
