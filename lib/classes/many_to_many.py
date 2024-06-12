class Band:
    all = []
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        Band.all.append(self)
        self.played= [] 

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            if not isinstance(value, str) or not len(value) > 0:
                raise Exception
            self._name = value

        @property
        def hometown(self):
            return self._hometown

        @hometown.setter
        def hometown(self,value):
            if not isinstance(value, str) or not len(value) > 0:
                raise Exception
            self._hometown = value

    def concerts(self):
        return [show for show in Concert.all if show.band == self]

    def venues(self):
        return list(set(show.venue for show in self.concerts()))

    def play_in_venue(self, venue, date):
        show = Concert(date, self, venue)
        self.played.append(show)

    def all_introductions(self):
        return [show.introduction() for show in self.concerts()]


class Concert:
    all = []
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

        @property
        def date(self):
            return self._date

        @date.setter
        def date(self, value):
            if not (len(value)>0 and not isinstance(value,str) and not hasattr(value, "date")):
                raise ValueError("Invalid date")
            self._date = value

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all=[]
    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            if not isinstance(value, str) or not len(value) > 0:
                raise ValueError("Invalid name")
            self._name = value

        @property
        def city(self):
            return self._city

        @city.setter
        def city(self, value):
            if not isinstance(value, str) or not len(value) > 0:
                raise ValueError("Invalid city")
            self._city = value
    def concerts(self):
        return [show for show in Concert.all if show.venue == self]

    def bands(self):
        return list(set(show.band for show in self.concerts()))
    

    # bonus deliverables
    def concert_on(self, date):
        for show in self.concerts():
            if show.date == date:
                return show
        return None     
