from PySide2.QtCore import QSortFilterProxyModel, Qt

class PortFilterProxyModel(QSortFilterProxyModel):

    def __init__(self, *args, **kwargs):
        QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.filters = {}

    def setFilterByColumn(self, match, column):
        self.filters[column] = match
        self.invalidateFilter()

    def clearFilters(self):
        self.filters = {}
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        for key, match in self.filters.items():
            index = self.sourceModel().index(source_row, key, source_parent)
            if index.isValid():
                text = self.sourceModel().data(index, Qt.DisplayRole)
                if match != str(text).strip():
                    return False
        return True