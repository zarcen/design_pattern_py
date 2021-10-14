from observer import AbsSubject

class MySubject(AbsSubject):
    _foo = -1
    _bar = -1
        
    @property
    def foo(self):
        return self._foo 
    
    @property
    def bar(self):
        return self._bar

    def set_states(self, new_foo, new_bar):
        self._foo = new_foo
        self._bar = new_bar
        self.notify()