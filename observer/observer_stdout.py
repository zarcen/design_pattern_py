from observer import AbsObserver

class ObserverStdout(AbsObserver):
    foo = -1
    bar = -1

    def __init__(self, subject):
        self._subject = subject
        # ---- let subject attach this observer ----
        self._subject.attach(self)
        self.update()
        # ------------------------------------------

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Context management
        ensure observer detached from the subject
        """
        self._subject.detach(self)
    
    def update(self):
        # update states from subject
        self.foo = self._subject.foo
        self.bar = self._subject.bar
        self.printToStdout()
        
    def printToStdout(self):
        print(f'foo {self.foo}')
        print(f'bar {self.bar}')