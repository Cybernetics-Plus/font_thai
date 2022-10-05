# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    Add Fonts Thai to Document Layout
#
#    Copyright (C) 2021-TODAY Cybernetics Plus Technologies (<https://www.cybernetics.plus>).
#    Author: Cybernetics Plus Techno Solutions (<https://www.cybernetics.plus>)
#
###################################################################################

{
    'name': 'Fonts Thai',
    'version': '15.0.1.0.1',
    'summary': """ 
            Add Fonts Thai to Document Layout
            .""",
    'description': """ 
            Add Fonts Thai to Document Layout
            .""",
    'author': 'Cybernetics Plus Co., Ltd.',
    'website': 'https://www.cybernetics.plus',
    'live_test_url': 'https://www.cybernetics.plus',
    'images': ['static/description/icon.png'],
    "category": "Report",
    "license": "AGPL-3",
    'price': 9.99,
    'currency': 'EUR',
    'application': True,
    'installable': True,
    'auto_install': True,
    'contributors': [
        'Developer <dev@cybernetics.plus>',
    ],
    "depends": ["web"],
    "assets":{
        'web.report_assets_common': [
            'ctp_fonts_th/static/src/scss/fonts_style.scss',
        ],
        'web.report_assets_pdf': [
            'ctp_fonts_th/static/src/scss/fonts_style.scss',
        ],
    }
}