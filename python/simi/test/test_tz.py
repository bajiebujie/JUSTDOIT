import dateutil.parser
import pytz

dt = dateutil.parser.parse("2018-10-29T08:59:38.447+0530")
print dt
utc_dt = dt.astimezone(pytz.timezone("UTC"))
print utc_dt
print dt.strftime("%w")
print dt.weekday()
print dt.hour
