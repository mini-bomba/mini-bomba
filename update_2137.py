import re
import datetime
import math

pattern = re.compile(r"<!--here2137goes-->\n(?:.*\n){3}<!--end2137-->")

fnow = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
now = fnow.replace(second=0, microsecond=0)
if now.hour == 21 and now.minute == 37:
    text = "####**It's now 21:37!** (UTC+2)"
else:
    next2137 = now.replace(hour=21, minute=37, second=0, microsecond=0)
    if now.hour >= 22 or (now.hour == 21 and now.minute > 37):
        next2137 += datetime.timedelta(days=1)
    eta2137 = next2137 - now
    mins = math.ceil(eta2137.seconds / 60)
    hours = mins // 60
    mins %= 60
    arr = []
    if hours > 0:
        arr.append(f'{hours} hours')
    if mins > 0:
        arr.append(f'{mins} minutes')
    text = f"21:37 will be in **{' and '.join(arr)}** (UTC+2)"

text += f"\n\n*Last updated: {fnow.strftime('%H:%M:%S')} (UTC+2)*"

with open("README.md", "r") as f:
    readme = f.read()

readme = pattern.sub(f"<!--here2137goes-->\n{text}\n<!--end2137-->", readme)

with open("README.md", "w") as f:
    f.write(readme)
