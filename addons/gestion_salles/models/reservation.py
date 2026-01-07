from odoo import models, fields

class Reservation(models.Model):
    _name = "gestion.reservation"
    _description = "Réservation de salle"

    name = fields.Char(string="Objet de la réunion", required=True)
    salle_id = fields.Many2one("gestion.salle", string="Salle", required=True)
    date_debut = fields.Datetime(string="Début", required=True)
    date_fin = fields.Datetime(string="Fin", required=True)
    responsable_id = fields.Many2one("res.users", string="Organisateur", default=lambda self: self.env.user)
    statut = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
    ], string="Statut", default='brouillon')