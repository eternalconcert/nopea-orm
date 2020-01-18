old_state = {}

actions = {'creations': {'Address': {'fields': [{'test': {'field_attrs': {'default': True},
                                                'field_type': 'BooleanField'}},
                                      {'a': {'field_attrs': {},
                                             'field_type': 'IntegerField'}},
                                      {'id': {'field_attrs': {},
                                              'field_type': 'PkField'}}],
                           'tablename': 'address'},
               'User': {'fields': [{'first_name': {'field_attrs': {'max_length': 250},
                                                   'field_type': 'CharField'}},
                                   {'username': {'field_attrs': {'max_length': 250},
                                                 'field_type': 'CharField'}},
                                   {'id': {'field_attrs': {},
                                           'field_type': 'PkField'}}],
                        'tablename': 'user'}}}

new_state = {'Address': {'fields': [{'test': {'field_attrs': {'default': True},
                                  'field_type': 'BooleanField'}},
                        {'a': {'field_attrs': {},
                               'field_type': 'IntegerField'}},
                        {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
             'tablename': 'address'},
 'User': {'fields': [{'first_name': {'field_attrs': {'max_length': 250},
                                     'field_type': 'CharField'}},
                     {'username': {'field_attrs': {'max_length': 250},
                                   'field_type': 'CharField'}},
                     {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
          'tablename': 'user'}}

