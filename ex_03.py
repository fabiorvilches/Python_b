import sqlalchemy

import ex_01

select_operation = sqlalchemy.select(
    [ex_01.users_table  ]
)