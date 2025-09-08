# -*- coding: utf-8 -*-
{
    'name': "Europa Cucine",

    'summary': """ Europa Cucine """,

    'description': """
         Módulo para Europa Cucine
    """,

    'author': "Aquih S.A.",
    'website': "http://www.aquih.com",

    'category': 'Uncategorized',
    'version': '0.3',

    'depends': ['sale', 'purchase', 'stock', 'account', 'fel_gt', 'account_reports'],

    'data': [
        'views/account_move_views.xml',
        'views/reporte_productos_minimos.xml',
        'views/reporte_productos_showroom.xml',
        'views/product_template_views.xml',
        'views/report.xml',
        'views/sale_views.xml',
        'views/stock_warehouse_views.xml',
        'data/email_templates.xml',
        'data/cron_enviar_reportes.xml',
    ],
}
