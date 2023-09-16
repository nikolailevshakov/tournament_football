import channel_posts
import schedule
import jobs
import utils
import time

schedule.every().monday.at("20:00").do(channel_posts.post_results())
schedule.every().tuesday.at("20:00").do(jobs.clear_current_week())
schedule.every().wednesday.at("20:00").do(channel_posts.post_with_header("Игры этой недели!", utils.read_games()))
schedule.every().friday.at("20:00").do(channel_posts.check_if_prediction_exists())

while True:
    schedule.run_pending()
    time.sleep(1)