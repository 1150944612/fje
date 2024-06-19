from abc import ABC, abstractmethod
from Factory import RectangleStyledJSONNodeFactory, TreeStyledJSONNodeFactory

class Visitor(ABC):
    @abstractmethod
    def visit(self, node, icon_family=None):
        pass

class TreeVisitor(Visitor):
    def visit(self, node, icon_family=None):
        return TreeStyledJSONNodeFactory(node, icon_family)

class RectangleVisitor(Visitor):
    def visit(self, node, icon_family=None):
        return RectangleStyledJSONNodeFactory(node, icon_family)
