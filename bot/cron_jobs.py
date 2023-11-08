import channel_posts
import utils
import sys

if sys.argv[1] == "monday":
    if not utils.if_games_empty():
        channel_posts.post_results()
elif sys.argv[1] == "wednesday":
    if not utils.if_games_empty():
        channel_posts.post_with_header("🎮⚽Игры этой недели!⚽🎮\n", utils.read_games() + utils.interest_fact_team())
elif sys.argv[1] == "friday":
    if not utils.if_games_empty():
        channel_posts.check_if_prediction_exists()
