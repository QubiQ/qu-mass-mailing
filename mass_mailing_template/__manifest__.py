# Copyright 2020 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https: //www.gnu.org/licenses/agpl).

{
    "name": "Mass Mailing Template",
    "summary": "Mass Mailing Template",
    "version": "13.0.1.0.0",
    "category": "Pro",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ['mass_mailing',],
    "data": [
        "security/ir.model.access.csv",
        "views/mailing_mailing.xml",
        "views/mailing_mailing_template.xml",
    ],
}
