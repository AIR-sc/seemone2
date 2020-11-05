# -*- coding: utf-8 -*-

from odoo import models, fields, api

class passwodoo(models.Model):
    _name = 'passwodoo.passwodoo'
    _description = 'passwodoo.passwodoo'

    name = fields.Char()
    description = fields.Integer()
    expiringDate = fields.Date()
    password = fields.Char()

    # Many 2 one verso il cliente
    cliente = fields.Many2one('res.partner', string="Cliente")

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100