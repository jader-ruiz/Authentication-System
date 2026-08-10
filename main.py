import services.database as db

db.create_table()

from gui.login import Login

main = Login()
main.run()

