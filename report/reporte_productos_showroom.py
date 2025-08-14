# -*- encoding: utf-8 -*-

from odoo import api, models
import logging

class ReporteProductosShowroom(models.AbstractModel):
    _name = 'report.europacucine.productos_showroom'
    _inherit = 'report.europacucine.abstract.productos'

    @api.model
    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_ids', []))
        lineas = self.lineas(True)
        return {
            'doc_ids': self.ids,
            'doc_model': model,
            'data': data['form'],
            'docs': docs,
            'lineas': lineas,
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
