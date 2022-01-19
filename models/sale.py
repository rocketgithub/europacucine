# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
import logging

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends('invoice_ids')
    def _obtener_facturado(self):
        for pedido in self:
            facturado = pendiente_facturar =  0.0
            if pedido.invoice_ids:
                for factura in pedido.invoice_ids:
                    facturado += factura.amount_total

                pendiente_facturar = pedido.amount_total - facturado

            pedido.update({
                'facturado': facturado,
                'pendiente_facturar': pendiente_facturar
            })

    facturado = fields.Monetary(string='Facturado', store=True, readonly=True, compute='_obtener_facturado')
    pendiente_facturar = fields.Monetary(string='Pendiente facturar', store=True, readonly=True, compute='_obtener_facturado')
