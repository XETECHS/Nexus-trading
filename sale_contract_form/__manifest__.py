# -*- coding: utf-8 -*-

{
    'name': 'Sale Contract Form',
    'version': '1.0',
    'author': 'Xetechs GT',
    'website': 'https://xetechs.com',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
        'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_contract_views.xml',
        'views/sale_views.xml',
        'views/sale_portal_templates.xml'
    ]
}