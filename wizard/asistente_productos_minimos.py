# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import time

class AsistenteProductosMinimos(models.TransientModel):
    _name = 'europacucine.asistente_productos_minimos'

    def print_report(self):
        data = {
             'ids': [],
             'model': 'europacucine.asistente_productos_minimos',
             'form': self.read()[0]
        }
        return self.env.ref('europacucine.action_productos_minimos').report_action(self, data=data)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
