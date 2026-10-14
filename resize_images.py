# from PIL import Image
# import pillow_heif
# import os

# pillow_heif.register_heif_opener()

# input_folder = "/Users/reshmasri/Downloads/Dragon"
# output_folder = "/Users/reshmasri/Downloads/Dragon_resized_224/"
# os.makedirs(output_folder, exist_ok=True)

# count = 0
# for filename in sorted(os.listdir(input_folder)):
#     if not filename.lower().endswith(('.heic', '.jpg', '.jpeg', '.png', '.webp')):
#         continue
#     if count >= 100:
#         break
#     img = Image.open(os.path.join(input_folder, filename))
#     img = img.convert('RGB')
#     img = img.resize((224, 224))
#     img.save(os.path.join(output_folder, f"dragon_{count+1:03d}.jpg"))
#     count += 1

# print(f"Resized {count} images to 224x224")

# from PIL import Image, ImageFilter
# import pillow_heif
# import os

# pillow_heif.register_heif_opener()

# input_folder = "/Users/reshmasri/Downloads/Dragon"
# output_folder = "/Users/reshmasri/Downloads/Dragon_resized_224/"
# os.makedirs(output_folder, exist_ok=True)

# count = 0
# for filename in sorted(os.listdir(input_folder)):
#     if not filename.lower().endswith(('.heic', '.jpg', '.jpeg', '.png', '.webp')):
#         continue
#     if count >= 100:
#         break
#     img = Image.open(os.path.join(input_folder, filename))
#     img = img.convert('RGB')
#     img = img.resize((224, 224), Image.LANCZOS)       # best quality downscale
#     img = img.filter(ImageFilter.SHARPEN)               # restore sharpness
#     img.save(os.path.join(output_folder, f"dragon_{count+1:03d}.jpg"), quality=95)  # minimal compression
#     count += 1

# print(f"Resized {count} images to 224x224")

import os

folder = "/Users/reshmasri/Documents/DeepLearningAI/project/Dragon_resized_224/"

for filename in os.listdir(folder):
    if not filename.lower().endswith('.jpg'):
        continue
    # dragon_091.jpg → dragon_091_OBJ111.jpg
    new_name = filename.replace(".jpg", "_OBJ111.jpg")
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

print("Done")