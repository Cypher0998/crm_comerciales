# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import logging
from datetime import datetime


_logger = logging.getLogger(__name__)

class Registro(models.Model):
    _name = 'registro.registro'

    def _get_employee_id(self):
        employee_rec = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        return employee_rec.id

    employee = fields.Many2one('hr.employee', string=_("Comercial"),default=_get_employee_id,readonly=True, required=True)
    visited_client = fields.Many2one('res.partner', string=_("Cliente Visitado"))
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
    visitado = fields.Boolean(default=False)
    visita_terminada = fields.Boolean(default=False)
    geo_lat = fields.Char(string=_('Latitud'))
    geo_long = fields.Char(string = _('Longitud'))

#funciones que controlan el inicio y final de la visita
    @api.multi
    def check_date_in(self):
        self.initial_date = datetime.now()
        self.visitado = True

    def check_date_out(self):
        self.final_date = datetime.now()
        self.visita_terminada = True