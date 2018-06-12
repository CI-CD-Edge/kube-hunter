import logging
import requests
import json

class Event(object):
    def __init__(self):
        self.previous = None

    # newest attribute gets selected first
    def __getattr__(self, name):
        if name == "previous":
            return None
        for event in self.history:
            if name in event.__dict__:
                return event.__dict__[name]

    # returns the event history ordered from newest to oldest
    @property
    def history(self):
        previous, history = self.previous, list()
        while previous:
            history.append(previous)
            previous = previous.previous
        return history

"""Kubernetes Components"""
class KubernetesCluster():
    """Kubernetes Cluster"""
    name = "Kubernetes Cluster"

class Kubelet(KubernetesCluster):
    """The kubelet is the primary "node agent" that runs on each node"""
    name = "Kubelet"


""" Event Types """
# TODO: make proof an abstract method.
class Service(object):
    def __init__(self, name, path="", secure=False):
        self.name = name
        self.secure = secure
        self.path = path

    def get_name(self):
        return self.name

    def get_path(self):
        return "/" + self.path if self.path else ""

    def explain(self):
        return self.__doc__

    def proof(self):
        return self.name

class Vulnerability(object):
    def __init__(self, component, name):
        self.component = component
        self.name = name
        self.evidence = ""

    def get_name(self):
        return self.name

    def explain(self):
        return self.__doc__

class Information(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def explain(self):
        return self.__doc__
        
    def proof(self):
        return self.name


event_id_count = 0
""" Discovery/Hunting Events """
class NewHostEvent(Event):
    def __init__(self, host, cloud=None):
        global event_id_count
        self.host = host
        self.id = event_id_count
        self.cloud = cloud
        event_id_count += 1

    def __str__(self):
        return str(self.host)

class OpenPortEvent(Event):
    def __init__(self, port):
        self.port = port
    
    def __str__(self):
        return str(self.port)