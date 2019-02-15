# -*- coding: utf-8 -*-
# Copyright 2019 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Iban invoice",
    "version": "10.0.1.2.0",
    "description": "This module defines the bank account to be displayed in the invoice print.",
    "category": "Account",
    "website": "http://www.apuliasoftware.it",
    "author": "Ilaria Franchini",
    "depends": [
        'base',
        'base_iban',
        'sale',
        'account'
    ],
    "data": [
        'views/partner_view.xml',
        'views/account_invoice.xml',
        'data/account_bank_menu.xml'
    ],
    'installable': True,
}
