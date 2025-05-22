import os
import re

# Set your actual scene folder path here
scene_root = '/home/nchiluk6/MVSNet/data/eth3d/lowres/training/undistorted/delivery_area'
images_root = os.path.join(scene_root, 'images')
print(images_root)
cams_dir = os.path.join(scene_root, 'cams')
output_file = os.path.join(cams_dir, 'index2prefix.txt')

# Check if images folder exists
if not os.path.exists(images_root):
    print("[!] Error: images folder does not exist at {}".format(images_root))
    exit(1)

# Find all image subfolders like images_rig_cam4_undistorted, etc.
cam_folders = sorted([d for d in os.listdir(images_root)
                      if os.path.isdir(os.path.join(images_root, d)) and
                      re.match(r'images_rig_cam\d+_undistorted', d)])

index = 0
entries = []

# Go through each cam folder
for cam_folder in cam_folders:
    image_dir = os.path.join(images_root, cam_folder)
    image_files = sorted([f for f in os.listdir(image_dir) if f.endswith('.png')])

    for img in image_files:
        relative_path = "{}/{}".format(cam_folder, img)
        entries.append("{} {}".format(index, relative_path))
        index += 1

# Create cams folder if it doesn't exist
if not os.path.exists(cams_dir):
    os.makedirs(cams_dir)

# Write to index2prefix.txt
with open(output_file, 'w') as f:
    f.write("{}\n".format(len(entries)))
    for entry in entries:
        f.write(entry + "\n")

print("[Ok] index2prefix.txt created at {} with {} entries.".format(output_file, len(entries)))
