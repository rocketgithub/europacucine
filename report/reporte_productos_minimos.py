# -*- encoding: utf-8 -*-

from odoo import api, models
import logging

class ReporteProuctosMinimos(models.AbstractModel):
    _name = 'report.europacucine.productos_minimos'
    _inherit = 'report.europacucine.abstract.productos'

    @api.model
    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        lineas = self.lineas(False)

        return {
            'doc_ids': self.ids,
            'doc_model': model,
            'lineas': lineas,
        }
