import logging
import sys
import time
from datetime import datetime

import prawcore
from praw import Reddit

from tor.core.config import config
from tor.core.initialize import configure_logging
from tor.core.initialize import configure_tor
from tor.core.initialize import initialize
from tor.helpers.flair import css_flair
from tor.helpers.misc import explode_gracefully
from tor.helpers.misc import subreddit_from_url
from tor.strings.urls import reddit_url


# it all goes to the same log, so we name this something easy to identify
def run_archivist(tor, config, archive):
    # TODO the bot will now check ALL posts on the subreddit.
    # when we remove old transcription requests, there aren't too many left.
    # but we should make it stop after a certain amount of time anyway
    # eg. if it encounters a post >36 hours old, it will break the loop

    # TODO we can use .submissions(end=unixtime) apparently
    for post in tor.new(limit=1000):

        # [META] - do nothing
        # [UNCLAIMED] - remove
        # [COMPLETED] - remove and x-post to r/tor_archive
        # [IN PROGRESS] - do nothing (should discuss)
        # [DISREGARD] - remove
        flair = post.link_flair_css_class

        if flair not in (css_flair.unclaimed, css_flair.completed):
            continue

        # is it a disregard post? Nuke it and move on -- we don't want those
        # sitting around and cluttering up the sub
        if flair == css_flair.disregard:
            post.mod.remove()
            continue

        # find the original post subreddit
        # take it in lowercase so the config is case insensitive
        post_subreddit = subreddit_from_url(post.url).lower()

        # hours until a post from this subreddit should be archived
        hours = config.archive_time_subreddits.get(
            post_subreddit, config.archive_time_default)

        # time since this post was made
        date = datetime.utcfromtimestamp(post.created_utc)
        seconds = (datetime.utcnow() - date).seconds

        if seconds > hours * 3600:
            logging.info(
                'Post "{}" is older than maximum age of {} hours, removing.'.format(
                    post.title, hours)
            )

            # post.mod.remove()

            if flair == css_flair.completed:
                logging.info('Archiving completed post...')
                archive.submit(
                    post.title,
                    url=reddit_url.format(post.permalink))
                logging.info('Post archived!')


if __name__ == '__main__':
    r = Reddit('bot_archiver')

    configure_logging(config)

    tor = configure_tor(r, config)
    initialize(tor, config)
    logging.info('Initialization complete.')
    archive = r.subreddit('ToR_Archive')

    try:
        while True:
            run_archivist(tor, config, archive)
            time.sleep(300)  # 5 minutes

    except KeyboardInterrupt:
        logging.info('Received keyboard interrupt! Shutting down!')
        sys.exit(0)

    except (
        prawcore.exceptions.RequestException,
        prawcore.exceptions.ServerError,
        prawcore.exceptions.Forbidden
    ) as e:
        logging.warning(
            '{} - Issue communicating with Reddit. Sleeping for 60s!'
            ''.format(e)
        )
        time.sleep(60)

    except Exception as e:
        explode_gracefully('ToR_archivist', e, tor)
