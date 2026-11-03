def search_by_title(self, title):
        for dvd in self.items:
            if dvd.title == title:
                return dvd
        return None