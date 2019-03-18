class Interval:
    def __init__(self,s,e):
        self.start=s
        self.end=e


def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out

i1=Interval(1,2)
i2=Interval(1,3)
i3=Interval(1,4)
i4=Interval(5,7)
intervals=[i1,i2,i3,i4]

print(merge(intervals))