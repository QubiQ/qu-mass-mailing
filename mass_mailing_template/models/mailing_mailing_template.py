# Copyright 2020 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https: //www.gnu.org/licenses/agpl).
from odoo import api, models, fields

MASS_MAILING_BUSINESS_MODELS = [
    'crm.lead',
    'event.registration',
    'hr.applicant',
    'res.partner',
    'event.track',
    'sale.order',
    'mailing.list',
    'mailing.contact'
]


class MailingMailingTemplate(models.Model):
    _name = 'mailing.mailing.template'
    _description = "Mailing Templates"
    _rec_name = "subject"

    use_default = fields.Boolean(
        string="Use By Default",
    )
    active = fields.Boolean(default=True, tracking=True)
    subject = fields.Char(
        'Subject', help='Subject of emails to send', required=True,
        translate=True)
    email_from = fields.Char(string='Send From', )
    mailing_model_id = fields.Many2one(
        'ir.model', string='Recipients Model',
        domain=[('model', 'in', MASS_MAILING_BUSINESS_MODELS)],
        default=lambda self:
            self.env.ref('mass_mailing.model_mailing_list').id)
    body_arch = fields.Html(string='Body', translate=False)
    body_html = fields.Html(
        string='Body converted to be send by mail', sanitize_attributes=False)

    @api.model
    def clean_default(self, model_id):
        self.env['mailing.mailing.template'].search([
            ('use_default', '=', True),
            ('mailing_model_id', '=', model_id),
        ]).write({'use_default': False})

    @api.model
    def create(self, vals):
        if vals.get('use_default') and vals.get('mailing_model_id'):
            self.clean_default(vals['mailing_model_id'])
        return super().create(vals)

    def write(self, vals):
        if vals.get('use_default') and vals.get('mailing_model_id'):
            self.clean_default(vals['mailing_model_id'])
        return super().write(vals)
