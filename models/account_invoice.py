# -*- coding: utf-8 -*-
# Copyright 2019 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.onchange('partner_id')
    def change_partner_id(self):
        self.partner_bank_id = False
        # ---- Checks if the field bank_transfer_account specifics the main bank
        if self.partner_id.bank_transfer_account:
            self.partner_bank_id =\
                self.partner_id.bank_transfer_account
        else:
            # ----Checks if a company bank is set as main bank transfer
            for bank in self.company_id.partner_id.bank_ids:
                if bank.main_bank_transfer_account and not self.partner_bank_id:
                    self.partner_bank_id = bank
        # ---- If there isn't a main bank trasfer, it takes the first
        if not self.partner_bank_id:
            self.partner_bank_id = self.company_id.partner_id.bank_ids[0]
