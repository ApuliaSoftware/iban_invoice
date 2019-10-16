# -*- coding: utf-8 -*-
# Copyright 2019 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class SaleAdvancePaymentInv(models.TransientModel):

    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        res = super(
            SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
        if res.partner_id:
            partner_bank_id = False
            if res.partner_id.bank_transfer_account:
                partner_bank_id = \
                    res.partner_id.bank_transfer_account
            else:
                acc_bank = self.env['res.partner.bank'].search([
                    ('main_bank_transfer_account', '=', True)], limit=1)
                if acc_bank:
                    partner_bank_id = acc_bank
            if not partner_bank_id:
                if res.company_id.partner_id.bank_ids:
                    partner_bank_id = res.company_id.partner_id.bank_ids[0]
            if partner_bank_id:
                res.update({'partner_bank_id': partner_bank_id.id})
            return res
