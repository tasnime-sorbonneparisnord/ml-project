# Cookiecutter ML Project

## Auteur

Hakimi Tasnime + AOUN Myriam

## Objectif du projet

Ce projet a pour objectif de concevoir un template Cookiecutter réutilisable pour la création de projets de Machine Learning.

Il permet de standardiser l’architecture des projets, d’automatiser les étapes répétitives et de fournir une base de code cohérente, maintenable et directement exploitable.

## Objectifs principaux

- Générer rapidement un projet ML structuré
- Garantir une architecture standardisée et maintenable
- Intégrer des outils essentiels (tests, formatage, configuration Python)
- Faciliter la collaboration entre développeurs
- Réduire les erreurs lors de la création de projets

## Structure du projet

src/
data/
output/
tests/

## Architecture du projet

Le projet est organisé selon une architecture modulaire :

- loaders : chargement des données
- processors : traitement et nettoyage des données
- translators : traduction ou transformation des données
- evaluators : évaluation des résultats
- orchestrator : coordination du pipeline

## Pipeline ML

Le pipeline implémente les étapes suivantes :

1. Chargement des données
2. Traduction automatique
3. Traitement des résultats
4. Évaluation avec la métrique BLEU
5. Affichage des résultats

## Technologies utilisées

- Python 3.10+
- Cookiecutter
- pytest
- black

## Exécution du projet

```bash
python main.py
