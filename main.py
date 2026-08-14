import services.database as db

db.create_table()
#db.add_role_column()

from gui.login import Login

main = Login()
main.run()

