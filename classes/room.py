class Room:
    def __init__(self, capacity, room_num, room_cost):
        self.capacity = capacity
        self.current_guests = []
        self.playlist = []
        self.room_num = room_num
        self.room_cost = room_cost

    def check_in_guest(self, guest):
        if len(self.current_guests) < self.capacity:
            self.current_guests.append(guest)
        else:
            return f"Room capacity is {self.capacity}"

    def check_out_guest(self, guest):
        self.current_guests.remove(guest)

    def add_to_playlist(self, song):
        self.playlist.append(song)

    