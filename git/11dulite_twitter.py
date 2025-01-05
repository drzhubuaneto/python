from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> str:
        pass


class User(Observer):
    def __init__(self, name: str):
        self._name = name
        self._follows = []
        self._feed = []

    def add_follows(self, user):
        self._follows.append(user)

    def get_follows(self):
        return self._follows

    def add_user_tweet(self, message):
        self._feed.append(message)
        
    def update(self,original_seder, message):
        return f"{self._name}: {original_seder} tweets: {message}"
    
    def __str__(self):
        return f"{self._name}"
    
class Observable(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, message: str):
        pass

class Twitter(Observable):
    def __init__(self):
        self._users = []

    def register_observer(self, user: User):
        self._users.append(user)

    def notify(self, message, original_sender: User):
        for user in self._users:
            if(original_sender in user.get_follows()):
                print(user.update(original_sender, message))
    
    def add_tweet(self, user: User, message):
        user.add_user_tweet(message)
        self.notify(message, user)

if __name__ == "__main__":
    user1 = User("user1")
    user2 = User("user2")
    user3 = User("user3")

    twitter = Twitter()

    twitter.register_observer(user1)
    twitter.register_observer(user2)
    twitter.register_observer(user3)

    user1.add_follows(user2)
    user1.add_follows(user3)
    user2.add_follows(user3)
    user3.add_follows(user1)
    user3.add_follows(user2)

    print()
    twitter.add_tweet(user1,"Tweet for user3")
    twitter.add_tweet(user2,"Tweet for user 1 and 3")
    twitter.add_tweet(user3,"Tweet for user 1 and 2")


    pass
