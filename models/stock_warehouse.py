# -*- coding: utf-8 -*-

from odoo import fields, models, api
import base64
import logging

class Warehouse(models.Model):
    _inherit = 'stock.warehouse'

    reporte_productos_minimos = fields.Many2many(
        'res.partner', 
        'res_company_minimos_partner_rel',
        'company_id',
        'partner_id',
        string='Reporte de productos mínimos'
    )
    reporte_productos_showroom = fields.Many2many(
        'res.partner',
        'res_company_showroom_partner_rel',
        'company_id',
        'partner_id',
        string='Reporte de productos showroom'
    )

    @api.model
    def enviar_reportes_productos(self):
        almacenes = self.search([])
        for almacen in almacenes:

            if almacen.reporte_productos_minimos:
                correos = ",".join(almacen.reporte_productos_minimos.mapped("email"))
                if correos:
                    template_minimos = self.env.ref("europacucine.mail_template_productos_minimos")
                    report = self.env.ref('europacucine.europacucine_reporte_minimos')._render_qweb_pdf(almacen.id)
                    filename = 'reporte_minimos.pdf'
                    attachments = [('%s' % filename, base64.b64encode(report[0]))]

                    template_minimos.with_context(email_to=correos).send_mail(almacen.id, email_values={'attachments': attachments})

            if almacen.reporte_productos_showroom:
                correos = ",".join(almacen.reporte_productos_showroom.mapped("email"))
                if correos:
                    template_showroom = self.env.ref("europacucine.mail_template_productos_showroom")

                    report = self.env.ref('europacucine.europacucine_reporte_showroom')._render_qweb_pdf(almacen.id)
                    filename = 'reporte_showroom.pdf'
                    attachments = [('%s' % filename, base64.b64encode(report[0]))]

                    template_showroom.with_context(email_to=correos).send_mail(almacen.id, email_values={'attachments': attachments})

