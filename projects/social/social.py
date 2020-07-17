import random
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Add friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
        {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
        """

        visited = {}
        queue = Queue()
        queue.enqueue([user_id])

        while queue.size() > 0:

            path = queue.dequeue()

            # print(f" PATH: {path}")
            vertex = path[-1]
            # print(f" VERTEX: {vertex}")

            if vertex not in visited:
                # print("VERTEX NOT IN VISITED")
                visited[vertex] = path
                # print(f" VIS VERTEX: {visited[vertex]}")


                for neighbor in self.friendships[vertex]:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    queue.enqueue(new_path)
        return visited


'''     
3. Questions

To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why?
500 because the add_friendships code is the number of users (100) multiplied by the average friends (10) divided by 2 : (500).

If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? 
What is the average degree of separation between a user and those in his/her extended network?

5% of users in extended network?
Avg degree of separation 2?


'''


'''
    # the key is the user ID
    # the value is the path
    # the path is the BFS
    
            # 
            
            
    # visited = {}
    # q = Queue()
    # q.enqueue([user_id])
    # while q.size() > 0:
    #     path = q.dequeue()
    #     user_key = path[-1]
    #     if user_key in visited:
    #         if len(path) < len(visited[user_key]):
    #             visited[user_key] = path.copy()
    #     else:
    #         for friend in self.friendships[user_key]:
    #             visited[user_key] = path.copy()
    #             copy = path.copy()
    #             copy.append(friend)
    #             q.enqueue(copy)
    
    
    # for k in self.friendships:
    #     visited[k] = False
    #
    # for k in self.friendships:
    #     if visited[k] == False:
    #         visited[k] = True
        # visited[k] = 0
        # if self.friendships[k] not in visited:
        #     visited[k] = 1
        # print (visited)
    # can I print all the users in user 1's extended network?
        # print(self.friendships[user_id])
        # for {1: {8, 4} this prints:
        # {8, 4}

    # can I find the shortest path between two users?
        # {1: {8, 4}
        # {1: [1], 8: [1, 8]
'''





class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
'''
>>> print(sg.friendships)
{1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
>>> connections = sg.get_all_social_paths(1)
>>> print(connections)
{1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}

Hint 1: What kind of graph search guarantees you a shortest path?
- BFS?

Hint 2: Instead of using a set to mark users as visited, you could use a dictionary. Similar to sets, 
checking if something is in a dictionary runs in O(1) time. If the visited user is the key, what would the value be?

We could set the value to True or 1?

'''





if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    # print(sg.get_all_social_paths(1))
    connections = sg.get_all_social_paths(1)
    print(connections)
