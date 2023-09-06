import sql
import utils


def clear_current_week():
    sql.clear_current_week()
    utils.clear_games()
