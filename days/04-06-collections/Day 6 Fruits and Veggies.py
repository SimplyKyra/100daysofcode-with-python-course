

# Collections to keep track of fruits and veggies eaten and water drank
# defunct because of Pandas or sqlite
from collections import defaultdict, namedtuple
import datetime
from datetime import timedelta
from datetime import date





# Movie = namedtuple('Movie', 'title year score')
# directors = defaultdict(list)
#     with open(data, encoding='utf-8') as f:
#         for line in csv.DictReader(f):
#             try:
#                 director = line['director_name']
#                 movie = line['movie_title'].replace('\xa0', '')
#                 year = int(line['title_year'])
#                 score = float(line['imdb_score'])
#             except ValueError:
#                 continue
#
#             m = Movie(title=movie, year=year, score=score)
#             directors[director].append(m)


Tracker = namedtuple('Tracker', 'date_entered veggie_serving fruit_serving water_amount')
tracking = {} #dict

# Hard-coded for now

temp_data = [
    [datetime.datetime.now(), 4, 0, 8],
    [datetime.datetime.now() + timedelta(days=1), 2, 4, 6],
    [datetime.datetime.now(), 6, 7, 23],
    [datetime.datetime(2018, 5, 5, 16, 20, 42, 518352), 3, 5, 7],
    [datetime.datetime(2018, 5, 5, 20, 20, 42, 518352), 3, 5, 7]

]

# load up tracking
for i in range(len(temp_data)):
    temp = Tracker(date_entered=temp_data[i][0],
                    veggie_serving=temp_data[i][1],
                    fruit_serving=temp_data[i][2],
                    water_amount=temp_data[i][3])
    tracking[temp_data[i][0]] = temp


print(tracking)



def get_daily_tracking_details(tracking):
    # Goes through the total tracking dict and returns a result for each day
    for date_entered, numbers in tracking.items():
        print(f"/n {date_entered}   {numbers.veggie_serving}  {numbers.fruit_serving }   {numbers.water_amount}")
#     print(tracking[0])
#     temp = tracking[0]
#     for date_entered, veggie_serving, fruit_serving, water_amount in tracking.items():
#         print(f"For day {date_entered} the veggies were {veggie_serving}, fruit were {fruit_serving}, and water was {water_amount}")
#
#
get_daily_tracking_details(tracking)
#
