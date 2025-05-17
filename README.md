# 🧠 Ilya30u30 – Étude approfondie de 30 papers fondamentaux en Intelligence Artificielle

## 📚 Origine du projet

En 2023, **Ilya Sutskever**, cofondateur d'OpenAI, a partagé avec **John Carmack** une liste de lectures composée d’une trentaine de **papers de recherche** en intelligence artificielle, en lui affirmant :

> _“Si tu apprends vraiment tous ceux-là, tu sauras 90% de ce qui est important aujourd’hui.”_

Ce dépôt GitHub a pour objectif de **documenter l’étude systématique et approfondie** de cette liste, dans l’ordre chronologique de parution des publications, en vue d’acquérir une compréhension rigoureuse et opérationnelle des **fondamentaux de l’IA**.

---

## 🧪 Méthodologie d’étude

Chaque paper fait l’objet d’une **étude complète**, structurée selon le plan suivant :

1. **Biographie des auteurs**
2. **Abstract commenté**
3. **Lexique** :
   - Chaque terme technique ou mathématique cité dans l’article est **expliqué simplement**
   - Avec des **exemples concrets** pour rendre la lecture accessible même sans bagage universitaire
4. **Étude du research paper par section**, avec :
   - Sujet de la section
   - Court lexique si de nouveaux termes techniques sont employés
   - Explication détaillée des notions et éventuelles figures & équations avec des analogies pédagogiques
   - Résumé des concepts fondamentaux appris dans la section
5. **Conclusion**
6. **Cas pratique appliqué**, avec :
   - Rejoue **chaque transformation conceptuelle du paper**
   - Visualisation de l’**évolution du modèle** section après section

---

## 🗂 Arborescence du dépôt

```
.
├── papers/                   # 📥 Tous les papers à étudier, rangés par ordre chronologique de parution
│   ├── 19930801 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights.pdf
│   └── ...
│
├── studies/                  # 📂 Études réalisées (1 dossier par paper)
│   ├── 19930801 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights/
│   │   ├── paper.pdf         # 📄 Paper original
│   │   └── study.md          # 📝 Étude complète du paper
│   └── ...
│
├── audiobooks/               # 🎧 Audiobooks générés automatiquement à partir des études (créé par le script)
│   ├── 19930801 - Keeping Neural Networks Simple by Minimizing the Description Length of the Weights/
│   │   └── study.mp3         # 🔊 Audio correspondant à l'étude
│   └── ...
│
├── venv/                     # 🐍 Environnement virtuel Python local (non suivi par Git)
│
├── .gitignore                # 📜 Ignore venv/ et audiobooks/ pour garder le repo léger
├── .python-version           # 📜 Force Python 3.10.13 avec pyenv
├── setup.sh                  # ⚙️ Script d'installation automatique pour tout mettre en place
├── generate_audiobooks.py    # 🧠 Script principal pour générer tous les fichiers audio
├── README.md                 # 📚 Ce fichier
└── README_Audio.md           # 🎧 Guide spécifique pour générer et écouter les audiobooks
```

---

## 🎧 Générer et écouter les études en Audiobooks

Vous pouvez désormais générer et écouter la version audio de chaque étude réalisée !

👉 [Voir les instructions détaillées pour la génération d'audiobooks](./README_Audio.md)

### ⚡ Démarrage rapide pour générer tous les audiobooks

1. **Cloner ce repository** :

```
git clone https://github.com/DFATPUNK/ilya30u30.git
cd ilya30u30
```

2. **Lancer le script d'installation** :

```
bash setup.sh
```

3. **Activer l'environnement virtuel** :

```
source venv/bin/activate
```

4. **Générer les audiobooks** :

```
python generate_audiobooks.py
```

✅ Ce script automatique :
- Installe la bonne version de Python (3.10.13) si nécessaire
- Crée et active un environnement virtuel isolé
- Installe toutes les dépendances nécessaires
- Génère un fichier `.mp3` pour chaque étude dans le dossier `audiobooks/`

🎧 Vous pourrez alors écouter les analyses d'articles de recherche où et quand vous voulez !

---

## 🧑‍💻 Contact

Ce projet est mené par **Jérémy Brunet**  
📧 jeremy@jeremybrunet.com  
🌐 [jeremybrunet.com](https://jeremybrunet.com)

---

## ✨ Objectif du projet

Ce projet est né d’une volonté personnelle de maîtriser en profondeur les **principes fondamentaux de l’intelligence artificielle**, à travers l’étude rigoureuse de la liste de lectures créée par Ilya Sutskever.

Il constitue une **démonstration de méthode, de persévérance et de clarté pédagogique** : chaque étude vise non seulement à comprendre les publications les plus influentes du domaine, mais aussi à **les rendre accessibles à d’autres passionnés**.

🧠 Ce dépôt s’adresse autant :
- aux **professionnels du secteur** souhaitant sonder mes compétences techniques et ma capacité à apprendre seul,
- qu’aux **développeurs et curieux d'IA** à la recherche de ressources détaillées, fiables et gratuites pour progresser dans leur compréhension du domaine.

Voyez ce projet comme un **pont entre la recherche académique et la curiosité libre**, au service de la connaissance partagée.
En ce sens, **toute collaboration sérieuse sur ce projet sera la bienvenue**.