from sys import stdin
import re


def memoized(function):
    memo = {}
    def wrapper(*args):
        if args not in memo:
            memo[args] = function(*args)
        return memo[args]
    return wrapper

class Topic:
    def __init__(self, topic):
        self.topic = topic
        self.children = []
        self._questions = set()
    
    def add_children(self, others):
        self.children.extend(others)

    def add_question(self, question):
        self._questions.add(question)

    @property
    @memoized
    def descendents(self):
        self._descendents = [self]
        for child in self.children:
            self._descendents.extend(child.descendents)
        return self._descendents

    @property
    @memoized
    def questions(self):
        for descentent in self.descendents[1:]:
            self._questions |= descentent.questions
        return self._questions

    def __str__(self):
        self._name = self.topic
        if any(self.children):
            self._name += ' ( '
            self._name += ' '.join(map(str, self.children))
            self._name += ' ) '

        return self._name

question_pat = re.compile(r'^(\w+): ([\w ?]+)$')
query_pat = re.compile(r'^(\w+) ([\w ]+)$')

if __name__ == '__main__':
    N = int(stdin.readline()) # nb of topics
    topics = {}
    children = []
    next_is_parent = False
    for s in reversed(stdin.readline().split()):
        if s == '(':
            next_is_parent = True
        elif s != ')':
            topic = Topic(s)
            if next_is_parent:
                next_is_parent = False
                topic.add_children(children)
                children = []
            children.append(topic)
            topics[s] = topic

    M = int(stdin.readline()) # nb of questions
    for _ in range(M):
        line = stdin.readline()
        topic, question = question_pat.match(line).groups()
        topics[topic].add_question(question)

    K = int(stdin.readline()) # nb of queries
    for _ in range(K):
        line = stdin.readline()
        topic, query = query_pat.match(line).groups()
        answers = filter(lambda s: s.startswith(query), topics[topic].questions)
        print(len(list(answers)))