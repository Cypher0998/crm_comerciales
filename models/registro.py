# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Registro(models.Model):
    _name = 'registro.registro'

    visited_client = fields.Many2one('res.partner', string=_("Visited Client"))
    visit_type = fields.Selection([
    	('casa','Puerta por puerta'),
    	('tlf','Llamada telefónica'),
    	('email','Contacto por correo')
    	],
    	string=_('Tipo de visita'))
    initial_date = fields.Datetime(
        string='Fecha Inicial',
    )
    final_date = fields.Datetime(
        string='Fecha Final',
    )