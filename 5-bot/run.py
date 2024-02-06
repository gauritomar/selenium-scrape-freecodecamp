from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.select_place_to_go('New York')
    bot.select_dates('2024-02-16', '2024-02-24')
    bot.select_adults(2)