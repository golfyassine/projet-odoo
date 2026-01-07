from odoo import models, fields

class Salle(models.Model):
    _name = "gestion.salle"
    _description = "Salle de réunion"

    name = fields.Char(string="Nom de la salle", required=True)
    capacite = fields.Integer(string="Capacité (personnes)")
    a_projecteur = fields.Boolean(string="Projecteur vidéo disponible ?")
    a_climatisation = fields.Boolean(string="Climatisation ?")
    description = fields.Text(string="Description / Notes")