reddit_url = 'https://reddit.com{}'

summoned_submit_title = (
    '{sub} | {title} | We\'ve been summoned for a {commentorpost}!'
)

discovered_submit_title = (
    '{sub} | {type} | "{title}"'
)

id_already_handled_in_db = 'We\'ve already handled ID {}! Skipping!'

rules_comment = (
    'If you would like to claim this post, please respond to this comment '
    'with the word `claiming` or `claim` in your response. I will automatically '
    'update the flair so that only one person is working on a post at any given '
    'time.'
    '\n\nWhen you\'re done, please comment again with `done`. Your flair will '
    'be updated to reflect the number of posts you\'ve transcribed and the '
    'will be marked as completed.'
    '\n\nThis is a(n) {post_type} post, so please use the following formatting:'
    '\n\n---\n\n{formatting}\n\n---'
    '\n\nIf you have any questions, feel free to [message the mods!]'
    '(https://www.reddit.com/message/'
    'compose?to=%2Fr%2FTranscribersOfReddit&subject=General%20Question'
    '&message=)'
)

rules_comment_unknown_format = (
    'If you would like to claim this post, please respond to this comment '
    'with the word `claiming` or `claim` in your response. I will automatically '
    'update the flair so that only one person is working on a post at any given '
    'time.'
    '\n\nWhen you\'re done, please comment again with `done`. Your flair will '
    'be updated to reflect the number of posts you\'ve transcribed and the '
    'will be marked as completed.'
    '\n\nWe do not know what type of formatting the above post has, but if '
    'one of the mods finds it we will update this comment. Otherwise please '
    'refer to the sidebar for further information.\n\n---'
    '\n\nIf you have any questions, feel free to [message the mods.]'
    '(https://www.reddit.com/message/'
    'compose?to=%2Fr%2FTranscribersOfReddit&subject=General%20Question'
    '&message=)'
)

bot_footer = (
    "{}\n\n---\nv. {version} | This message was posted by a bot. "
    "| [FAQ](https://www.reddit.com/r/TranscribersOfReddit/wiki/index) "
    "| Questions? [Message the mods!](https://www.reddit.com/message/"
    "compose?to=%2Fr%2FTranscribersOfReddit&subject=Bot%20Question"
    "&message=)"
)

claim_success = (
    'The post is yours! Best of luck and thanks for helping!\n\nPlease respond '
    'with "done" when complete so we can check this one off the list!'
)

already_claimed = (
    'I\'m sorry, but it looks like someone else has already claimed this post! '
    'You can check in with them to see if they need any help, but otherwise I '
    'suggest sticking around to see if another post pops up here in a little bit.'
)

claim_already_complete = (
    'This post has already been completed! Perhaps you can find a new one on the '
    'front page?'
)

done_still_unclaimed = (
    'This post is still unclaimed! Please claim it first or message the mods to'
    ' take care of this.'
)

done_completed_transcript = (
    'Awesome, thanks for your help! I\'ll update your flair to reflect your new count.'
)

done_cannot_find_transcript = (
    'Sorry; I can\'t find your transcript post on the link. Please message the '
    'mods to have them look at this.'
)