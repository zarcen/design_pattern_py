from observer import *
from observer import *
from observer.mysubject import MySubject
from observer.observer_stdout import ObserverStdout
from observer.observer_stderr import ObserverStderr

def test_observer():
    ob_ext = None
    with MySubject() as sub:
        with ObserverStdout(sub) as ob1, ObserverStderr(sub) as ob2:
            # assert cxt mgmt that 2 observers are attached
            assert len(sub._observers) == 2
            # assert observers have initial states (-1)
            assert ob1.foo == -1
            assert ob1.bar == -1
            assert ob2.foo == -1
            assert ob2.bar == -1
            sub.set_states(2, 0)
            # assert observers get notified and update the states from observant(subject)
            assert ob1.foo == 2
            assert ob1.bar == 0
            assert ob2.foo == 2
            assert ob2.bar == 0
        # assert cxt mgmt that observers detached themselves
        assert len(sub._observers) == 0
        ob_ext = ObserverStdout(sub)
        assert len(sub._observers) == 1
        assert ob_ext.foo == 2
        assert ob_ext.bar == 0
        sub.set_states(3, 9)
        # assert ob_ext is notified
        assert ob_ext.foo == 3
        assert ob_ext.bar == 9
        # assert ob1 is *NOT* notified
        assert ob1.foo == 2
        assert ob1.bar == 0
    # assert cxt mgmt that subject clears all observers
    assert len(sub._observers) == 0
    sub.set_states(9, 2)
    # assert ob_ext is *NOT* notified
    assert ob_ext.foo == 3
    assert ob_ext.bar == 9
