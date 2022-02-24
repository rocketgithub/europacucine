# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import logging

class AccountMove(models.Model):
    _inherit = "account.move"

    numero_factura = fields.Char('Numero factura',compute='_compute_numero_factura', store = True)

    @api.onchange('payment_reference', 'ref','numero_fel')
    def _onchange_payment_reference(self):
        res = super()._onchange_payment_reference()
        self.payment_reference = (self.serie_fel +"-"+ self.numero_fel) if (self.journal_id.generar_fel and self.numero_fel and self.serie_fel) else ''
        for line in self.line_ids.filtered(lambda line: line.account_id.user_type_id.type in ('receivable', 'payable')):
            line.name =  (self.serie_fel +"-"+ self.numero_fel) if (self.journal_id.generar_fel and self.numero_fel and self.serie_fel) else (self.payment_reference or self.ref)

    def _post(self,soft=True):
        res = super(AccountMove, self)._post(soft)
        for factura in self:
            if factura.journal_id.generar_fel:
                factura._onchange_payment_reference()
        return res

    @api.depends('numero_fel', 'serie_fel')
    def _compute_numero_factura(self):
        for factura in self:
            if factura.serie_fel and factura.numero_fel:
                factura.numero_factura = factura.serie_fel + "-" + factura.numero_fel
            else:
                factura.numero_factura = ""
