class Student:  # this class represents a node in the linked list that is each student

    def __init__(self, number):

        self.id = number
        self.next = None
        self.prev = None


class Circle:  # An object of this class is actually the circular linked list

    def __init__(self, num_students):

        cur_student = None  # points towards the last node that is last student inserted
        cur_student = self.insert_head(0)  # head student has zero ID

        for i in range(1, num_students):

            cur_student = self.append_student(cur_student, i)

    def insert_head(self, data):

        # using an object of student class, insert a node
        self.head_student = Student(data)
        self.head_student.next = self.head_student  # single node points to itself
        self.head_student.prev = self.head_student  # single node points to itself
        return self.head_student

    def append_student(self, curr_tail, data):

        if self.head_student is None:  # making sure head is present before calling append
            insert_head(0)

        else:
            self.new_student = Student(data)
            curr_tail.next = self.new_student
            self.new_student.prev = curr_tail
            self.new_student.next = self.head_student
            self.head_student.prev = self.new_student

        return self.new_student

    def print_list(self):

        iter_ptr = self.head_student
        print("At Student ID " + str(iter_ptr.id))
        iter_ptr = iter_ptr.next

        while iter_ptr.id != self.head_student.id:

            print("At Student ID " + str(iter_ptr.id))
            iter_ptr = iter_ptr.next

    '''
    def test_links(self,target_id):
        
        iter_ptr = self.head_student
        
        while iter_ptr.id != target_id:
            
            iter_ptr = iter_ptr.next
        
        print("Next Node ID is " + str(iter_ptr.next.id))
        print("Previous Node ID is " + str(iter_ptr.prev.id))
    '''

    def remove_node(self, remove_id):

        iter_ptr = self.head_student

        while iter_ptr.id != remove_id:

            iter_ptr = iter_ptr.next

        prev_node = iter_ptr.prev  # node previous to the one that we want to remove
        next_node = iter_ptr.next

        if iter_ptr == self.head_student:  # if head is removed. make sure to point head ptr of class in right direction
            self.head_student = next_node

        prev_node.next = next_node
        next_node.prev = prev_node

        print("Student " + str(remove_id) + " is removed")

    def Josephus_Solution_PartA(self):

        iter_ptr = self.head_student

        while self.head_student.next != self.head_student:  # means there is only one node left in the list

            for i in range(0, 1):
                iter_ptr = iter_ptr.next
            self.remove_node(iter_ptr.id)

            iter_ptr = iter_ptr.next

        print("Among 41 Students at Positions 0 - 40, to Win, I Should be Assigned Position " +
              str(iter_ptr.next.id))

    def Josephus_Solution_PartB(self, num_stud, skip_num):

        iter_ptr = self.head_student

        while self.head_student.next != self.head_student:  # means there is only one node left in the list

            for i in range(0, skip_num-1):
                iter_ptr = iter_ptr.next
            self.remove_node(iter_ptr.id)

            iter_ptr = iter_ptr.next

        print("Congratulations, Student " + str(iter_ptr.next.id) + "!")


# Driver Functions

print("First consider 41 students in a circle")
print("41 students in a circle having positions 0 to 40")
student_circleA = Circle(41)  # argument passed is number of students
student_circleA.Josephus_Solution_PartA()
print("")
print("")

print("Now consider variable 'k' number of students")
print("Enter number(n) of students, should be at least 2")
num_students = int(input())
print("Enter number(k) of students to skip, must be between 1 and n")
skip_num = int(input())
student_circleB = Circle(num_students)  # argument passed is number of students
student_circleB.Josephus_Solution_PartB(num_students, skip_num)
