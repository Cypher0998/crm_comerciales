# -*- coding: utf-8 -*-
from odoo import http

# class CrmComerciales(http.Controller):
#     @http.route('/crm_comerciales/crm_comerciales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_comerciales/crm_comerciales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_comerciales.listing', {
#             'root': '/crm_comerciales/crm_comerciales',
#             'objects': http.request.env['crm_comerciales.crm_comerciales'].search([]),
#         })

#     @http.route('/crm_comerciales/crm_comerciales/objects/<model("crm_comerciales.crm_comerciales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_comerciales.object', {
#             'object': obj
#         })