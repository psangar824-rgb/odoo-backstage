{
    'name': 'BackStage Rent',
    'version': '19.0.1.0.0',
    'summary': 'Alquiler de equipos audiovisuales',
    'author': 'Tu nombre',
    'category': 'Services',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/equipo_views.xml',
    ],
    'application': True,
    'installable': True,
}