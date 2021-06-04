from odoo import models,fields,api, _
from datetime import datetime
from odoo.exceptions import UserError



class EmployeeRequisition(models.Model):
    _name = "employee.requisition"
    _description = "test"
    


    name = fields.Many2one('hr.employee',string='Employee Name')
    requisition_date = fields.Date(
                string='Requisition Date', default=datetime.today())

    appoinment_line= fields.One2many('employee.requisition.line','appoinment_id',string='Requisition')
    state= fields.Selection([
            ('draft',"DRAFT"),
            ('confirm',"CONFIRMED"),
            ('approve',"Approved"),
            ('ready',"READY"),
            ('receive',"RECEIVED"),
        ], string="status", default='draft')

    def button_confirm(self):
        self.write({'state': 'confirm'})

    def button_approve(self):
        self.write({'state': 'approve'})

    def button_ready(self):
        self.write({'state': 'ready'})

    def button_receive(self):
        self.write({'state': 'receive'})

class EmployeeRequisitionLine(models.Model):
    _name = "employee.requisition.line"
    _description = "test_two"
    


    product_name = fields.Many2one('product.template',string='Product Name',required=True)
    product_qty = fields.Integer(string='Quanty',required=True)
    appoinment_id= fields.Many2one('employee.requisition',string='Appoinment Id')
