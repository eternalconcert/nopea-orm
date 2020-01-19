old_state = {}

actions = {'creations': {'Address': {'fields': [{'a': {'field_attrs': {},
                                             'field_type': 'IntegerField'}},
                                      {'id': {'field_attrs': {},
                                              'field_type': 'PkField'}}],
                           'tablename': 'address'},
               'User': {'fields': [{'username': {'field_attrs': {'max_length': 250},
                                                 'field_type': 'CharField'}},
                                   {'first_name': {'field_attrs': {'max_length': 250},
                                                   'field_type': 'CharField'}},
                                   {'id': {'field_attrs': {},
                                           'field_type': 'PkField'}}],
                        'tablename': 'user'}}}

new_state = {'Address': {'fields': [{'a': {'field_attrs': {},
                               'field_type': 'IntegerField'}},
                        {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
             'tablename': 'address'},
 'User': {'fields': [{'username': {'field_attrs': {'max_length': 250},
                                   'field_type': 'CharField'}},
                     {'first_name': {'field_attrs': {'max_length': 250},
                                     'field_type': 'CharField'}},
                     {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
          'tablename': 'user'}}

