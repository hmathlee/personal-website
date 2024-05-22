from torchvision.models.detection import maskrcnn_resnet50_fpn_v2, MaskRCNN_ResNet50_FPN_V2_Weights
import torchvision.transforms.functional as F

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("images/me.JPG")
img_tensor = F.to_tensor(img).unsqueeze(0)

weights = MaskRCNN_ResNet50_FPN_V2_Weights.DEFAULT
model = maskrcnn_resnet50_fpn_v2(weights=weights)
model.eval()

prediction = model(img_tensor)[0]
masks = prediction["masks"].squeeze(1)
scores = prediction["scores"]
labels = prediction["labels"]

filter_idx = scores > 0.5

filtered_masks = masks[scores > 0.5]
filtered_labels = labels[scores > 0.5]

n_instances = filtered_masks.shape[0]
color = np.random.randint(0, 255, 3, dtype=np.uint8)

img = np.array(img)
mask = filtered_masks[0].detach().numpy()
label = filtered_labels[0].item()

# Save segmented image
for c in range(3):
    t = mask > 0.5
    img[:, :, c] = np.where(mask > 0.5, img[:, :, c] * 0.5 + color[c] * 0.5, img[:, :, c])

plt.figure(figsize=(10, 7))
plt.imshow(img)
plt.axis("off")
plt.savefig("images/me_segmented.eps", format="eps", bbox_inches="tight", pad_inches=0.0)

# Save version with black background
for c in range(3):
    t = mask > 0.5
    img[:, :, c] = np.where(mask > 0.5, img[:, :, c] * 0.5 + color[c] * 0.5, 0)

plt.figure(figsize=(10, 7))
plt.imshow(img)
plt.axis("off")
plt.savefig("images/me_black_background.eps", format="eps", bbox_inches="tight", pad_inches=0.0)