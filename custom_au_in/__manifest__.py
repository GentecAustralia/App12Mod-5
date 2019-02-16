# -*- coding: utf-8 -*-


{
    'name': 'App12Mod-5 Custom_Au_In',
    'version': '12.0.0.0',
    'category': 'Accounting',
    'summary': 'Custom_AU_In Version 5',
    'description': """ This apps automatically create invoice from Picking when picking(Shipment/Delivery) get done
""",
    'depends': ['sale','purchase','stock','Au_In12'],
    'data': [
        'report/custom_report.xml',
        'report/custom_stock_picking_report.xml',
        ],
    'demo': [],
    'js': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
