{
    'name' : "Employee want",
    'version' :'1.0',
    'sequence' : 1,
    'website': 'https://www.odoo.com',
    'summary': 'For test purpose',
    'description' : "xyz organization management system",
    'depends' : ['base','contacts','sale_management','purchase'],
    'data' :[
        'security/employee_security.xml',
        'security/ir.model.access.csv',
        'views/employee.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
