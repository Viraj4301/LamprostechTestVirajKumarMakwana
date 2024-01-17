from collections import defaultdict, deque

def find_course_order(num_courses, prerequisites):
    # Creaing a graph
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    # build graph
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Initialize a queue with courses that have no prerequisites
    queue = deque([course for course in range(num_courses) if in_degree[course] == 0])
    
    # Initialize the result order
    course_order = []
    
    # Perform topological sort
    while queue:
        current_course = queue.popleft()
        course_order.append(current_course)
        
        # Update in-degrees of neighboring courses
        for neighbor_course in graph[current_course]:
            in_degree[neighbor_course] -= 1
            
            # If the neighbor course has no more prerequisites, add it to the queue
            if in_degree[neighbor_course] == 0:
                queue.append(neighbor_course)
    
    # Check if all courses are included in the order
    if len(course_order) == num_courses:
        return course_order
    else:
        # If there is a cycle, return an empty list
        return []

#Example
num_courses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
result = find_course_order(num_courses, prerequisites)
print(result)
