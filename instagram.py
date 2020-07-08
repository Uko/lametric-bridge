from igramscraper.instagram import Instagram

instagram = Instagram()

def follower_count():
    account = instagram.get_account('terpuhlabs_ua')
    return account.followed_by_count
