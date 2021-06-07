from odoo import models,fields,api, _
from odoo.exceptions import UserError

class ProductGroupTable(models.Model):
    _name = "product.group"
    _description = "testing_product"
    


    name =fields.Char(string="Name",required=True)
    code = fields.Char(string='Short Code',required=True)
    parent_group = fields.Many2one('product.group',string="Parent Group")
    



    @api.onchange('code')
    def onchange_code(self):
        exist = self.env['product.group'].search([])
        if self.code:
            for i in exist:
                if self.code == i.code:
                    raise UserError(_("This Code Already exist"))

    def write(self, values):
        code_exist = self.env ['product.group'].search([('code', '=', values['code'])])
        if code_exist:
            raise UserError(_("This Code Already exist"))
        result = super(ProductGroupTable, self).write(values)
        return result 

     
    @api.model
    def create(self, values):
        code_exist = self.env ['product.group'].search([('code', '=', values['code'])])
        if code_exist:
            raise UserError(_("This Code Already exist"))
        result = super(ProductGroupTable, self).create(values)
        return result
