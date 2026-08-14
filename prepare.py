"""Prepara la Divina Commedia per nanoGPT (char-level).

Scrive train.bin, val.bin e meta.pkl nella stessa cartella, come
`data/shakespeare_char/prepare.py` del repo di Karpathy.
"""
import pickle
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
text = (HERE / "divina_commedia.txt").read_text(encoding="utf-8")

chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}
print(f"{len(text):,} caratteri, vocabolario di {len(chars)}")

n = int(0.9 * len(text))
for name, split in (("train", text[:n]), ("val", text[n:])):
    ids = np.array([stoi[c] for c in split], dtype=np.uint16)
    ids.tofile(HERE / f"{name}.bin")
    print(f"{name}: {len(ids):,} token")

with open(HERE / "meta.pkl", "wb") as f:
    pickle.dump({"vocab_size": len(chars), "itos": itos, "stoi": stoi}, f)
print("meta.pkl scritto")
