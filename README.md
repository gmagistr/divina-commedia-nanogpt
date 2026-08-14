# La Divina Commedia — corpus per nanoGPT

Il testo integrale della *Divina Commedia* pronto per addestrare un language
model da zero, seguendo [nanoGPT](https://github.com/karpathy/nanoGPT) di
Andrej Karpathy. È l'equivalente italiano di `tinyshakespeare`, con in più una
struttura metrica che il modello impara in modo visibile: la **terza rima**
(ABA BCB CDC…).

| | Divina Commedia | tinyshakespeare |
|---|---|---|
| caratteri | 532.783 | 1.115.394 |
| versi | 14.366 | — |
| vocabolario char-level | 83 | 65 |

Testo di pubblico dominio, da [Project Gutenberg](https://www.gutenberg.org/ebooks/1012):
rimossi intestazione e licenza, tolta l'indentazione uniforme, conservate le
righe vuote fra le terzine (sono il segnale strutturale che il modello deve
cogliere).

## Uso

```bash
wget https://raw.githubusercontent.com/gmagistr/divina-commedia-nanogpt/main/divina_commedia.txt
```

Con nanoGPT, in stile `data/shakespeare_char`:

```bash
python prepare.py                 # scrive train.bin, val.bin, meta.pkl
python train.py --dataset=dante --n_layer=6 --n_head=6 --n_embd=384 \
  --max_iters=5000 --block_size=256 --compile=False
python sample.py --out_dir=out
```

Su Apple Silicon aggiungi `--device=mps --compile=False`.

## Cosa aspettarsi

Dopo poche migliaia di iterazioni il modello produce endecasillabi
plausibili, con la lunghezza di verso giusta e le terzine separate
correttamente; le rime iniziano a comparire più tardi, perché richiedono di
tenere a mente il verso a distanza di due righe. È esattamente il fenomeno
che rende questo corpus più istruttivo di un testo in prosa.
