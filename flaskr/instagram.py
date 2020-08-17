from igramscraper.instagram import Instagram

instagram = Instagram()

def follower_count(account_name):
    account = instagram.get_account(account_name)
    return account.followed_by_count
