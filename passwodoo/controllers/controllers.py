# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    @http.route('/passwodoo/passwodoo/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/passwodoo/passwodoo/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('passwodoo.listing', {
            'root': '/passwodoo/passwodoo',
            'objects': http.request.env['passwodoo.passwodoo'].search([]),
        })

    @http.route('/passwodoo/passwodoo/objects/<model("passwodoo.passwodoo"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('passwodoo.object', {
            'object': obj
        })