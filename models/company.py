# -*- coding: utf-8 -*-

from odoo import api, fields, models

class res_company(models.Model):
    _inherit = "res.company"

    skype_name = fields.Char(string='Skype')




