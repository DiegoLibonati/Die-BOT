import random
from collections import deque

from cfg import cfg


class Playlist:
    

    def __init__(self):
       
        self.playque = deque()
        self.playhistory = deque()

        
        self.trackname_history = deque()

        self.loop = False

    def __len__(self):
        return len(self.playque)

    def add_name(self, trackname):
        self.trackname_history.append(trackname)
        if len(self.trackname_history) > cfg.MAX_TRACKNAME_HISTORY_LENGTH:
            self.trackname_history.popleft()

    def add(self, track):
        self.playque.append(track)

    def next(self, song_played):

        if self.loop == True:
            self.playque.appendleft(self.playhistory[-1])

        if len(self.playque) == 0:
            return None

        if len(self.playque) == 0:
            return None

        if song_played != "Dummy":
            if len(self.playhistory) > cfg.MAX_HISTORY_LENGTH:
                self.playhistory.popleft()

        return self.playque[0]

    def prev(self, current_song):

        if current_song is None:
            self.playque.appendleft(self.playhistory[-1])
            return self.playque[0]

        ind = self.playhistory.index(current_song)
        self.playque.appendleft(self.playhistory[ind - 1])
        if current_song != None:
            self.playque.insert(1, current_song)

    def shuffle(self):
        random.shuffle(self.playque)

    def move(self, oldindex: int, newindex: int):
        temp = self.playque[oldindex]
        del self.playque[oldindex]
        self.playque.insert(newindex, temp)

    def empty(self):
        self.playque.clear()
        self.playhistory.clear()
