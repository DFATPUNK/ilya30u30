import os
import re
import torch
import soundfile as sf
import numpy as np
from pathlib import Path
from typing import List
from transformers import AutoTokenizer
from parler_tts import ParlerTTSForConditionalGeneration

device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = "parler-tts/parler-tts-mini-v1"

print("🔄 Chargement du modèle...")
model = ParlerTTSForConditionalGeneration.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Configuration vocale
voice_description = (
    "Lea's voice is calm, slightly expressive and natural, "
    "with moderate speed and pitch. Very clear audio, no background noise."
)

def clean_markdown(text: str) -> str:
    text = re.sub(r"`{1,3}.*?`{1,3}", "", text, flags=re.DOTALL)  # code blocks
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)  # images
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)  # links
    text = re.sub(r"[*_~#>\-]+", "", text)  # md chars
    text = re.sub(r"[^\w\s.,;:!?\'\"À-ÿ]", "", text)  # emojis, special symbols
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def split_into_paragraphs(text: str) -> List[str]:
    paragraphs = text.split("\n\n")
    return [clean_markdown(p) for p in paragraphs if len(p.strip()) > 50]

def synthesize(text: str, idx: int, temp_dir: Path) -> Path:
    input_ids = tokenizer(voice_description, return_tensors="pt").input_ids.to(device)
    prompt_ids = tokenizer(text, return_tensors="pt").input_ids.to(device)
    wav = model.generate(input_ids=input_ids, prompt_input_ids=prompt_ids).cpu().numpy().squeeze()
    path = temp_dir / f"chunk_{idx:03}.wav"
    sf.write(path, wav, model.config.sampling_rate)
    return path

def concatenate(files: List[Path], output: Path):
    all_audio = [sf.read(f)[0] for f in files]
    audio = np.concatenate(all_audio)
    sf.write(output, audio, model.config.sampling_rate)

def generate_audiobook(md_path: str):
    path = Path(md_path)
    out_wav = path.with_suffix(".wav")
    temp_dir = Path("tmp_audio")
    temp_dir.mkdir(exist_ok=True)

    print(f"📥 Lecture de {md_path}...")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    paragraphs = split_into_paragraphs(text)
    print(f"📄 {len(paragraphs)} paragraphes détectés.")

    audio_paths = []
    for i, para in enumerate(paragraphs):
        print(f"🗣️ Paragraphe {i + 1}/{len(paragraphs)}...")
        audio_paths.append(synthesize(para, i, temp_dir))

    print("🔗 Fusion de l'audio final...")
    concatenate(audio_paths, out_wav)

    print("🧹 Nettoyage...")
    for f in audio_paths:
        f.unlink()
    temp_dir.rmdir()

    print(f"✅ Audiobook créé : {out_wav}")

# Exécution via la ligne de commande
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("❌ Utilisation : python generate_audiobook.py <fichier_markdown>")
    else:
        generate_audiobook(sys.argv[1])
