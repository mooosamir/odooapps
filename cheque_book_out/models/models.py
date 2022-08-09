
from odoo import models, fields
from datetime import datetime
from odoo.exceptions import UserError
from odoo.addons.portal.controllers.mail import _message_post_helper


class CheckInJournal(models.Model):
    _name = 'account.journal'
    _inherit = 'account.journal'

    is_check = fields.Boolean(string="is Check", default=False)
    account_id = fields.Many2one('account.account', 'ACC Bank - Check',
                                 domain=[('deprecated', '=', False)])
    check_journal = fields.Many2one('account.journal', string="Check Journal")


class CheckInPayment(models.Model):
    _name = 'account.payment'
    _inherit = 'account.payment'

    is_paid = fields.Boolean(string="Is Paid", default=False, copy=False)
    rec_check = fields.Many2one('account.move', string="Check to Bank", copy=False)
    is_check = fields.Boolean(related='journal_id.is_check', string="is Check")
    check_py_date = fields.Date(string="Date in Bank")

    def set_date(self):
        if self.journal_id.is_check and self.partner_type == 'supplier' and self.payment_type == 'outbound' and self.state in ['posted', 'send', 'reconciled']:
            if not self.is_paid:
                if not self.check_py_date:
                    self.check_py_date = datetime.today()
        else:
            raise UserError("Please check the type of transaction ( Payment Type , Partner Type, State )")

    def run_for_paid(self):
        if not self.is_paid:
            if self.journal_id.is_check and self.partner_type == 'supplier' and self.payment_type == 'outbound' and self.state in ['posted', 'send', 'reconciled']:
                _sheet = 'Check '
                name = '{} / {}'.format(_sheet, self.name)
                journal_items_one = {
                    'account_id': self.journal_id.account_id.id, 'name': name,
                    'credit': self.amount
                }
                journal_items_two = {
                    'account_id': self.journal_id.default_credit_account_id.id, 'name': name,
                    'debit': self.amount
                }
                data = {
                    # 'name': name,
                    'date': self.check_py_date,
                    'journal_id': self.journal_id.check_journal.id,
                    'state': 'draft',
                    'ref': name,
                    'line_ids': [(0, 0, journal_items_one), (0, 0, journal_items_two)],
                }
                rec_id = self.env['account.move'].sudo().create(data)
                rec_id.action_post()
                self.rec_check = rec_id.id
                self.is_paid = True
                body = 'The check has been cashed.'
                _message_post_helper(res_model='account.payment', res_id=self.id, message=body,
                                     message_type='notification', subtype="mail.mt_note")
            else:
                raise UserError("Please check the type of transaction ( Payment Type , Partner Type, State )")
        else:
            raise UserError("Already paid from the bank")
