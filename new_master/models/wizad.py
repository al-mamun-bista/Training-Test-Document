from odoo import models, fields, api, _
from odoo.exceptions import UserError


class purchasefilter(models.TransientModel):
    _name = 'purchase.filter'
    add_date= fields.Integer(string="Customer")