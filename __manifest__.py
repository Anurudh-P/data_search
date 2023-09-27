{
    'name': 'Data Search',
    'version': '16.0.1.0.0',
    'sequence': 16,
    'summary': 'data search ',
    'depends': [
        'base_setup',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/data_search.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
