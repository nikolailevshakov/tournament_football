import sys
sys.path.append('../bot')
import sql
import utils

sql.clear_current_week()
utils.clear_games()