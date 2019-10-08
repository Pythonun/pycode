ln_path = '~/downloads/d.txt'
fn_path = '~/downloads/d.txt'
fn = []
ln1 = []
ln2 = []
with open(fn_path,'r') as f:
    for line in f.readlines():
        fn.append(line.split('\n')[0])
print(fn)
with open(ln_path,'r') as f:
    for line in f.readlines():
        if len(line.split('\n')[0]) == 1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])
print(ln1)
print('='*70)
print(ln2)

import random
class FakeUser:
    def fake_name(self,amount=1,one_word=False,two_word=False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
            yield full_name
            n += 1
    def fake_gender(self,amount=1):
        gender = random.choice(['man','woman','unknown'])
        yield gender
        n += 1

class SnsUser(FakeUser):
    def get_followers(self,few=True,a_lot=False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1,50)
            elif a_lot:
                followers = random.randrange(200,10000)
            yield followers
            n += 1
user_a = FakerUser()
user_b = SnsUser()
for name in user_a.fake_name(30):
    print(name)
for name in user_b.fake_gemder(30):
    print(gender)
