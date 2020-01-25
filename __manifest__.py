# -*- coding: utf-8 -*-

{
    'name': 'Website Add Skype',
    'version': '1.0',
    'category': 'website',
    'sequence': 6,
    'author': 'Webveer',
    'summary': 'This module allows you to add skype in your Odoo website.',
    'description': """

=======================
This module allows you to add skype in your Odoo website.

""",
    'depends': ['website'],
    'data': [
        'views/template.xml',
        'views/views.xml',
    ],
    'qweb': [

    ],
    'images': [
        'static/description/popup.jpg',
    ],
    'installable': True,
    'website': '',
    'auto_install': False,
    'price': 15,
    'currency': 'EUR',
}
