class Node:
    def __init__(self, _name):
        self.name = _name
        self.pipes = set()

    def add_pipe(self, pipename):
        self.pipes.add(pipename)

    def add_pipes(self, pipelist):
        self.pipes = self.pipes | set(pipelist)
