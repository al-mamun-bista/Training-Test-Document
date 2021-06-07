from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchseOrder(models.Model):
    _inherit = 'purchase.order'

    product_group = fields.Many2one('product.group', string="Product Group")
    active_group_filter =fields.Boolean(string="Active Group Filter")
    

##################################################################################################
class PurchaseOrderLine(models.Model):    
    _inherit = 'purchase.order.line'



class PurchaseOrderLine(models.Model):    
    _inherit = 'product.template'
    group= fields.Many2one('product.group', string="Group")