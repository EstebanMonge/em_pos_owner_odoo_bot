{
    'name': 'POS session user to odoo bot change',
    'version': '12.0.1.0.0',
    'summary': 'Change the owner of a pos session to make possible close it',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_session_views.xml',
    ],
    'installable': True,
    'application': False,
}
