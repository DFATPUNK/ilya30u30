#!/bin/bash

echo "🔵 Setting up the Python environment for audiobook generation..."

# Vérifier Homebrew
if ! command -v brew &> /dev/null
then
    echo "⚠️ Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✅ Homebrew is already installed."
fi

# Vérifier pyenv
if ! command -v pyenv &> /dev/null
then
    echo "⚠️ pyenv not found. Installing pyenv via Homebrew..."
    brew install pyenv
else
    echo "✅ pyenv is already installed."
fi

# Initialiser pyenv pour ce shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

# Vérifier Python 3.10.13
if ! pyenv versions | grep -q "3.10.13"; then
    echo "🔵 Installing Python 3.10.13 via pyenv..."
    pyenv install 3.10.13
fi

# Définir Python local
echo "🔵 Setting local Python version to 3.10.13"
pyenv local 3.10.13

# Créer un venv si inexistant
if [ ! -d "venv" ]; then
  echo "🔵 Creating a virtual environment..."
  python -m venv venv
fi

# Activer le venv
source venv/bin/activate

# Upgrade pip + installer TTS
echo "🔵 Upgrading pip and installing TTS..."
python -m pip install --upgrade pip
python -m pip install TTS

echo "✅ Setup complete. Ready to generate audiobooks!"