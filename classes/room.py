class Room:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_guests = []
        self.playlist = []

    def check_in_guest(self, guest):
        self.current_guests.append(guest)
        return self.current_guests

    def check_out_guest(self, guest):
        self.current_guests.remove(guest)
        return self.current_guests

    def add_to_playlist(self, song):
        self.playlist.append(song)