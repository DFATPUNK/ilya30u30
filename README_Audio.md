# Audio Book Generator for Studies

This repository can automatically generate audiobooks (MP3) from all `study.md` files using Coqui TTS.

## Quick Start

1. Clone the repository:

```
git clone https://github.com/DFATPUNK/ilya30u30.git
cd ilya30u30
```

2. Run the setup script:

```
bash setup.sh
```
This script will install Python 3.10.13 (if needed), create a virtual environment, and install the required TTS library.

3. Generate the audiobooks:

```
source venv/bin/activate
python generate_audiobooks.py
```

All the MP3 files will be created inside the audiobooks/ folder, organized by study.

---

🎧 Enjoy listening to research study analyses anywhere!