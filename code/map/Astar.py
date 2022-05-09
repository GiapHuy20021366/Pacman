class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, __o: object) -> bool:
        return self.position == __o.position


def astar_findpath(maze, start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    list_open = []
    list_closed = []

    # Add the start node
    list_open.append(start_node)

    # Loop until you find the end
    while len(list_open) > 0:

        # Get the current node
        curr_node = list_open[0]
        curr_index = 0
        for index, item in enumerate(list_open):
            if item.f < curr_node.f:
                curr_node = item
                curr_index = index

        # Pop current off open list, add to closed list
        list_open.pop(curr_index)
        list_closed.append(curr_node)

        # Found the goal
        if curr_node == end_node:
            path = []
            curr = curr_node
            while curr is not None:
                path.append(curr.position)
                curr = curr.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_pos = (curr_node.position[0] + new_position[0], curr_node.position[1] + new_position[1])

            # Make sure within range
            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze)-1]) -1) or node_pos[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_pos[0]][node_pos[1]] != 0:
                continue

            # Create new node
            new_node = Node(curr_node, node_pos)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in list_closed:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = curr_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in list_open:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            list_open.append(child)

if __name__ == '__main__':
    
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar_findpath(maze, start, end)
    print(path)