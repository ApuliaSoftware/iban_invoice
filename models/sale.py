# -*- coding: utf-8 -*-
# Copyright 2019 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class SaleOrder(models.Model):

    _inherit = "sale.order"

    @api.multi
    # ---- inherit prepare_invoice to pass information about the bank account
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        if self.partner_id:
            partner_bank_id = False
            print(partner_bank_id)
            if self.partner_id.bank_transfer_account:
                partner_bank_id = \
                    self.partner_id.bank_transfer_account
            else:
                for bank in self.company_id.partner_id.bank_ids:
                    if bank.main_bank_transfer_account and not\
                            self.partner_bank_id:
                        partner_bank_id = bank
            if not partner_bank_id:
                partner_bank_id = self.company_id.partner_id.bank_ids[0]
            res.update({'partner_bank_id': partner_bank_id.id})
            return res
