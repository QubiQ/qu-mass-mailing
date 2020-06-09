# Copyright 2020 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https: //www.gnu.org/licenses/agpl).
from odoo import api, models, fields


class MailingMailing(models.Model):
    _inherit = 'mailing.mailing'

    @api.model
    def get_default_template_id(self):
        template_id = False
        if self._context.get('default_mailing_model_id'):
            template_id = self.env['mailing.mailing.template'].search(
                [
                    ('use_default', '=', True),
                    ('mailing_model_id', '=',
                     self._context.get('default_mailing_model_id'))
                ]
            )
            template_id = template_id[0] if template_id else False
        return template_id

    template_id = fields.Many2one(
        comodel_name='mailing.mailing.template',
        default=get_default_template_id)

    subject = fields.Char(
        compute="_compute_template_id_values",
        store=True,
        readonly=False,
    )
    body_arch = fields.Html(
        compute="_compute_template_id_values",
        store=True,
        readonly=False,
    )
    body_html = fields.Html(
        compute="_compute_template_id_values",
        store=True,
        readonly=False,
    )

    @api.depends('template_id')
    def _compute_template_id_values(self):
        self.body_arch = False
        self.boddy_html = False
        self.subject = False
        for rec in self.filtered('template_id'):
            rec.body_arch = rec.template_id.body_arch
            rec.body_html = rec.template_id.body_html
            rec.subject = rec.template_id.subject
