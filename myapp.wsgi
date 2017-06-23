import psycopg2

def application(environ, start_response):
  status = '200 OK'
  output = str(get_num_dancers()) + " dancers in the database right now!"

  response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
  start_response(status, response_headers)

  return [output]


def get_connection():
  return psycopg2.connect("dbname=test")


def get_num_dancers():
  """Returns all dancers from the database"""
  conn = get_connection()
  cur  = conn.cursor()
  cur.execute("SELECT count(*) from dancers;")
  num_dancers = cur.fetchone()
  conn.close()

  return num_dancers[0]
