# -*- coding: utf-8 -*-
{
    'name':'OpWall data module',
    'version':'1.0',
    'category':'Configuration',
    'sequence': 2,
    'summary' : 'Data container for runtime data.',
    'description': """
This module contains data for the OpWall project. Do not introduce
    dependencies for this module, although it clearly depends on the proper
    configuration of the database, we want this module to run in isolation.
    The proper structure of the data is the responsibility of the author.
""",
    'author': 'HSD',
    'website': 'http://www.hsdev.com',
    'depends': [],
    'data' : [
        # Insert datafiles which need to be evaluated during upgrade here, typically xml or csv files
        # Name csv files after the model they import into: example: model res.partner -> res.partner.csv
        'data/res.partner.csv'
    ],
    'demo' : [],
    'installable': True,
    'auto_install': False,
    'application': False,
    'images' : [],
    'web'  : True,
    'css'  : [],
    'js'   : [],
    'qweb' : [],
}
