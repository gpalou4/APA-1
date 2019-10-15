import sys, csv, re, math

class Node:
  def __init__(self, loci, position):
    chromosome_regex = '^(?P<number>\d+)(?P<letter>[a-zA-Z])(?P<position>\d+\.\d+)$'
    matches = re.match(chromosome_regex, loci).groupdict()
    self._chromosome_arm_number = int(matches['number'])
    self._chromosome_arm_letter = matches['letter']
    self._chromosome_arm_position = float(matches['position'])
    self._position = position
    self._frequency = 0
    self.next = None

  def is_matching_within_distance(self, node, distance_threshold):
    if self.get_chromsome_arm() != node.get_chromsome_arm():
      return False

    position = node.get_position()
    distance = math.sqrt(
      math.pow(self._position[0] - position[0], 2)
      + math.pow(self._position[1] - position[1], 2)
    )
    return distance <= distance_threshold

  """
    When two nodes are on the same chromosome number and letter, compare the position.
    When two nodes are on the same chromosome number, compare the letter.
    When two nodes are on different chromosome numbers, compare just the numbers.
  """
  def has_larger_loci(self, node):
    arm_number = node.get_chromosome_arm_number()
    arm_letter = node.get_chromosome_arm_letter()
    arm_position = node.get_chromosome_arm_position()

    if self._chromosome_arm_number == arm_number:
      if self._chromosome_arm_letter == arm_letter:
        return self._chromosome_arm_position > arm_position

      return self._chromosome_arm_letter > arm_letter
    return self._chromosome_arm_number > arm_number

  def increment_frequency(self):
    self._frequency += 1

  def get_frequency(self):
    return self._frequency

  def get_chromsome_arm(self):
    return str(self._chromosome_arm_number) + self._chromosome_arm_letter

  def get_position(self):
    return self._position

  def get_chromosome_arm_number(self):
    return self._chromosome_arm_number

  def get_chromosome_arm_letter(self):
    return self._chromosome_arm_letter

  def get_chromosome_arm_position(self):
    return self._chromosome_arm_position


def read_file_to_linked_list(file_name):
  head = None
  tail = None
  with open(file_name, 'r') as file:
    tsv_reader = csv.reader(file, delimiter='\t')

    for row in tsv_reader:
      node = convert_row_to_node(row)
      if head is None:
        head = node
        tail = node
      else:
        tail.next = node
        tail = node
  return head


def convert_row_to_node(row):
  coordinates = re.sub('\(|\)', '', row[2]).split(',')
  position = tuple(map(float, coordinates))
  return Node(row[1], position)


def sort_linked_list(head):
  sorted_list = head
  node = head.next
  sorted_list.next = None

  while node is not None:
    current_node = node
    node = node.next

    # Current node belongs before the spot in the sorted list
    if sorted_list.has_larger_loci(current_node):
      current_node.next = sorted_list
      sorted_list = current_node

    # Find the spot in the sorted list that the value belongs
    else:
      tracking_node = sorted_list
      while tracking_node.next and current_node.has_larger_loci(tracking_node.next):
        tracking_node = tracking_node.next

      # Insert current_node in the position of tracking_node and continue list after
      current_node.next = tracking_node.next
      tracking_node.next = current_node

  return sorted_list


def increment_node_frequencies(sorted_list_head, distance_threshold):
  node = sorted_list_head
  while node is not None:
    tracking_node = node.next

    while tracking_node is not None:
      if node != tracking_node and node.is_matching_within_distance(tracking_node, distance_threshold):
        node.increment_frequency()

      tracking_node = tracking_node.next
    node = node.next


def write_linked_list_to_file(sorted_list_head, file_name):
  with open(file_name, 'w') as file:
    tsv_writer = csv.writer(file, delimiter='\t')

    node = sorted_list_head
    chromosome_arm = node.get_chromsome_arm()
    frequency_sum = 0

    # Sum all frequencies for nodes with matching chromosome arms, after
    # reaching a different chromosome arm, write the previous frequency.
    while node is not None:
      current_chromosome_arm = node.get_chromsome_arm()
      if current_chromosome_arm == chromosome_arm:
        frequency_sum += node.get_frequency()
      else:
        tsv_writer.writerow([chromosome_arm, frequency_sum])
        frequency_sum = node.get_frequency()
        chromosome_arm = current_chromosome_arm

      node = node.next

    # Account for final chromosome arm after reaching the None node
    tsv_writer.writerow([current_chromosome_arm, frequency_sum])


if __name__ == '__main__':
  if len(sys.argv) < 3:
    print('Missing file name or distance threshold')
    sys.exit(1)

  file_name, distance_threshold = sys.argv[1:3]
  distance_threshold = float(distance_threshold)

  head = read_file_to_linked_list(file_name)
  sorted_list_head = sort_linked_list(head)
  increment_node_frequencies(sorted_list_head, distance_threshold)
  write_linked_list_to_file(sorted_list_head, './output.tsv')