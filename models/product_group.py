from odoo import api, models, fields, _
from odoo.exceptions import UserError


class ParentGroup(models.Model):
    _name = 'parent.group'
    _description = 'Parent Group'
    _rec_name = 'parent_group'

    parent_group = fields.Char(string='Parent Group')

    product_group_line = fields.One2many('product.group.line', 'product_group_id', string='Product Line')


class ProductGroup(models.Model):
    _name = 'product.group'
    _description = 'Product Group'

    name = fields.Char(string='Product Name')


class ProductGroupLine(models.Model):
    _name = 'product.group.line'
    _description = 'Product Group Line'
    _rec_name = 'name_id'

    name_id = fields.Many2one('product.group', string='Product Name')
    short_code = fields.Char(string='Short Code')

    product_group_id = fields.Many2one('parent.group', string='Product Under')


