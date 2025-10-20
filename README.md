# Fête de la Science @CRNL-EduWell-MEL

**Thème 2025 : Intelligences**

**Concept : Apprentissage humain vs machine**

**Atelier : ZootopIA, à la croisée des intelligences**

**Public visé : à partir de 12 ans**

**Durée : 1 heure**

## Présentation

Ce projet a été développé dans le cadre de la **Fête de la Science 2025**.
L’atelier a été conçu par l’équipe **EduWell – Memory & Learning (MEL)** du **Centre de Recherche en Neurosciences de Lyon (CRNL)**.

Objectif : vulgariser et comparer les mécanismes d’apprentissage chez l’humain et chez la machine, en mettant en lumière leurs similarités, différences et complémentarités.

## Objectifs pédagogiques

* Illustrer les principes de **l’apprentissage humain** (mémoire, attention, renforcement, oubli).
* Expliquer les bases de **l’apprentissage machine** (réseaux de neurones, données, ajustement de poids).
* Favoriser la compréhension du concept d’**intelligence** sous plusieurs formes.
* Encourager l’esprit critique sur les relations entre cognition biologique et intelligence artificielle.

## Déroulé de l’atelier

### 1. Accueil et mise en contexte

Présentation de la mission : les participant·es deviennent des **chercheurs** chargés de construire le modèle le plus performant pour **détecter des tumeurs cérébrales** à partir d’images IRM (jeu de données *BRATS*).

Organisation possible : travail en **équipes** ou en **collaboration collective**.

Objectif : comprendre les enjeux de la quantité et de la qualité des données, de leur correcte labellisation, permettant de répondre au problème.

### 2. Mini-jeu 1 : Entraîner un modèle

Utilisation de **Teachable Machine** pour créer un modèle d’apprentissage pas à pas via la **webcam**.
Les participant·es observent comment les exemples influencent les performances.

**Points à retenir :**

* Un modèle nécessite **beaucoup d’images**.
* Ces images doivent être **variées** (angles, luminosité, arrière-plans) et **représentatives** de la réalité (attention à la class imbalance).
* Il faut parfois ruser pour mieux représenter la réalité (ex. ajouter une classe pour représenter les anomalies).

### 3. Mini-jeu 2 : Les biais de l’intelligence

Exploration des biais :

* **Humain**: perception (ce que l’on croit voir), confirmation (ce que l’on veut voir), disponibilité (ce dont on se souvient facilement).
* **Apprentissage machine**: biais liés aux données (sur-représentation, échantillons non équilibrés, variables implicites).
Illustrations proposées :
Images : un arrière-plan inhabituel modifie la détection d’une tumeur.
Sons : un bruit de fond (hôpital vs salle neutre) influence la reconnaissance vocale.
Données patients : un modèle prédictif biaisé selon le sexe, l’âge ou l’origine.
Texte : associations de mots reflétant des stéréotypes dans les corpus d’entraînement.

**Points à retenir :**

* En tant qu’humains, nous sommes traversés par de nombreux biais cognitifs.
* En tant que scientifiques, nous devons identifier et limiter les biais dans nos modèles.
* Les biais humains peuvent se transférer aux modèles d’IA (ex. sexisme, racisme, stéréotypes culturels).
* Comprendre ces biais est essentiel pour construire une intelligence artificielle fiable, équitable et responsable.
  
### 4. Mini-jeu 3 : Quiz interactif

Questions-réponses pour consolider les notions vues : apprentissage, biais, données, mémoire.

### 5. Conclusion – Mission finale

Retour sur la mission : les participant·es collaborent entre eux et avec la machine pour atteindre le meilleur score final.
Cette coopération illustre la complémentarité entre intelligence humaine et intelligence artificielle.

**Message de clôture :**
C’est grâce à notre raisonnement, notre créativité et notre capacité à nous remettre en question que nous concevons ces modèles.
Mais, contrairement à nous, la machine n’a pas de recul : elle applique ce qu’on lui apprend, même lorsque c’est faux.
Notre rôle est donc de rester vigilants, de questionner les résultats et d’utiliser l’IA comme outil d’aide, jamais comme vérité absolue.

## Pistes d'amélioration

* **Recadrer la mission** : orienter l’atelier vers un domaine plus médical. Si l’objectif reste de travailler sur des images pour un rendu visuel adapté aux enfants, le dataset BRATS pour la segmentation des tumeurs est pertinent, surtout que c’est une tâche complexe, inaccessible aux enfants, ce qui renforce l’effet pédagogique.

* **Introduire des concepts scientifiques** : aborder des notions comme les biais cognitifs dans l’apprentissage humain, en utilisant des exemples imagés facilement compréhensibles par les enfants.

* **Clarifier le vocabulaire** : les enfants ont tendance à associer “IA” uniquement aux grands modèles génératifs (texte, images, voix), et peuvent sous-estimer que des modèles plus simples, comme la simple classification d’images, relèvent de l’apprentissage machine, et donc de l'IA. Il serait utile d’accompagner les mots-clés introduits (par exemple étiquette, neurone, biais) de visuels, par exemple un schéma récapitulatif construit avec eux au tableau, plutôt que de compter uniquement sur l’explication orale.
 
* **Clarifier l’approche modèles vs données** : actuellement, l’atelier présente l'importance du choix des données, mais ne montre pas la diversité des architectures possibles. Il serait utile de leur faire entrevoir que l’apprentissage machine comporte deux volets : les modèles et les données, pour donner une vision plus complète du fonctionnement de l’IA.
 
* **Varier les supports** : explorer d’autres formats que les images, par exemple des fichiers audio à écouter, du texte ou des dossiers patients à analyser.

* **Adapter la durée** : si toutes ces améliorations sont intégrées, l’atelier pourrait durer 1h30 à 2h, ce qui reste court pour un sujet aussi vaste.

* **Repenser la mission finale** : concevoir une tâche sur laquelle les enfants peuvent travailler de manière autonome, en reprenant bien les concepts appris.

## Structure du dépôt

```
Fete-de-la-science-MEL/
│
├── intro/
├── mini-jeu1/
├── mini-jeu2/
├── mini-jeu3/
├── mission-finale/
├── autre/
└── README.md
```

## Équipe

**CRNL – EduWell (Memory & Learning Team)**

Responsable scientifique : *Pauline Mouchès, Post-doctorante*

Membres : *Thomas Geraud, Doctorant* ; *Elias Boulanger, Doctorant* ; *Agnès Guinard, Ingénieure*

## Licence

??
