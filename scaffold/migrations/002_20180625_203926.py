old_state = {'Address': {'fields': [{'test': {'field_attrs': {'default': True},
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

actions = {'fields_to_add': {'Address': [{'test2': {'field_attrs': {'default': False},
                                          'field_type': 'BooleanField'}}]}}

new_state = {'Address': {'fields': [{'a': {'field_attrs': {},
                               'field_type': 'IntegerField'}},
                        {'test2': {'field_attrs': {'default': False},
                                   'field_type': 'BooleanField'}},
                        {'test': {'field_attrs': {'default': True},
                                  'field_type': 'BooleanField'}},
                        {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
             'tablename': 'address'},
 'User': {'fields': [{'username': {'field_attrs': {'max_length': 250},
                                   'field_type': 'CharField'}},
                     {'first_name': {'field_attrs': {'max_length': 250},
                                     'field_type': 'CharField'}},
                     {'id': {'field_attrs': {}, 'field_type': 'PkField'}}],
          'tablename': 'user'}}

