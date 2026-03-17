
def total(galleons, sickles, knuts):
    return galleons * 17 * 29 + sickles * 29 + knuts

coins = [100, 50, 25]
print(total(*coins), "knuts")

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "knuts")

def f(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)