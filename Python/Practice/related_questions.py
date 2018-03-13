from sys import stdin

def memoize(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  return wrapper

class Question:
    def __init__(self, index, time):
        self.index = index
        self.parent = None
        self.child = None       
        # times until no more related questions from this
        self.time = time
    
    def relate(self, other):
        self.child = other
        other.parent = self

    @property
    @memoize
    def time_up(self):
        if not self.parent:
            return self.time
        return self.time + self.parent.time_up

    @property
    @memoize
    def time_down(self):
        if not self.child:
            return self.time
        return self.time + self.child.time_down


if __name__ == '__main__':
    # Number of questions
    N = int(stdin.readline())
    # Time to read each question
    T = list(map(int, stdin.readline().split()))
    # Make  list of question where the index in the list matchese the index of the question
    questions = [Question(i, t) for i, t in zip(range(1, N+1), T)]
    questions.insert(0, None)
    
    for line in stdin:
        i1, i2 = tuple(map(int, line.split()))
        questions[i1].relate(questions[i2])

    best_q= questions[1]
    best_t = max(best_q.time_up, best_q.time_down)
    for q in questions[2:]:
        t = max(q.time_up, q.time_down)
        if t < best_t:
            best_q = q
            best_t = t
    
    print(best_q.index)


    
