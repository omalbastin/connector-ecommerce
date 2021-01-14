# -*- coding: utf-8 -*-
# © 2013 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    def action_invoice_paid(self):
        res = super().action_invoice_paid()
        for record in self:
            self._event('on_invoice_paid').notify(record)
        return res

    def _post(self, soft=True):
        # OVERRIDE
        posted = super()._post(soft)
        for record in self:
            self._event('on_invoice_validated').notify(record)
        return posted
