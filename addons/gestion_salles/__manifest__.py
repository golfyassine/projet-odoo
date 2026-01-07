{
    "name": "Gestion des Réservations de Salles",
    "version": "1.0",
    "summary": "Système complet de réservation de salles",
    "category": "Productivity",
    "author": "Yassine Bekkouch",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/salle_views.xml",
        "views/reservation_views.xml",
    ],
    "installable": True,
    "application": True,
}