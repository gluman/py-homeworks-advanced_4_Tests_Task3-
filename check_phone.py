import regex as re
def check_phone_number(number):
    pattern = r'(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})'
    subb = r'+7 \1 \2 ***-**-\5'
    subbmit_phone = re.sub(pattern, subb, number)
    return subbmit_phone