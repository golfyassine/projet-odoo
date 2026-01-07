# Gestion des Réservations de Salles

## 📋 Description

Module Odoo 17 pour la gestion complète des réservations de salles de réunion. Ce système permet de gérer efficacement les salles disponibles et leurs réservations au sein d'une organisation.

## 👤 Auteur

**Yassine Bekkouch**

## 📦 Informations du Module

- **Nom**: Gestion des Réservations de Salles
- **Version**: 1.0
- **Catégorie**: Productivity
- **Type**: Application
- **Dépendances**: base

## 🏗️ Structure du Projet

```
gestion_salles/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── salle.py
│   └── reservation.py
├── views/
│   ├── salle_views.xml
│   └── reservation_views.xml
└── security/
    └── ir.model.access.csv
```

## 🎯 Fonctionnalités

### 1. Gestion des Salles (`gestion.salle`)

Le module permet de créer et gérer des salles de réunion avec les informations suivantes :

- **Nom de la salle** (requis)
- **Capacité** (nombre de personnes)
- **Projecteur vidéo** (disponibilité)
- **Climatisation** (disponibilité)
- **Description / Notes** (informations complémentaires)

### 2. Gestion des Réservations (`gestion.reservation`)

Système de réservation complet incluant :

- **Objet de la réunion** (requis)
- **Salle** (sélection parmi les salles disponibles, requis)
- **Début** (date et heure de début, requis)
- **Fin** (date et heure de fin, requis)
- **Organisateur** (utilisateur responsable, défaut: utilisateur actuel)
- **Statut** :
  - Brouillon (par défaut)
  - Confirmé
  - Annulé

## 🔐 Sécurité

Le module inclut des règles d'accès configurées dans `ir.model.access.csv` :

- Accès complet (lecture, écriture, création, suppression) pour les salles
- Accès complet (lecture, écriture, création, suppression) pour les réservations

## 🚀 Installation

1. Placez le module dans le répertoire `addons` d'Odoo
2. Redémarrez le serveur Odoo
3. Activez le mode développeur
4. Allez dans Applications
5. Cliquez sur "Mettre à jour la liste des applications"
6. Recherchez "Gestion des Réservations de Salles"
7. Cliquez sur "Installer"

## 💻 Modèles de Données

### Modèle Salle

```python
_name = "gestion.salle"
_description = "Salle de réunion"

Champs:
- name: Char (requis)
- capacite: Integer
- a_projecteur: Boolean
- a_climatisation: Boolean
- description: Text
```

### Modèle Réservation

```python
_name = "gestion.reservation"
_description = "Réservation de salle"

Champs:
- name: Char (requis)
- salle_id: Many2one -> gestion.salle (requis)
- date_debut: Datetime (requis)
- date_fin: Datetime (requis)
- responsable_id: Many2one -> res.users
- statut: Selection ['brouillon', 'confirme', 'annule']
```

## 📱 Utilisation

### Créer une Salle

1. Accédez au menu "Salles"
2. Cliquez sur "Créer"
3. Remplissez les informations de la salle
4. Sauvegardez

### Créer une Réservation

1. Accédez au menu "Réservations"
2. Cliquez sur "Créer"
3. Saisissez l'objet de la réunion
4. Sélectionnez la salle souhaitée
5. Définissez les dates et heures de début et fin
6. Le statut est automatiquement défini sur "Brouillon"
7. Sauvegardez et confirmez si nécessaire

## 🔄 États de Réservation

- **Brouillon**: Réservation en cours de création ou modification
- **Confirmé**: Réservation validée et active
- **Annulé**: Réservation annulée

## 📄 Fichiers Principaux

- `__manifest__.py`: Configuration du module
- `models/salle.py`: Modèle de données pour les salles
- `models/reservation.py`: Modèle de données pour les réservations
- `views/salle_views.xml`: Vues pour la gestion des salles
- `views/reservation_views.xml`: Vues pour la gestion des réservations
- `security/ir.model.access.csv`: Règles d'accès et de sécurité

## 🛠️ Technologies

- **Framework**: Odoo 17
- **Langage**: Python 3
- **Base de données**: PostgreSQL (via Odoo)

## 📝 Notes

- Le module est marqué comme `application=True`, ce qui le rend visible comme application principale dans Odoo
- L'organisateur d'une réservation est automatiquement défini sur l'utilisateur connecté
- Le statut par défaut d'une nouvelle réservation est "Brouillon"

---

*Module développé pour faciliter la gestion des salles de réunion et optimiser l'utilisation des espaces dans l'entreprise.*
