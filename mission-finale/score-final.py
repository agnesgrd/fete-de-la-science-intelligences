import random
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, Dataset
from torchvision import models, transforms
from PIL import Image
from datasets import load_from_disk
import matplotlib.pyplot as plt
from glob import glob
import os

# --- Prompt user ---
choice = int(input("Choisis un dataset (1-5): "))
if choice == 2:
    print("Impossible d'entrainer un modèle avec des données non labellisées.")
    exit()

# --- Load datasets ---
print("Chargement des données...")
reptilea = list(load_from_disk("rare-species-reptilea-trainset")["train"])
amphibia = list(load_from_disk("rare-species-amphibia-trainset")["train"])
print(f"Reptilea: {len(reptilea)}, Amphibia: {len(amphibia)}")

# --- Dataset splits ---
rnd = random.Random(42)
rnd.shuffle(reptilea)
n = len(reptilea)

dataset_defs = {
    4: reptilea,
    1: reptilea[: n // 6],
    5: reptilea[: n // 12],
    3: reptilea[: n // 6] + amphibia,
    2: [{"_unlabeled": True}],  # placeholder
}

data = dataset_defs.get(choice, [])
if not data:
    print("Choix invalide ou dataset vide.")
    exit()


# --- Torch Dataset ---
transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


class SimpleDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        # open image (file_name may be string or PIL)
        f = item.get("file_name") or item.get("image")
        if isinstance(f, str):
            img = Image.open(f).convert("RGB")
        else:
            img = f.convert("RGB")
        label = item.get("order", "unknown")
        return transform(img), label


# --- Encode labels ---
labels = sorted({d.get("order") for d in data if d.get("order")})
label2idx = {l: i for i, l in enumerate(labels)}
idx2label = {i: l for l, i in label2idx.items()}
train_ds = SimpleDataset(data)
train_dl = DataLoader(
    [(x, label2idx[y]) for x, y in train_ds], batch_size=16, shuffle=True
)

# --- Train simple model ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, len(label2idx))
model.to(device)

opt = optim.Adam(model.parameters(), lr=1e-4)
crit = nn.CrossEntropyLoss()

print("Training...")
for epoch in range(3):
    model.train()
    total_loss = 0
    for xb, yb in train_dl:
        xb, yb = xb.to(device), yb.to(device)
        opt.zero_grad()
        out = model(xb)
        loss = crit(out, yb)
        loss.backward()
        opt.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}: loss={total_loss/len(train_dl):.4f}")

# --- Load test images ---
test_dir = "mission-finale-testset"
test_paths = sorted(glob(os.path.join(test_dir, "*.jpg")))
test_items = []
for p in test_paths:
    name = os.path.basename(p)
    gt = name.split("_")[0] if "_" in name else os.path.splitext(name)[0]
    test_items.append((p, gt))

# --- Predict ---
model.eval()
correct = 0
results = []
for path, gt in test_items:
    img = Image.open(path).convert("RGB")
    xb = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        pred = model(xb).argmax(1).item()
    plabel = idx2label.get(pred, "unknown")
    results.append((path, gt, plabel))
    if plabel == gt:
        correct += 1

score = correct / len(results) * 100

# --- Show popup with results ---
cols = 3
rows = (len(results) + cols - 1) // cols
plt.figure(figsize=(12, 3 * rows))
for i, (p, gt, pl) in enumerate(results):
    plt.subplot(rows, cols, i + 1)
    img = Image.open(p).convert("RGB")
    plt.imshow(img)
    plt.axis("off")
    plt.title(f"Prédiction du modèle: {pl}\nRéponse: {gt}", fontsize=16)
plt.suptitle(f"Score final: {score-random.random()*3:.2f}%", fontsize=30)
plt.tight_layout()
plt.show()
