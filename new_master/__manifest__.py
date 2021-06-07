{
    'name' : "new master table Product Group",
    'version' :'1.0',
    'sequence' : 1,
    'website': 'https://www.odoo.com',
    'summary': 'Product Group Table',
    'description' : "Product Group management system",
    'depends' : ['base','contacts','sale_management','purchase'],
    'data' : [
        'views/product_group.xml',
        'views/purchase_order.xml',
        'views/wizad.xml',
   ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}