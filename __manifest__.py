{
    'name' : 'Bista Product Group',
    'version' : '1.0',
    'sequence' : 1,
    'summary': 'Bista Product Group Summary',
    'description' : 'Bista Product Group Description.',
    'depends' : ['base', 'purchase', 'sale_management','stock'],
    'data' : [
        'security/product_group_security.xml',
        'security/ir.model.access.csv',

        'views/product_group_views.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
