class BrowserHistory:

    def __init__(self, homepage: str):
        # 访问流程
        self.page_list = []
        # 初始化第一个浏览界面
        self.page_list.append(homepage)
        # 设置当前页面指针
        self.page_point = 0

    def visit(self, url: str) -> None:
        # 清空前进列表
        self.page_list = self.page_list[:self.page_point+1]
        # 将这个界面加入到访问列表
        self.page_list.append(url)
        # 指针右移
        self.page_point += 1

    def back(self, steps: int) -> str:
        if steps >= self.page_point:
            self.page_point = 0
            return self.page_list[self.page_point]
        else:
            self.page_point -= steps
            return self.page_list[self.page_point]

    def forward(self, steps: int) -> str:
        if steps >= (len(self.page_list) - 1) - self.page_point:
            self.page_point = (len(self.page_list) - 1)
            return self.page_list[self.page_point]
        else:
            self.page_point += steps
            return self.page_list[self.page_point]
