class Screen(object):
    @property
    def width(self):
        return self._width
    def height(self):
        return self._height
    @width.setter
    def width(self, value):
        self._width = value
    def height(self, value):
        self._height= vale
    @property
    def resolution(self):
        return self._width * self.height
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
