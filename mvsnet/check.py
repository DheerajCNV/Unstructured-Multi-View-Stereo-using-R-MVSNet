import cv2, os

folder = "/home/nchiluk6/MVSNet/data/eth3d/test/lakeside/images"
sizes = set()
for f in sorted(os.listdir(folder)):
    if f.endswith(".jpg"):
        img = cv2.imread(os.path.join(folder, f))
        h, w = img.shape[:2]
        print(f"{f}: {w}x{h}")
        sizes.add((w, h))

print("Unique sizes found:", sizes)
