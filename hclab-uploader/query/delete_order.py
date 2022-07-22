from sqlalchemy.exc import SQLAlchemyError

def delete_row(engine:object):

  sql = 'update lis_order set flag = 1 where ono = "LAB0004"'
  # params = (id)

  try:
    with engine.connect() as conn:
      conn.execute(sql)
  
  except SQLAlchemyError as e:
    raise Exception(f'Cannot connect HIS table while deleting id {id}. {e}')
