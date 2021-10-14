import abc
from observer import AbsObserver

class AbsSubject(object):
    __metaclass__ = abc.ABCMeta
    _observers = set()
    
    @abc.abstractmethod
    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers |= {observer}

    @abc.abstractmethod        
    def detach(self, observer):
        self._observers -= {observer}
        
    @abc.abstractmethod
    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self._observers.clear()