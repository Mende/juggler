import jug
import sys

jv1 = int(input('Jug 1 capacity:'), 10)

jv2 = int(input('Jug 2 capacity:'), 10)

if jv1 == jv2:
    print('jugs can\'t have equal capacity')
    sys.exit(1)

tv = int(input('Target Volume:'), 10)

if tv > jv1 and tv > jv2:
    print('target volume can\'t be larger than jug capacities')
    sys.exit(1)

smaller = jug.Jug(min(jv1, jv2), 'Jug 1')
larger = jug.Jug(max(jv1, jv2), 'Jug 2')


def getGCD(a, b):
    print('comparing: ', a, ':', b)
    larger = max(a, b)
    smaller = min(a, b)
    if larger != smaller:
        smaller = getGCD(larger - smaller, smaller)

    return smaller


def makeMove(smaller, larger):
    if smaller.is_empty():
        smaller.fill()
        print('filling smaller', smaller.current_volume, larger.current_volume)
        return True

    if larger.is_full():
        larger.dump()
        print('dumping larger', smaller.current_volume, larger.current_volume)
        return True

    if not(smaller.is_empty()):
        smaller.transfer(larger)
        print('transfer sm to lg',
              smaller.current_volume, larger.current_volume)
        return True


gcd = getGCD(smaller.capacity, larger.capacity)

if tv % gcd != 0:
    print('no solution possible')
    sys.exit(0)
keep_looping = not(larger.has_target_volume(
    tv) or smaller.has_target_volume(tv))

print('making moves...')
while keep_looping:
    makeMove(smaller, larger)
    keep_looping = not(larger.has_target_volume(
        tv) or smaller.has_target_volume(tv))

print('found target volume')
print(smaller.current_volume)
print(larger.current_volume)
sys.exit(0)
