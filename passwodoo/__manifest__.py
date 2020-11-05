# -*- coding: utf-8 -*-
{
    'name': "Passwodoo",

    'summary': """
       Password manager for odoo""",

    'description': """
        Made with love (and possibly some bugs) by Seemone
    """,

    'author': "Seemone",
    'website': "http://www.seemone.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}