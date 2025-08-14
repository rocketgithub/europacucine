# -*- encoding: utf-8 -*-

from odoo import api, models
import logging

class ReporteAbstractProductos(models.AbstractModel):
    _name = 'report.europacucine.abstract.productos'

    def obtener_cadena_categorias(self, categoria):
        cadena = []
        while categoria:
            cadena.insert(0, categoria.name)
            categoria = categoria.parent_id
        return ' / '.join(cadena)

    def preparar_valores_diccionario(self, producto, showroom):
        product_id = producto.product_variant_id.id
        lineas_po = self.env['purchase.order.line'].search([('product_id', '=', product_id), ('order_id.state', 'in', ['purchase', 'done'])])

        cantidad_pedida = 0.0
        for linea in lineas_po:
            pendiente = linea.product_qty - linea.qty_received
            if pendiente > 0:
                cantidad_pedida += pendiente

        valor_minimo = min(producto.product_variant_id.orderpoint_ids.mapped('product_min_qty') or [0.0])

        if not showroom and producto.qty_available >= valor_minimo:
            return False

        return {
            'product_id': producto,
            'valor_minimo': valor_minimo,
            'cantidad_pedida': cantidad_pedida,
        }

    def obtener_productos(self, showroom=False):
        domain = [('categ_id', '!=', False)]
        if showroom:
            domain.append(('showroom', '=', True))
        return self.env['product.template'].search(domain, order='name asc')

    def lineas(self, showroom=False):
        lineas = {}
        productos = self.obtener_productos(showroom)

        for producto in productos:
            cadena_categoria = self.obtener_cadena_categorias(producto.categ_id)
            dict_producto = self.preparar_valores_diccionario(producto, showroom)

            if dict_producto:
                if cadena_categoria not in lineas:
                    lineas[cadena_categoria] = []
                lineas[cadena_categoria].append(dict_producto)

        return dict(sorted(lineas.items()))
