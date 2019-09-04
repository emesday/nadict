class NaDict(dict):
    def __getattr__(self, key):
        if key not in self:
            self[key] = NaDict()
        if key in self:
            return self[key]

    def __setattr__(self, key, val):
        if key in self.__dict__:
            self.__dict__[key] = val
        else:
            self[key] = val

    def as_dict(self):
        r = {}
        for k, v in self.items():
            r.update(self._as_dict(k, v))
        return r

    def _as_dict(self, parent, children):
        if not children:
            return {}
        else:
            if isinstance(children, dict):
                r = {}
                for k, v in children.items():
                    r.update(self._as_dict('.'.join([parent, k]), v))
                return r
            else:
                return {parent: children}

